//! Executable conformance for the author-side PTS-0 pre-pin differential law.
//!
//! This checker contains no apparatus data and awards no scientific result.
//! It implements common-opportunity randomization, control descent, reader
//! aggregation, trace-veto semantics, core-versus-suite memory decisions, and
//! six finite physical parent controls fixed in the differential audit.

use std::fmt;

const OUTCOME_CELLS: usize = 32;
const UNIQUE_CELL_TYPES: usize = 148;
const REGISTERED_EDGES: usize = 80;
const EDGE_ARM_LAWS: usize = 2 * REGISTERED_EDGES;
const MACROBLOCKS: usize = 32;
const SIMULTANEOUS_ALPHA: f64 = 0.01;
const EMPIRICAL_LAW_TV_RADIUS: f64 = 0.0125;
const DISTANCE_CI_RADIUS: f64 = 0.025;
const MATCH_THRESHOLD: f64 = 0.10;
const SCREEN_PASS_THRESHOLD: f64 = 0.10;
const SCREEN_FAIL_THRESHOLD: f64 = 0.25;
const POWER_LOW: f64 = 0.05;
const POWER_HIGH: f64 = 0.30;
const TRACE_PASS_THRESHOLD: f64 = 0.05;
const TRACE_POWER_LOW: f64 = 0.025;
const TARGET_BETA: f64 = 0.01;
const CHOSEN_MICROBLOCKS_PER_EDGE: usize = 104_192;

type Law = [f64; OUTCOME_CELLS];

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Decision {
    Invalid,
    Pass,
    Fail,
    Underdetermined,
}

