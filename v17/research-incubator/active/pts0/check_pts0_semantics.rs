//! Executable reference semantics for the author-side PTS-0 design.
//!
//! This program is quality assurance, not physical evidence.  It checks the
//! finite routing law, the design cardinalities, the distribution-free sample
//! bound, and explicit mathematical witnesses for both decision regions.

use std::fmt;

const OUTCOME_CELLS: usize = 32;
const CELL_LAWS: usize = 148;
const ACQUISITION_BLOCKS: usize = 32;
const SIMULTANEOUS_ALPHA: f64 = 0.01;

// For each assigned cell law, empirical TV from its randomized-schedule
// conditional-mean law is controlled at this radius.  A distance between two
// cell laws therefore has radius 2 * EMPIRICAL_LAW_TV_RADIUS.
const EMPIRICAL_LAW_TV_RADIUS: f64 = 0.0125;
const DISTANCE_CI_RADIUS: f64 = 0.025;

const MATCH_THRESHOLD: f64 = 0.10;
const SCREEN_PASS_THRESHOLD: f64 = 0.10;
const SCREEN_FAIL_THRESHOLD: f64 = 0.25;

// Interior power regions.  The 0.05 separation from the decision boundaries
// is exactly twice the distance-CI radius.
const POWER_LOW: f64 = 0.05;
const POWER_HIGH: f64 = 0.30;
const TARGET_BETA: f64 = 0.01;

const CHOSEN_ATTEMPTS_PER_CELL: usize = 103_936;

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
enum ObligationState {
    Invalid,
    Satisfied,
    Contradicted,
    Unresolved,
}

fn valid_interval(lower: f64, upper: f64) -> bool {
    lower.is_finite()
        && upper.is_finite()
        && 0.0 <= lower
        && lower <= upper
        && upper <= 1.0
}

fn classify_boundary_row(
    procedural_valid: bool,
    confidence_nonempty: bool,
    full_boundary_forced_restart: bool,
    mismatch_lower: f64,
    mismatch_upper: f64,
    screen_lower: f64,
    screen_upper: f64,
) -> BoundaryRowState {
    if !procedural_valid || !confidence_nonempty {
        return BoundaryRowState::Invalid;
    }
    if full_boundary_forced_restart {
        return BoundaryRowState::ForcedRestart;
    }
    if !valid_interval(mismatch_lower, mismatch_upper)
        || !valid_interval(screen_lower, screen_upper)
    {
        return BoundaryRowState::Invalid;
    }

    if mismatch_upper <= MATCH_THRESHOLD {
        if screen_upper <= SCREEN_PASS_THRESHOLD {
            BoundaryRowState::MatchedPass
        } else if screen_lower >= SCREEN_FAIL_THRESHOLD {
            BoundaryRowState::MatchedFail
        } else {
            BoundaryRowState::MatchedUnresolved
        }
    } else if mismatch_lower > MATCH_THRESHOLD {
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

fn classify_effect_interval(
    procedural_valid: bool,
    confidence_nonempty: bool,
    direction: EffectDirection,
    lower: f64,
    upper: f64,
) -> ObligationState {
    if !procedural_valid || !confidence_nonempty || !valid_interval(lower, upper) {
        return ObligationState::Invalid;
    }
    match direction {
        EffectDirection::MustBePresent => {
            if lower >= SCREEN_FAIL_THRESHOLD {
                ObligationState::Satisfied
            } else if upper <= SCREEN_PASS_THRESHOLD {
                ObligationState::Contradicted
            } else {
                ObligationState::Unresolved
            }
        }
        EffectDirection::MustBeAbsent => {
            if upper <= SCREEN_PASS_THRESHOLD {
                ObligationState::Satisfied
            } else if lower >= SCREEN_FAIL_THRESHOLD {
                ObligationState::Contradicted
            } else {
                ObligationState::Unresolved
            }
        }
    }
}

fn classify_memory_descent(obligations: &[ObligationState]) -> Decision {
    if obligations.is_empty()
        || obligations
            .iter()
            .any(|state| *state == ObligationState::Invalid)
    {
        return Decision::Invalid;
    }
    if obligations
        .iter()
        .any(|state| *state == ObligationState::Contradicted)
    {
        return Decision::Fail;
    }
    if obligations
        .iter()
        .all(|state| *state == ObligationState::Satisfied)
    {
        return Decision::Pass;
    }
    Decision::Underdetermined
}

fn design_counts() -> (usize, usize) {
    // Validation copies:
    // B0: 2 memory histories * 4 system preparations * 3 Pauli readers.
    // B1: 4 histories in 2 matched pairs * 9 local-Pauli product readers.
    let validation_laws = 2 * 4 * 3 + 4 * 9;

    // Scored continuations:
    // B0 natural ID rows over all system preparations and future policies;
    // six additional memory operations at one anchor S preparation;
    // B1 natural ID rows for four histories and three future policies.
    let scored_laws = 2 * 4 * 3 + 2 * 6 * 3 + 4 * 3;

    // Eight physically typed paired controls cover schedule drift, reader
    // anchors, randomizer leakage, and pass/fail sensitivity.
    let control_laws = 16;

    let matching_distances = 4 * 3 + 2 * 9;
    let screening_distances = 4 * 3 + 2 * 3;
    let memory_distances = 24;
    let drift_and_anchor_distances = 8;

    (
        validation_laws + scored_laws + control_laws,
        matching_distances
            + screening_distances
            + memory_distances
            + drift_and_anchor_distances,
    )
}

fn union_bound(n: usize) -> f64 {
    let nontrivial_subsets = ((1_u64 << OUTCOME_CELLS) - 2) as f64;
    2.0 * CELL_LAWS as f64
        * nontrivial_subsets
        * (-2.0 * n as f64 * EMPIRICAL_LAW_TV_RADIUS.powi(2)).exp()
}

fn minimum_attempts_per_cell() -> usize {
    let nontrivial_subsets = ((1_u64 << OUTCOME_CELLS) - 2) as f64;
    let numerator =
        (2.0 * CELL_LAWS as f64 * nontrivial_subsets / SIMULTANEOUS_ALPHA).ln();
    (numerator / (2.0 * EMPIRICAL_LAW_TV_RADIUS.powi(2))).ceil() as usize
}

fn tv(p: &[f64; OUTCOME_CELLS], q: &[f64; OUTCOME_CELLS]) -> f64 {
    0.5 * p
        .iter()
        .zip(q.iter())
        .map(|(left, right)| (left - right).abs())
        .sum::<f64>()
}

fn point_mass(cell: usize) -> [f64; OUTCOME_CELLS] {
    let mut law = [0.0; OUTCOME_CELLS];
    law[cell] = 1.0;
    law
}

fn verify_design_counts() -> Result<(), String> {
    let (laws, distances) = design_counts();
    if laws != CELL_LAWS {
        return Err(format!("cell-law count {laws} != {CELL_LAWS}"));
    }
    if distances != 80 {
        return Err(format!("distance count {distances} != 80"));
    }
    Ok(())
}

fn verify_power_contract() -> Result<(), String> {
    if (2.0 * EMPIRICAL_LAW_TV_RADIUS - DISTANCE_CI_RADIUS).abs() > 1e-15 {
        return Err("pair-distance radius does not equal two law radii".into());
    }
    if (POWER_LOW + 2.0 * DISTANCE_CI_RADIUS - SCREEN_PASS_THRESHOLD).abs() > 1e-15
    {
        return Err("pass-side power margin is inconsistent".into());
    }
    if (POWER_HIGH - 2.0 * DISTANCE_CI_RADIUS - SCREEN_FAIL_THRESHOLD).abs()
        > 1e-15
    {
        return Err("fail-side power margin is inconsistent".into());
    }
    if CHOSEN_ATTEMPTS_PER_CELL % ACQUISITION_BLOCKS != 0 {
        return Err("attempt count is not block divisible".into());
    }

    let minimum = minimum_attempts_per_cell();
    if CHOSEN_ATTEMPTS_PER_CELL < minimum {
        return Err(format!(
            "chosen n={} is below minimum {minimum}",
            CHOSEN_ATTEMPTS_PER_CELL
        ));
    }
    if CHOSEN_ATTEMPTS_PER_CELL - ACQUISITION_BLOCKS >= minimum {
        return Err("chosen n is not the smallest block multiple".into());
    }
    let bound = union_bound(CHOSEN_ATTEMPTS_PER_CELL);
    if bound > SIMULTANEOUS_ALPHA || bound > TARGET_BETA {
        return Err(format!("simultaneous error bound {bound} is too large"));
    }
    Ok(())
}

fn verify_witness_laws() -> Result<(), String> {
    // These mathematical laws are tied in the design packet to executable
    // two-transmon control modes.  They prove only that the full finite model's
    // pass and fail regions are nonempty.
    let same_left = point_mass(0);
    let same_right = point_mass(0);
    let separated_right = point_mass(1);
    let matched_boundary_left = point_mass(2);
    let matched_boundary_right = point_mass(2);

    if tv(&same_left, &same_right) > POWER_LOW {
        return Err("pass witness is outside the interior pass region".into());
    }
    if tv(&same_left, &separated_right) < POWER_HIGH {
        return Err("fail witness is outside the interior fail region".into());
    }
    if tv(&matched_boundary_left, &matched_boundary_right) > POWER_LOW {
        return Err("fail witness does not have a matched boundary".into());
    }
    Ok(())
}

fn verify_boundary_truth_table() -> Result<(usize, [usize; 4]), String> {
    let states = [
        BoundaryRowState::Invalid,
        BoundaryRowState::MatchedPass,
        BoundaryRowState::MatchedFail,
        BoundaryRowState::MatchedUnresolved,
        BoundaryRowState::BoundaryMismatch,
        BoundaryRowState::BoundaryMatchUnresolved,
        BoundaryRowState::ForcedRestart,
    ];
    let mut counts = [0_usize; 4];
    let mut total = 0_usize;

    for first in states {
        for second in states {
            for third in states {
                let rows = [first, second, third];
                let decision = classify_boundary(&rows);
                let index = match decision {
                    Decision::Invalid => 0,
                    Decision::Pass => 1,
                    Decision::Fail => 2,
                    Decision::Underdetermined => 3,
                };
                counts[index] += 1;
                total += 1;

                if rows.iter().any(|state| {
                    matches!(
                        state,
                        BoundaryRowState::Invalid | BoundaryRowState::ForcedRestart
                    )
                }) && decision != Decision::Invalid
                {
                    return Err("invalid/restart row escaped INVALID".into());
                }
                if decision == Decision::Fail
                    && !rows
                        .iter()
                        .any(|state| *state == BoundaryRowState::MatchedFail)
                {
                    return Err("boundary mismatch was promoted to FAIL".into());
                }
                if decision == Decision::Pass
                    && !rows
                        .iter()
                        .all(|state| *state == BoundaryRowState::MatchedPass)
                {
                    return Err("PASS occurred without all required row passes".into());
                }
            }
        }
    }
    if total != 343 || counts.iter().any(|count| *count == 0) {
        return Err("boundary truth table is incomplete".into());
    }
    Ok((total, counts))
}

fn verify_numeric_row_map() -> Result<usize, String> {
    let grid = [0.0, 0.05, 0.10, 0.15, 0.25, 0.30, 1.0];
    let mut total = 0_usize;
    for procedural_valid in [false, true] {
        for confidence_nonempty in [false, true] {
            for forced_restart in [false, true] {
                for mismatch_lower in grid {
                    for mismatch_upper in grid {
                        for screen_lower in grid {
                            for screen_upper in grid {
                                let state = classify_boundary_row(
                                    procedural_valid,
                                    confidence_nonempty,
                                    forced_restart,
                                    mismatch_lower,
                                    mismatch_upper,
                                    screen_lower,
                                    screen_upper,
                                );
                                total += 1;
                                if forced_restart
                                    && procedural_valid
                                    && confidence_nonempty
                                    && state != BoundaryRowState::ForcedRestart
                                {
                                    return Err("forced restart entered natural sufficiency".into());
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    Ok(total)
}

fn verify_memory_truth_table() -> Result<(usize, [usize; 4]), String> {
    let states = [
        ObligationState::Invalid,
        ObligationState::Satisfied,
        ObligationState::Contradicted,
        ObligationState::Unresolved,
    ];
    let mut counts = [0_usize; 4];
    let mut total = 0_usize;
    for first in states {
        for second in states {
            for third in states {
                for fourth in states {
                    let obligations = [first, second, third, fourth];
                    let decision = classify_memory_descent(&obligations);
                    let index = match decision {
                        Decision::Invalid => 0,
                        Decision::Pass => 1,
                        Decision::Fail => 2,
                        Decision::Underdetermined => 3,
                    };
                    counts[index] += 1;
                    total += 1;
                    if obligations
                        .iter()
                        .any(|state| *state == ObligationState::Invalid)
                        && decision != Decision::Invalid
                    {
                        return Err("invalid memory obligation escaped INVALID".into());
                    }
                    if decision == Decision::Pass
                        && !obligations
                            .iter()
                            .all(|state| *state == ObligationState::Satisfied)
                    {
                        return Err("memory PASS occurred with an unsatisfied duty".into());
                    }
                }
            }
        }
    }
    if total != 256 || counts.iter().any(|count| *count == 0) {
        return Err("memory truth table is incomplete".into());
    }
    Ok((total, counts))
}

fn verify_effect_interval_map() -> Result<(), String> {
    let present = classify_effect_interval(
        true,
        true,
        EffectDirection::MustBePresent,
        0.30,
        0.35,
    );
    let absent = classify_effect_interval(
        true,
        true,
        EffectDirection::MustBeAbsent,
        0.00,
        0.05,
    );
    let empty = classify_effect_interval(
        true,
        false,
        EffectDirection::MustBePresent,
        0.30,
        0.35,
    );
    if present != ObligationState::Satisfied
        || absent != ObligationState::Satisfied
        || empty != ObligationState::Invalid
    {
        return Err("effect interval routing failed".into());
    }
    Ok(())
}

fn run_all_checks() -> Result<(), String> {
    verify_design_counts()?;
    verify_power_contract()?;
    verify_witness_laws()?;
    verify_boundary_truth_table()?;
    verify_numeric_row_map()?;
    verify_memory_truth_table()?;
    verify_effect_interval_map()?;
    Ok(())
}

fn main() {
    if let Err(error) = run_all_checks() {
        eprintln!("PTS0-CHECK: FAIL: {error}");
        std::process::exit(1);
    }

    let (cell_laws, distances) = design_counts();
    let (boundary_cases, boundary_counts) =
        verify_boundary_truth_table().expect("already checked boundary table");
    let numeric_cases = verify_numeric_row_map().expect("already checked numeric map");
    let (memory_cases, memory_counts) =
        verify_memory_truth_table().expect("already checked memory table");
    let minimum = minimum_attempts_per_cell();
    let simultaneous_bound = union_bound(CHOSEN_ATTEMPTS_PER_CELL);

    println!("PTS0-CHECK: PASS");
    println!("outcome_cells={OUTCOME_CELLS}");
    println!("assigned_cell_laws={cell_laws}");
    println!("registered_distances={distances}");
    println!("minimum_attempts_per_cell={minimum}");
    println!("chosen_attempts_per_cell={CHOSEN_ATTEMPTS_PER_CELL}");
    println!(
        "total_issued_attempts={}",
        CHOSEN_ATTEMPTS_PER_CELL * CELL_LAWS
    );
    println!("simultaneous_error_bound={simultaneous_bound:.15}");
    println!("distance_ci_radius={DISTANCE_CI_RADIUS:.6}");
    println!("boundary_aggregate_cases={boundary_cases}");
    println!("boundary_decision_counts={boundary_counts:?}");
    println!("numeric_row_cases={numeric_cases}");
    println!("memory_aggregate_cases={memory_cases}");
    println!("memory_decision_counts={memory_counts:?}");
    println!("empty_confidence_set=INVALID");
    println!("boundary_mismatch_never_implies=FAIL");
    println!("full_boundary_restart_never_enters=NATURAL_SUFFICIENCY");
    println!("memory_descent_never_fills=BOUNDARY_SUFFICIENCY");
    println!("authority=AUTHOR_SIDE_QA_ONLY");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn complete_checker_passes() {
        run_all_checks().unwrap();
    }

    #[test]
    fn empty_boundary_confidence_is_invalid() {
        let row = classify_boundary_row(true, false, false, 0.0, 0.0, 0.0, 0.0);
        assert_eq!(row, BoundaryRowState::Invalid);
    }

    #[test]
    fn mismatch_cannot_refute_sufficiency() {
        let decision = classify_boundary(&[BoundaryRowState::BoundaryMismatch]);
        assert_eq!(decision, Decision::Underdetermined);
    }

    #[test]
    fn forced_restart_is_not_natural_sufficiency() {
        let decision = classify_boundary(&[BoundaryRowState::ForcedRestart]);
        assert_eq!(decision, Decision::Invalid);
    }

    #[test]
    fn matched_residual_dependence_refutes_candidate() {
        let decision = classify_boundary(&[BoundaryRowState::MatchedFail]);
        assert_eq!(decision, Decision::Fail);
    }

    #[test]
    fn memory_and_boundary_outputs_remain_independent() {
        let memory = classify_memory_descent(&[
            ObligationState::Satisfied,
            ObligationState::Satisfied,
        ]);
        let boundary = classify_boundary(&[BoundaryRowState::MatchedUnresolved]);
        assert_eq!(memory, Decision::Pass);
        assert_eq!(boundary, Decision::Underdetermined);
    }
}