impl fmt::Display for Decision {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Decision::Invalid => write!(f, "INVALID"),
            Decision::Pass => write!(f, "PASS"),
            Decision::Fail => write!(f, "FAIL"),
            Decision::Underdetermined => write!(f, "UNDERDETERMINED"),
        }
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum BoundaryRowState {
    Invalid,
    MatchedPass,
    MatchedFail,
    MatchedUnresolved,
    BoundaryMismatch,
    BoundaryMatchUnresolved,
    ForcedRestart,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum EffectDirection {
    MustBePresent,
    MustBeAbsent,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum EvidenceState {
    Invalid,
    Satisfied,
    Contradicted,
    Unresolved,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum TraceState {
    Invalid,
    Clean,
    Contaminated,
    Unresolved,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Coordinate {
    Memory,
    B0,
    B1,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum ControlLift {
    Clear,
    Invalid,
    Underdetermined,
}

#[derive(Clone, Copy, Debug)]
struct Interval {
    lower: f64,
    upper: f64,
    nonempty: bool,
}

impl Interval {
    fn closed(lower: f64, upper: f64) -> Self {
        Self {
            lower,
            upper,
            nonempty: true,
        }
    }

    fn empty() -> Self {
        Self {
            lower: 0.0,
            upper: 0.0,
            nonempty: false,
        }
    }

    fn is_valid(self) -> bool {
        self.nonempty
            && self.lower.is_finite()
            && self.upper.is_finite()
            && 0.0 <= self.lower
            && self.lower <= self.upper
            && self.upper <= 1.0
    }
}

fn aggregate_max_interval(intervals: &[Interval]) -> Result<Interval, &'static str> {
    if intervals.is_empty() || intervals.iter().any(|interval| !interval.is_valid()) {
        return Err("reader interval family is empty or malformed");
    }
    Ok(Interval::closed(
        intervals
            .iter()
            .map(|interval| interval.lower)
            .fold(0.0, f64::max),
        intervals
            .iter()
            .map(|interval| interval.upper)
            .fold(0.0, f64::max),
    ))
}

fn classify_effect_interval(
    causal_valid: bool,
    direction: EffectDirection,
    interval: Interval,
) -> EvidenceState {
    if !causal_valid || !interval.is_valid() {
        return EvidenceState::Invalid;
    }
    match direction {
        EffectDirection::MustBePresent => {
            if interval.lower >= SCREEN_FAIL_THRESHOLD {
                EvidenceState::Satisfied
            } else if interval.upper <= SCREEN_PASS_THRESHOLD {
                EvidenceState::Contradicted
            } else {
                EvidenceState::Unresolved
            }
        }
        EffectDirection::MustBeAbsent => {
            if interval.upper <= SCREEN_PASS_THRESHOLD {
                EvidenceState::Satisfied
            } else if interval.lower >= SCREEN_FAIL_THRESHOLD {
                EvidenceState::Contradicted
            } else {
                EvidenceState::Unresolved
            }
        }
    }
}

fn classify_trace_interval(causal_valid: bool, interval: Interval) -> TraceState {
    if !causal_valid || !interval.is_valid() {
        return TraceState::Invalid;
    }
    if interval.upper <= TRACE_PASS_THRESHOLD {
        TraceState::Clean
    } else if interval.lower > TRACE_PASS_THRESHOLD {
        TraceState::Contaminated
    } else {
        TraceState::Unresolved
    }
}

fn classify_boundary_row(
    causal_valid: bool,
    full_boundary_forced_restart: bool,
    mismatch_readers: &[Interval],
    screen: Interval,
    left_trace: Interval,
    right_trace: Interval,
) -> BoundaryRowState {
    if !causal_valid {
        return BoundaryRowState::Invalid;
    }
    if full_boundary_forced_restart {
        return BoundaryRowState::ForcedRestart;
    }
    let mismatch = match aggregate_max_interval(mismatch_readers) {
        Ok(interval) => interval,
        Err(_) => return BoundaryRowState::Invalid,
    };
    if !screen.is_valid() {
        return BoundaryRowState::Invalid;
    }
    let trace_states = [
        classify_trace_interval(true, left_trace),
        classify_trace_interval(true, right_trace),
    ];
    if trace_states
        .iter()
        .any(|state| *state == TraceState::Invalid)
    {
        return BoundaryRowState::Invalid;
    }

    if mismatch.upper <= MATCH_THRESHOLD {
        if screen.upper <= SCREEN_PASS_THRESHOLD {
            if trace_states.iter().all(|state| *state == TraceState::Clean) {
                BoundaryRowState::MatchedPass
            } else {
                BoundaryRowState::MatchedUnresolved
            }
        } else if screen.lower >= SCREEN_FAIL_THRESHOLD {
            BoundaryRowState::MatchedFail
        } else {
            BoundaryRowState::MatchedUnresolved
        }
    } else if mismatch.lower > MATCH_THRESHOLD {
        BoundaryRowState::BoundaryMismatch
    } else {
        BoundaryRowState::BoundaryMatchUnresolved
    }
}

fn classify_boundary(rows: &[BoundaryRowState]) -> Decision {
    if rows.is_empty()
        || rows.iter().any(|state| {
            matches!(
                state,
                BoundaryRowState::Invalid | BoundaryRowState::ForcedRestart
            )
        })
    {
        return Decision::Invalid;
    }
    if rows
        .iter()
        .any(|state| *state == BoundaryRowState::MatchedFail)
    {
        return Decision::Fail;
    }
    if rows
        .iter()
        .all(|state| *state == BoundaryRowState::MatchedPass)
    {
        return Decision::Pass;
    }
    Decision::Underdetermined
}

const CONTROL_COUNT: usize = 8;

fn control_applies(control: usize, coordinate: Coordinate) -> bool {
    match control {
        0 | 1 => coordinate == Coordinate::B0,
        2 | 3 => coordinate == Coordinate::B1,
        4 => coordinate == Coordinate::Memory,
        5..=7 => true,
        _ => false,
    }
}

fn control_is_validity_null(control: usize) -> bool {
    matches!(control, 0 | 2 | 5 | 7)
}

fn classify_control_lift(
    coordinate: Coordinate,
    controls: &[EvidenceState; CONTROL_COUNT],
) -> ControlLift {
    let mut underdetermined = false;
    for (index, evidence) in controls.iter().enumerate() {
        if !control_applies(index, coordinate) {
            continue;
        }
        match evidence {
            EvidenceState::Invalid => return ControlLift::Invalid,
            EvidenceState::Contradicted if control_is_validity_null(index) => {
                return ControlLift::Invalid;
            }
            EvidenceState::Contradicted | EvidenceState::Unresolved => {
                underdetermined = true;
            }
            EvidenceState::Satisfied => {}
        }
    }
    if underdetermined {
        ControlLift::Underdetermined
    } else {
        ControlLift::Clear
    }
}

fn apply_control_lift(provisional: Decision, lift: ControlLift) -> Decision {
    match lift {
        ControlLift::Invalid => Decision::Invalid,
        ControlLift::Underdetermined => Decision::Underdetermined,
        ControlLift::Clear => provisional,
    }
}

fn classify_memory_suite(obligations: &[EvidenceState]) -> Decision {
    if obligations.is_empty()
        || obligations
            .iter()
            .any(|state| *state == EvidenceState::Invalid)
    {
        return Decision::Invalid;
    }
    if obligations
        .iter()
        .any(|state| *state == EvidenceState::Contradicted)
    {
        return Decision::Fail;
    }
    if obligations
        .iter()
        .all(|state| *state == EvidenceState::Satisfied)
    {
        return Decision::Pass;
    }
    Decision::Underdetermined
}

fn classify_removal_family(obligations: &[EvidenceState; 4]) -> EvidenceState {
    if obligations
        .iter()
        .any(|state| *state == EvidenceState::Invalid)
    {
        EvidenceState::Invalid
    } else if obligations
        .iter()
        .all(|state| *state == EvidenceState::Satisfied)
    {
        EvidenceState::Satisfied
    } else if obligations
        .iter()
        .any(|state| *state == EvidenceState::Contradicted)
    {
        EvidenceState::Contradicted
    } else {
        EvidenceState::Unresolved
    }
}

fn classify_memory_core(mandatory: &[EvidenceState], removals: &[EvidenceState; 3]) -> Decision {
    if mandatory.is_empty()
        || mandatory
            .iter()
            .any(|state| *state == EvidenceState::Invalid)
    {
        return Decision::Invalid;
    }
    if mandatory
        .iter()
        .any(|state| *state == EvidenceState::Contradicted)
    {
        return Decision::Fail;
    }
    if mandatory
        .iter()
        .any(|state| *state == EvidenceState::Unresolved)
    {
        return Decision::Underdetermined;
    }
    if removals
        .iter()
        .any(|state| *state == EvidenceState::Satisfied)
    {
        return Decision::Pass;
    }
    if removals
        .iter()
        .all(|state| *state == EvidenceState::Contradicted)
    {
        return Decision::Fail;
    }
    if removals
        .iter()
        .all(|state| *state == EvidenceState::Invalid)
    {
        return Decision::Invalid;
    }
    Decision::Underdetermined
}

fn union_bound(microblocks_per_edge: usize) -> f64 {
    let nontrivial_subsets = ((1_u64 << OUTCOME_CELLS) - 2) as f64;
    2.0 * EDGE_ARM_LAWS as f64
        * nontrivial_subsets
        * (-2.0 * microblocks_per_edge as f64 * EMPIRICAL_LAW_TV_RADIUS.powi(2)).exp()
}

fn minimum_microblocks_per_edge() -> usize {
    let nontrivial_subsets = ((1_u64 << OUTCOME_CELLS) - 2) as f64;
    let numerator = (2.0 * EDGE_ARM_LAWS as f64 * nontrivial_subsets / SIMULTANEOUS_ALPHA).ln();
    (numerator / (2.0 * EMPIRICAL_LAW_TV_RADIUS.powi(2))).ceil() as usize
}

fn tv(left: &[f64], right: &[f64]) -> f64 {
    0.5 * left
        .iter()
        .zip(right.iter())
        .map(|(a, b)| (a - b).abs())
        .sum::<f64>()
}

fn success_index(s: usize, m: usize, trace: usize) -> usize {
    ((2 * s + m) * 2) + trace
}

fn success_law(s_one: f64, m_one: f64, trace: usize) -> Law {
    let mut law = [0.0; OUTCOME_CELLS];
    for s in 0..=1 {
        for m in 0..=1 {
            let ps = if s == 1 { s_one } else { 1.0 - s_one };
            let pm = if m == 1 { m_one } else { 1.0 - m_one };
            law[success_index(s, m, trace)] += ps * pm;
        }
    }
    law
}

fn mixture(left: &Law, right: &Law, weight_left: f64) -> Law {
    let mut law = [0.0; OUTCOME_CELLS];
    for index in 0..OUTCOME_CELLS {
        law[index] = weight_left * left[index] + (1.0 - weight_left) * right[index];
    }
    law
}

fn is_normalized(law: &Law) -> bool {
    law.iter()
        .all(|probability| probability.is_finite() && *probability >= 0.0 && *probability <= 1.0)
        && (law.iter().sum::<f64>() - 1.0).abs() < 1e-12
}

fn s_marginal(law: &Law) -> [f64; 2] {
    let mut marginal = [0.0; 2];
    for s in 0..=1 {
        for m in 0..=1 {
            for trace in 0..=1 {
                marginal[s] += law[success_index(s, m, trace)];
            }
        }
    }
    marginal
}

fn m_marginal(law: &Law) -> [f64; 2] {
    let mut marginal = [0.0; 2];
    for s in 0..=1 {
        for m in 0..=1 {
            for trace in 0..=1 {
                marginal[m] += law[success_index(s, m, trace)];
            }
        }
    }
    marginal
}

fn sm_marginal(law: &Law) -> [f64; 4] {
    let mut marginal = [0.0; 4];
    for s in 0..=1 {
        for m in 0..=1 {
            for trace in 0..=1 {
                marginal[2 * s + m] += law[success_index(s, m, trace)];
            }
        }
    }
    marginal
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum ParentKind {
    B0Pass,
    B0Fail,
    B1Pass,
    B1Fail,
    MemoryPass,
    MemoryFail,
}

const PARENTS: [ParentKind; 6] = [
    ParentKind::B0Pass,
    ParentKind::B0Fail,
    ParentKind::B1Pass,
    ParentKind::B1Fail,
    ParentKind::MemoryPass,
    ParentKind::MemoryFail,
];

#[derive(Clone, Copy, Debug)]
enum CellSpec {
    B0Validation {
        history: usize,
        preparation: usize,
        reader: usize,
    },
    B1Validation {
        history: usize,
        reader_s: usize,
        reader_m: usize,
    },
    B0Natural {
        history: usize,
        preparation: usize,
        policy: usize,
    },
    MemoryExtra {
        history: usize,
        operation: usize,
        policy: usize,
    },
    B1Natural {
        history: usize,
        policy: usize,
    },
    Control {
        control: usize,
        arm: usize,
    },
}

fn all_cell_specs() -> Vec<CellSpec> {
    let mut cells = Vec::new();
    for history in 0..2 {
        for preparation in 0..4 {
            for reader in 0..3 {
                cells.push(CellSpec::B0Validation {
                    history,
                    preparation,
                    reader,
                });
            }
        }
    }
    for history in 0..4 {
        for reader_s in 0..3 {
            for reader_m in 0..3 {
                cells.push(CellSpec::B1Validation {
                    history,
                    reader_s,
                    reader_m,
                });
            }
        }
    }
    for history in 0..2 {
        for preparation in 0..4 {
            for policy in 0..3 {
                cells.push(CellSpec::B0Natural {
                    history,
                    preparation,
                    policy,
                });
            }
        }
    }
    for history in 0..2 {
        for operation in 0..6 {
            for policy in 0..3 {
                cells.push(CellSpec::MemoryExtra {
                    history,
                    operation,
                    policy,
                });
            }
        }
    }
    for history in 0..4 {
        for policy in 0..3 {
            cells.push(CellSpec::B1Natural { history, policy });
        }
    }
    for control in 0..CONTROL_COUNT {
        for arm in 0..2 {
            cells.push(CellSpec::Control { control, arm });
        }
    }
    cells
}

fn stabilizer_one_probability(preparation: usize, reader: usize) -> f64 {
    match (preparation, reader) {
        (0, 2) | (2, 0) | (3, 1) => 0.0,
        (1, 2) => 1.0,
        _ => 0.5,
    }
}

fn z_zero_reader_probability(reader: usize) -> f64 {
    if reader == 2 {
        0.0
    } else {
        0.5
    }
}

fn b0_natural_law(parent: ParentKind, history: usize, preparation: usize, policy: usize) -> Law {
    match parent {
        ParentKind::B0Pass => {
            // The old M value is unitarily exported to inaccessible R; the
            // registered M output is common and no future consults R.
            success_law(stabilizer_one_probability(preparation, 2), 0.0, 0)
        }
        ParentKind::B0Fail | ParentKind::MemoryPass => {
            let s = if policy == 2 { 0.0 } else { history as f64 };
            success_law(s, history as f64, 0)
        }
        ParentKind::B1Pass | ParentKind::B1Fail => success_law(
            stabilizer_one_probability(preparation, 2),
            history as f64,
            0,
        ),
        ParentKind::MemoryFail => success_law(0.0, 0.0, 0),
    }
}

fn memory_extra_law(parent: ParentKind, history: usize, operation: usize, policy: usize) -> Law {
    if parent == ParentKind::MemoryFail {
        return success_law(0.0, 0.0, 0);
    }
    let coupled = matches!(parent, ParentKind::MemoryPass | ParentKind::B0Fail);
    let sensitive = policy != 2 && coupled;
    match operation {
        // M-READ: QND in the ideal parent.
        0 => {
            let s = if sensitive { history as f64 } else { 0.0 };
            success_law(s, history as f64, 0)
        }
        // M-X.
        1 => {
            let m = 1 - history;
            let s = if sensitive { m as f64 } else { 0.0 };
            success_law(s, m as f64, 0)
        }
        // M-RAND-U: seed retained; histories induce the same S marginal.
        2 => {
            let left = success_law(0.0, 0.0, 1);
            let right = success_law(if sensitive { 1.0 } else { 0.0 }, 1.0, 1);
            mixture(&left, &right, 0.5)
        }
        // M-RESET: old value transferred to R, never cloned.
        3 => success_law(0.0, 0.0, 1),
        // M-ISO: M remains readable but cannot affect S.
        4 => success_law(0.0, history as f64, 0),
        // M-RESET-ISO.
        5 => success_law(0.0, 0.0, 1),
        _ => [0.0; OUTCOME_CELLS],
    }
}

fn control_law(control: usize, arm: usize) -> Law {
    match control {
        0 | 2 | 5 | 7 => success_law(0.0, 0.0, 0),
        1 | 3 | 6 => success_law(arm as f64, 0.0, 0),
        4 => success_law(0.0, arm as f64, 0),
        _ => [0.0; OUTCOME_CELLS],
    }
}

fn parent_law(parent: ParentKind, cell: CellSpec) -> Law {
    match cell {
        CellSpec::B0Validation {
            history,
            preparation,
            reader,
        } => success_law(
            stabilizer_one_probability(preparation, reader),
            if parent == ParentKind::MemoryFail {
                0.0
            } else {
                history as f64
            },
            0,
        ),
        CellSpec::B1Validation {
            history,
            reader_s,
            reader_m,
        } => {
            let trace = usize::from(parent == ParentKind::B1Fail && history == 3);
            success_law(
                z_zero_reader_probability(reader_s),
                z_zero_reader_probability(reader_m),
                trace,
            )
        }
        CellSpec::B0Natural {
            history,
            preparation,
            policy,
        } => b0_natural_law(parent, history, preparation, policy),
        CellSpec::MemoryExtra {
            history,
            operation,
            policy,
        } => memory_extra_law(parent, history, operation, policy),
        CellSpec::B1Natural { history, policy } => {
            if parent == ParentKind::B1Fail && history == 3 && policy != 2 {
                success_law(1.0, 0.0, 1)
            } else {
                success_law(0.0, 0.0, 0)
            }
        }
        CellSpec::Control { control, arm } => control_law(control, arm),
    }
}

fn verify_common_opportunity_identity() -> Result<usize, String> {
    let mut cases = 0_usize;
    // Four binary potential outcomes: arm 0/1 at slot 0/1.
    for mask in 0_u8..16 {
        let potential = [
            [f64::from(mask & 1), f64::from((mask >> 1) & 1)],
            [f64::from((mask >> 2) & 1), f64::from((mask >> 3) & 1)],
        ];
        for arm in 0..2 {
            let target = 0.5 * (potential[arm][0] + potential[arm][1]);
            let order_zero = potential[arm][arm];
            let order_one = potential[arm][1 - arm];
            let randomized_expectation = 0.5 * (order_zero + order_one);
            if (target - randomized_expectation).abs() > 1e-15 {
                return Err("paired order randomization misses common target".into());
            }
        }
        cases += 1;
    }

    // Hostile drift control: no treatment effect, but slot 0 always outputs 0
    // and slot 1 always outputs 1. Fixed order creates a spurious difference;
    // randomized common-opportunity targets agree at 1/2.
    let fixed_order_difference = (0.0_f64 - 1.0_f64).abs();
    let randomized_arm_zero: f64 = 0.5 * (0.0 + 1.0);
    let randomized_arm_one: f64 = 0.5 * (0.0 + 1.0);
    if fixed_order_difference != 1.0 || (randomized_arm_zero - randomized_arm_one).abs() > 1e-15 {
        return Err("drift counterexample or paired repair is malformed".into());
    }
    Ok(cases)
}

fn verify_power_contract() -> Result<(), String> {
    if (2.0 * EMPIRICAL_LAW_TV_RADIUS - DISTANCE_CI_RADIUS).abs() > 1e-15 {
        return Err("distance radius is not twice the arm-law radius".into());
    }
    if (POWER_LOW + 2.0 * DISTANCE_CI_RADIUS - SCREEN_PASS_THRESHOLD).abs() > 1e-15 {
        return Err("pass power margin is inconsistent".into());
    }
    if (POWER_HIGH - 2.0 * DISTANCE_CI_RADIUS - SCREEN_FAIL_THRESHOLD).abs() > 1e-15 {
        return Err("fail power margin is inconsistent".into());
    }
    if (TRACE_POWER_LOW + 2.0 * EMPIRICAL_LAW_TV_RADIUS - TRACE_PASS_THRESHOLD).abs() > 1e-15 {
        return Err("trace-veto power margin is inconsistent".into());
    }
    let minimum = minimum_microblocks_per_edge();
    if minimum != 104_174 {
        return Err(format!("unexpected minimum microblock count {minimum}"));
    }
    if CHOSEN_MICROBLOCKS_PER_EDGE % MACROBLOCKS != 0
        || CHOSEN_MICROBLOCKS_PER_EDGE < minimum
        || CHOSEN_MICROBLOCKS_PER_EDGE - MACROBLOCKS >= minimum
    {
        return Err("chosen microblock count is not the smallest block multiple".into());
    }
    let bound = union_bound(CHOSEN_MICROBLOCKS_PER_EDGE);
    if bound > SIMULTANEOUS_ALPHA || bound > TARGET_BETA {
        return Err(format!("simultaneous bound {bound} exceeds target"));
    }
    Ok(())
}

fn verify_reader_aggregation() -> Result<(), String> {
    let aggregate = aggregate_max_interval(&[
        Interval::closed(0.00, 0.04),
        Interval::closed(0.02, 0.08),
        Interval::closed(0.01, 0.06),
    ])
    .map_err(str::to_owned)?;
    if (aggregate.lower - 0.02).abs() > 1e-15 || (aggregate.upper - 0.08).abs() > 1e-15 {
        return Err("max-reader interval aggregation is incorrect".into());
    }
    if aggregate_max_interval(&[]).is_ok()
        || aggregate_max_interval(&[Interval::empty()]).is_ok()
        || aggregate_max_interval(&[Interval::closed(0.8, 0.2)]).is_ok()
    {
        return Err("invalid reader family escaped aggregation".into());
    }
    Ok(())
}

fn decode_evidence(mut code: usize) -> [EvidenceState; CONTROL_COUNT] {
    let states = [
        EvidenceState::Invalid,
        EvidenceState::Satisfied,
        EvidenceState::Contradicted,
        EvidenceState::Unresolved,
    ];
    let mut controls = [EvidenceState::Invalid; CONTROL_COUNT];
    for control in &mut controls {
        *control = states[code % 4];
        code /= 4;
    }
    controls
}

fn verify_control_routes() -> Result<usize, String> {
    let mut cases = 0_usize;
    for code in 0..4_usize.pow(CONTROL_COUNT as u32) {
        let controls = decode_evidence(code);
        for coordinate in [Coordinate::Memory, Coordinate::B0, Coordinate::B1] {
            let lift = classify_control_lift(coordinate, &controls);
            let result = apply_control_lift(Decision::Pass, lift);
            match lift {
                ControlLift::Invalid if result != Decision::Invalid => {
                    return Err("invalid control lift escaped INVALID".into());
                }
                ControlLift::Underdetermined if result != Decision::Underdetermined => {
                    return Err("unresolved control lift escaped UNDERDETERMINED".into());
                }
                ControlLift::Clear if result != Decision::Pass => {
                    return Err("clear control changed provisional decision".into());
                }
                _ => {}
            }
            cases += 1;
        }
    }

    let satisfied = [EvidenceState::Satisfied; CONTROL_COUNT];
    if classify_control_lift(Coordinate::B0, &satisfied) != ControlLift::Clear {
        return Err("all-satisfied B0 controls are not clear".into());
    }
    let mut b0_null_failure = satisfied;
    b0_null_failure[0] = EvidenceState::Contradicted;
    if classify_control_lift(Coordinate::B0, &b0_null_failure) != ControlLift::Invalid {
        return Err("B0 known-null contradiction did not invalidate B0".into());
    }
    if classify_control_lift(Coordinate::B1, &b0_null_failure) != ControlLift::Clear {
        return Err("B0-only control contaminated B1".into());
    }
    let mut sentinel_failure = satisfied;
    sentinel_failure[6] = EvidenceState::Contradicted;
    for coordinate in [Coordinate::Memory, Coordinate::B0, Coordinate::B1] {
        if classify_control_lift(coordinate, &sentinel_failure) != ControlLift::Underdetermined {
            return Err("sentinel sensitivity failure did not withhold coordinate".into());
        }
    }
    Ok(cases)
}

fn verify_memory_split() -> Result<(), String> {
    let mandatory = [EvidenceState::Satisfied; 8];
    let removals = [
        EvidenceState::Satisfied,
        EvidenceState::Invalid,
        EvidenceState::Contradicted,
    ];
    if classify_memory_core(&mandatory, &removals) != Decision::Pass {
        return Err("one satisfied removal family did not witness core memory".into());
    }

    let mut suite = [EvidenceState::Satisfied; 24];
    suite[8] = EvidenceState::Contradicted;
    if classify_memory_suite(&suite) != Decision::Fail
        || classify_memory_core(&mandatory, &removals) != Decision::Pass
    {
        return Err("core memory and instrument suite were not separated".into());
    }

    let family = classify_removal_family(&[
        EvidenceState::Satisfied,
        EvidenceState::Satisfied,
        EvidenceState::Satisfied,
        EvidenceState::Satisfied,
    ]);
    if family != EvidenceState::Satisfied {
        return Err("complete removal family did not pass".into());
    }
    let failed_removals = [EvidenceState::Contradicted; 3];
    if classify_memory_core(&mandatory, &failed_removals) != Decision::Fail {
        return Err("three contradicted removal routes did not fail core memory".into());
    }
    let invalid_removals = [EvidenceState::Invalid; 3];
    if classify_memory_core(&mandatory, &invalid_removals) != Decision::Invalid {
        return Err("three invalid removal routes did not invalidate core memory".into());
    }
    Ok(())
}

fn verify_trace_and_thresholds() -> Result<(), String> {
    let clean = Interval::closed(0.0, TRACE_PASS_THRESHOLD);
    let dirty = Interval::closed(0.075, 0.10);
    if classify_trace_interval(true, clean) != TraceState::Clean
        || classify_trace_interval(true, dirty) != TraceState::Contaminated
        || classify_trace_interval(true, Interval::empty()) != TraceState::Invalid
    {
        return Err("trace interval map is incorrect".into());
    }

    let refined_pass_ceiling = SCREEN_PASS_THRESHOLD + TRACE_PASS_THRESHOLD;
    if (refined_pass_ceiling - 0.15).abs() > 1e-15 {
        return Err("refined trace ceiling is not 0.15".into());
    }
    let meanings = [
        (POWER_LOW, 0.525),
        (SCREEN_PASS_THRESHOLD, 0.55),
        (SCREEN_FAIL_THRESHOLD, 0.625),
        (POWER_HIGH, 0.65),
        (refined_pass_ceiling, 0.575),
    ];
    for (distance, expected_guess) in meanings {
        let guess = 0.5 * (1.0 + distance);
        if (guess - expected_guess).abs() > 1e-15 {
            return Err("TV-to-guessing interpretation is incorrect".into());
        }
    }

    let mismatch = [Interval::closed(0.0, 0.05)];
    let screen_pass = Interval::closed(0.0, 0.05);
    let screen_fail = Interval::closed(0.30, 0.40);
    if classify_boundary_row(true, false, &mismatch, screen_pass, clean, clean)
        != BoundaryRowState::MatchedPass
    {
        return Err("clean trace veto blocked a valid matched pass".into());
    }
    if classify_boundary_row(true, false, &mismatch, screen_pass, dirty, clean)
        != BoundaryRowState::MatchedUnresolved
    {
        return Err("dirty trace was promoted to boundary pass".into());
    }
    if classify_boundary_row(true, false, &mismatch, screen_fail, dirty, dirty)
        != BoundaryRowState::MatchedFail
    {
        return Err("coarse matched failure was erased by trace contamination".into());
    }
    Ok(())
}

fn verify_trace_refinement_bound() -> Result<usize, String> {
    // One injective G=0 cell and two fine trace identities collapsed to G=1.
    // The quarter-grid is not the proof (Section 6.2 supplies it), but it is an
    // executable mutant surface for the exact inequality used by the design.
    let mut fine_laws = Vec::new();
    for nominal_quarters in 0..=4 {
        for trace_a_quarters in 0..=(4 - nominal_quarters) {
            let trace_b_quarters = 4 - nominal_quarters - trace_a_quarters;
            fine_laws.push([
                nominal_quarters as f64 / 4.0,
                trace_a_quarters as f64 / 4.0,
                trace_b_quarters as f64 / 4.0,
            ]);
        }
    }
    let mut cases = 0_usize;
    for left in &fine_laws {
        for right in &fine_laws {
            let coarse_left = [left[0], left[1] + left[2]];
            let coarse_right = [right[0], right[1] + right[2]];
            let fine_distance = tv(left, right);
            let coarse_distance = tv(&coarse_left, &coarse_right);
            let hidden_trace_ceiling = (left[1] + left[2]).min(right[1] + right[2]);
            if fine_distance > coarse_distance + hidden_trace_ceiling + 1e-15 {
                return Err("trace refinement exceeds the printed ceiling".into());
            }
            if coarse_distance > fine_distance + 1e-15 {
                return Err("coarse graining increased total variation".into());
            }
            cases += 1;
        }
    }
    if cases != 225 {
        return Err(format!("trace refinement grid has {cases} cases"));
    }
    Ok(cases)
}

fn verify_parent_models() -> Result<usize, String> {
    let cells = all_cell_specs();
    if cells.len() != UNIQUE_CELL_TYPES {
        return Err(format!(
            "unique cell-type count {} != {UNIQUE_CELL_TYPES}",
            cells.len()
        ));
    }
    let mut generated = 0_usize;
    for parent in PARENTS {
        for cell in &cells {
            let law = parent_law(parent, *cell);
            if !is_normalized(&law) {
                return Err(format!("parent {parent:?} generated a malformed law"));
            }
            generated += 1;
        }
    }

    // B0 pass and fail parents share exactly matched S readers.
    for parent in [ParentKind::B0Pass, ParentKind::B0Fail] {
        for preparation in 0..4 {
            for reader in 0..3 {
                let left = parent_law(
                    parent,
                    CellSpec::B0Validation {
                        history: 0,
                        preparation,
                        reader,
                    },
                );
                let right = parent_law(
                    parent,
                    CellSpec::B0Validation {
                        history: 1,
                        preparation,
                        reader,
                    },
                );
                if tv(&s_marginal(&left), &s_marginal(&right)) > POWER_LOW {
                    return Err("B0 parent failed its matched-S boundary".into());
                }
            }
        }
    }
    for policy in 0..3 {
        let pass_left = parent_law(
            ParentKind::B0Pass,
            CellSpec::B0Natural {
                history: 0,
                preparation: 0,
                policy,
            },
        );
        let pass_right = parent_law(
            ParentKind::B0Pass,
            CellSpec::B0Natural {
                history: 1,
                preparation: 0,
                policy,
            },
        );
        if tv(&pass_left, &pass_right) > POWER_LOW {
            return Err("B0 pass parent does not screen complete registered future".into());
        }
    }
    let b0_fail_left = parent_law(
        ParentKind::B0Fail,
        CellSpec::B0Natural {
            history: 0,
            preparation: 0,
            policy: 0,
        },
    );
    let b0_fail_right = parent_law(
        ParentKind::B0Fail,
        CellSpec::B0Natural {
            history: 1,
            preparation: 0,
            policy: 0,
        },
    );
    if tv(&b0_fail_left, &b0_fail_right) < POWER_HIGH {
        return Err("B0 fail parent lacks residual future dependence".into());
    }

    // B1 parents match all local-Pauli product reader laws at the SM projection.
    for parent in [ParentKind::B1Pass, ParentKind::B1Fail] {
        for reader_s in 0..3 {
            for reader_m in 0..3 {
                let c0 = parent_law(
                    parent,
                    CellSpec::B1Validation {
                        history: 2,
                        reader_s,
                        reader_m,
                    },
                );
                let c1 = parent_law(
                    parent,
                    CellSpec::B1Validation {
                        history: 3,
                        reader_s,
                        reader_m,
                    },
                );
                if tv(&sm_marginal(&c0), &sm_marginal(&c1)) > POWER_LOW {
                    return Err("B1 parent failed its matched SM boundary".into());
                }
            }
        }
    }
    for history_pair in [(0, 1), (2, 3)] {
        for policy in 0..3 {
            let left = parent_law(
                ParentKind::B1Pass,
                CellSpec::B1Natural {
                    history: history_pair.0,
                    policy,
                },
            );
            let right = parent_law(
                ParentKind::B1Pass,
                CellSpec::B1Natural {
                    history: history_pair.1,
                    policy,
                },
            );
            if tv(&left, &right) > POWER_LOW {
                return Err("B1 pass parent does not screen its history pair".into());
            }
        }
    }
    let b1_fail_left = parent_law(
        ParentKind::B1Fail,
        CellSpec::B1Natural {
            history: 2,
            policy: 0,
        },
    );
    let b1_fail_right = parent_law(
        ParentKind::B1Fail,
        CellSpec::B1Natural {
            history: 3,
            policy: 0,
        },
    );
    if tv(&b1_fail_left, &b1_fail_right) < POWER_HIGH {
        return Err("B1 fail parent lacks exterior-history response".into());
    }

    // Memory-pass parent: readable M, exchange/held-out phase transfer,
    // null policy, toggle, and all three qualifying removal routes.
    let read_zero = parent_law(
        ParentKind::MemoryPass,
        CellSpec::B0Validation {
            history: 0,
            preparation: 0,
            reader: 2,
        },
    );
    let read_one = parent_law(
        ParentKind::MemoryPass,
        CellSpec::B0Validation {
            history: 1,
            preparation: 0,
            reader: 2,
        },
    );
    if tv(&m_marginal(&read_zero), &m_marginal(&read_one)) < POWER_HIGH {
        return Err("memory-pass parent lacks readable memory".into());
    }
    for policy in 0..3 {
        let id_zero = parent_law(
            ParentKind::MemoryPass,
            CellSpec::B0Natural {
                history: 0,
                preparation: 0,
                policy,
            },
        );
        let id_one = parent_law(
            ParentKind::MemoryPass,
            CellSpec::B0Natural {
                history: 1,
                preparation: 0,
                policy,
            },
        );
        let distance = tv(&s_marginal(&id_zero), &s_marginal(&id_one));
        if (policy == 2 && distance > POWER_LOW) || (policy != 2 && distance < POWER_HIGH) {
            return Err("memory-pass baseline policy pattern is wrong".into());
        }
    }
    for history in 0..2 {
        for policy in 0..2 {
            let id = parent_law(
                ParentKind::MemoryPass,
                CellSpec::B0Natural {
                    history,
                    preparation: 0,
                    policy,
                },
            );
            let toggled = parent_law(
                ParentKind::MemoryPass,
                CellSpec::MemoryExtra {
                    history,
                    operation: 1,
                    policy,
                },
            );
            if tv(&s_marginal(&id), &s_marginal(&toggled)) < POWER_HIGH {
                return Err("memory-pass toggle is not causal".into());
            }
        }
    }
    for operation in [2, 3, 4] {
        for policy in 0..2 {
            let removed_zero = parent_law(
                ParentKind::MemoryPass,
                CellSpec::MemoryExtra {
                    history: 0,
                    operation,
                    policy,
                },
            );
            let removed_one = parent_law(
                ParentKind::MemoryPass,
                CellSpec::MemoryExtra {
                    history: 1,
                    operation,
                    policy,
                },
            );
            if tv(&s_marginal(&removed_zero), &s_marginal(&removed_one)) > POWER_LOW {
                return Err("memory removal leaves a history-to-S effect".into());
            }
            let id_one = parent_law(
                ParentKind::MemoryPass,
                CellSpec::B0Natural {
                    history: 1,
                    preparation: 0,
                    policy,
                },
            );
            if tv(&s_marginal(&id_one), &s_marginal(&removed_one)) < POWER_HIGH {
                return Err("memory removal does not differ from ID at H-M1".into());
            }
        }
    }
    let fail_read_zero = parent_law(
        ParentKind::MemoryFail,
        CellSpec::B0Validation {
            history: 0,
            preparation: 0,
            reader: 2,
        },
    );
    let fail_read_one = parent_law(
        ParentKind::MemoryFail,
        CellSpec::B0Validation {
            history: 1,
            preparation: 0,
            reader: 2,
        },
    );
    if tv(&m_marginal(&fail_read_zero), &m_marginal(&fail_read_one)) > POWER_LOW {
        return Err("memory-fail parent unexpectedly writes M".into());
    }

    // Every paired control has its frozen direction in every parent.
    for control in 0..CONTROL_COUNT {
        let left = control_law(control, 0);
        let right = control_law(control, 1);
        let distance = tv(&left, &right);
        if control_is_validity_null(control) {
            if distance > POWER_LOW {
                return Err("known-null control parent is not null".into());
            }
        } else if distance < POWER_HIGH {
            return Err("sensitivity control parent lacks separation".into());
        }
    }
    Ok(generated)
}

fn verify_legacy_firewalls() -> Result<(), String> {
    let clean = Interval::closed(0.0, 0.025);
    let pass_mismatch = [Interval::closed(0.0, 0.05)];
    let mismatched = [Interval::closed(0.30, 0.40)];
    let pass_screen = Interval::closed(0.0, 0.05);
    let fail_screen = Interval::closed(0.30, 0.40);

    if classify_boundary_row(true, true, &pass_mismatch, pass_screen, clean, clean)
        != BoundaryRowState::ForcedRestart
    {
        return Err("full-boundary restart entered natural sufficiency".into());
    }
    let mismatch_row = classify_boundary_row(true, false, &mismatched, fail_screen, clean, clean);
    if mismatch_row != BoundaryRowState::BoundaryMismatch
        || classify_boundary(&[mismatch_row]) == Decision::Fail
    {
        return Err("boundary mismatch was promoted to FAIL".into());
    }
    if classify_boundary_row(true, false, &[Interval::empty()], pass_screen, clean, clean)
        != BoundaryRowState::Invalid
    {
        return Err("empty reader confidence set escaped INVALID".into());
    }
    if classify_effect_interval(
        true,
        EffectDirection::MustBePresent,
        Interval::closed(0.30, 0.40),
    ) != EvidenceState::Satisfied
        || classify_effect_interval(
            true,
            EffectDirection::MustBeAbsent,
            Interval::closed(0.0, 0.05),
        ) != EvidenceState::Satisfied
    {
        return Err("effect directions are not executable".into());
    }
    Ok(())
}

fn run_all_checks() -> Result<(), String> {
    verify_common_opportunity_identity()?;
    verify_power_contract()?;
    verify_reader_aggregation()?;
    verify_control_routes()?;
    verify_memory_split()?;
    verify_trace_and_thresholds()?;
    verify_trace_refinement_bound()?;
    verify_parent_models()?;
    verify_legacy_firewalls()?;
    Ok(())
}

fn main() {
    if let Err(error) = run_all_checks() {
        eprintln!("PTS0-DIFFERENTIAL-CHECK: FAIL: {error}");
        std::process::exit(1);
    }
    let common_cases = verify_common_opportunity_identity().expect("checked above");
    let control_cases = verify_control_routes().expect("checked above");
    let generated_parent_laws = verify_parent_models().expect("checked above");
    let trace_refinement_cases = verify_trace_refinement_bound().expect("checked above");
    let minimum = minimum_microblocks_per_edge();
    let bound = union_bound(CHOSEN_MICROBLOCKS_PER_EDGE);

    println!("PTS0-DIFFERENTIAL-CHECK: PASS");
    println!("unique_cell_types={UNIQUE_CELL_TYPES}");
    println!("registered_edges={REGISTERED_EDGES}");
    println!("edge_arm_laws={EDGE_ARM_LAWS}");
    println!("common_opportunity_binary_cases={common_cases}");
    println!("minimum_microblocks_per_edge={minimum}");
    println!("chosen_microblocks_per_edge={CHOSEN_MICROBLOCKS_PER_EDGE}");
    println!(
        "total_issued_attempts={}",
        2 * REGISTERED_EDGES * CHOSEN_MICROBLOCKS_PER_EDGE
    );
    println!("simultaneous_error_bound={bound:.15}");
    println!("distance_ci_radius={DISTANCE_CI_RADIUS:.6}");
    println!("control_route_cases={control_cases}");
    println!("finite_parent_models={}", PARENTS.len());
    println!("generated_parent_cell_laws={generated_parent_laws}");
    println!("reader_aggregation=MAX_INTERVAL_EXECUTABLE");
    println!("trace_projection=VETO_WITH_REFINED_TV_CEILING_0.15");
    println!("trace_refinement_grid_pairs={trace_refinement_cases}");
    println!("memory_output=CORE_COORDINATE_PLUS_SUITE_DIAGNOSTIC");
    println!("assignment_randomness=INCLUDED");
    println!("predictable_drift=COMMON_OPPORTUNITY_AVERAGED");
    println!("authority=AUTHOR_SIDE_QA_ONLY");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn complete_differential_checker_passes() {
        run_all_checks().unwrap();
    }

    #[test]
    fn paired_randomization_removes_slot_drift_bias_in_target() {
        assert_eq!(verify_common_opportunity_identity().unwrap(), 16);
    }

    #[test]
    fn reader_max_interval_and_empty_route_are_exact() {
        verify_reader_aggregation().unwrap();
    }

    #[test]
    fn every_control_vector_has_a_total_coordinate_route() {
        assert_eq!(verify_control_routes().unwrap(), 196_608);
    }

    #[test]
    fn core_memory_can_pass_while_instrument_suite_fails() {
        verify_memory_split().unwrap();
    }

    #[test]
    fn trace_veto_blocks_coarse_false_pass() {
        verify_trace_and_thresholds().unwrap();
        assert_eq!(verify_trace_refinement_bound().unwrap(), 225);
    }

    #[test]
    fn six_parents_generate_all_registered_cell_types() {
        assert_eq!(verify_parent_models().unwrap(), 6 * UNIQUE_CELL_TYPES);
    }

    #[test]
    fn mismatch_restart_and_empty_set_still_fail_closed() {
        verify_legacy_firewalls().unwrap();
    }
}
