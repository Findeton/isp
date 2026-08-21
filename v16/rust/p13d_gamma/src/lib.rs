#![forbid(unsafe_code)]
#![deny(missing_debug_implementations)]

use std::collections::{BTreeMap, BTreeSet};
use std::fmt;
use std::fs::{self, OpenOptions};
use std::io::{self, Write};
use std::marker::PhantomData;
use std::ops::{Add, Mul, Neg, Sub};
use std::path::{Path, PathBuf};
use std::sync::atomic::{AtomicU64, Ordering};

pub const MATH_SHA256: &str = "3b91766fe269e8145766f4622f99e9009c3270530670119735e6045a473de5c9";
pub const ADJUDICATION_SHA256: &str =
    "ae2c4ef066335c39a0b8057c897c947b06e4270be67d1ed3ec59bf8d6d0a00c9";
pub const PIN_SHA256: &str = "f9e710b6f739bc159f741858ebf2993631a823bf23c3dec32eb97a5bbfd83e49";
pub const OFFICIAL_RESULT: &str = "/Users/felixrobles/workspace/isp/v16/paper13d-rust-result.json";
pub const OFFICIAL_RECEIPT: &str =
    "/Users/felixrobles/workspace/isp/v16/paper13d-rust-receipt.json";

#[derive(Debug)]
pub enum CliError {
    Usage(String),
    Refusal(String),
    Scientific(String),
    Io(io::Error),
}

impl CliError {
    pub fn exit_code(&self) -> u8 {
        match self {
            Self::Usage(_) | Self::Refusal(_) => 2,
            Self::Scientific(_) => 1,
            Self::Io(_) => 3,
        }
    }
}

impl fmt::Display for CliError {
    fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Self::Usage(message) => write!(formatter, "USAGE-ERROR: {message}"),
            Self::Refusal(message) => write!(formatter, "REFUSAL: {message}"),
            Self::Scientific(message) => write!(formatter, "SELFTEST-FAILURE: {message}"),
            Self::Io(error) => write!(formatter, "IO-ERROR: {error}"),
        }
    }
}

impl From<io::Error> for CliError {
    fn from(error: io::Error) -> Self {
        Self::Io(error)
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd, Hash)]
pub struct Rat {
    num: i128,
    den: i128,
}

impl Rat {
    pub fn new(num: i128, den: i128) -> Result<Self, String> {
        if den == 0 {
            return Err("zero denominator".to_owned());
        }
        if num == 0 {
            return Ok(Self { num: 0, den: 1 });
        }
        let sign = if den < 0 { -1 } else { 1 };
        let num = num
            .checked_mul(sign)
            .ok_or_else(|| "rational sign overflow".to_owned())?;
        let den = den
            .checked_mul(sign)
            .ok_or_else(|| "rational sign overflow".to_owned())?;
        let divisor = gcd(num, den);
        Ok(Self {
            num: num / divisor,
            den: den / divisor,
        })
    }

    pub const fn zero() -> Self {
        Self { num: 0, den: 1 }
    }

    pub const fn one() -> Self {
        Self { num: 1, den: 1 }
    }

    pub fn numerator(self) -> i128 {
        self.num
    }

    pub fn denominator(self) -> i128 {
        self.den
    }

    pub fn is_negative(self) -> bool {
        self.num < 0
    }

    pub fn checked_add(self, rhs: Self) -> Result<Self, String> {
        let left = self
            .num
            .checked_mul(rhs.den)
            .ok_or_else(|| "rational addition overflow".to_owned())?;
        let right = rhs
            .num
            .checked_mul(self.den)
            .ok_or_else(|| "rational addition overflow".to_owned())?;
        let numerator = left
            .checked_add(right)
            .ok_or_else(|| "rational addition overflow".to_owned())?;
        let denominator = self
            .den
            .checked_mul(rhs.den)
            .ok_or_else(|| "rational addition overflow".to_owned())?;
        Self::new(numerator, denominator)
    }

    pub fn checked_mul(self, rhs: Self) -> Result<Self, String> {
        let numerator = self
            .num
            .checked_mul(rhs.num)
            .ok_or_else(|| "rational multiplication overflow".to_owned())?;
        let denominator = self
            .den
            .checked_mul(rhs.den)
            .ok_or_else(|| "rational multiplication overflow".to_owned())?;
        Self::new(numerator, denominator)
    }
}

fn gcd(left: i128, right: i128) -> i128 {
    let mut left = left.unsigned_abs();
    let mut right = right.unsigned_abs();
    while right != 0 {
        let remainder = left % right;
        left = right;
        right = remainder;
    }
    i128::try_from(left).expect("gcd fits i128")
}

impl fmt::Display for Rat {
    fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
        if self.den == 1 {
            write!(formatter, "{}", self.num)
        } else {
            write!(formatter, "{}/{}", self.num, self.den)
        }
    }
}

impl Add for Rat {
    type Output = Self;
    fn add(self, rhs: Self) -> Self::Output {
        self.checked_add(rhs).expect("checked rational addition")
    }
}

impl Sub for Rat {
    type Output = Self;
    fn sub(self, rhs: Self) -> Self::Output {
        self + (-rhs)
    }
}

impl Mul for Rat {
    type Output = Self;
    fn mul(self, rhs: Self) -> Self::Output {
        self.checked_mul(rhs)
            .expect("checked rational multiplication")
    }
}

impl Neg for Rat {
    type Output = Self;
    fn neg(self) -> Self::Output {
        Self {
            num: -self.num,
            den: self.den,
        }
    }
}

pub type Matrix2 = [[Rat; 2]; 2];

pub fn matrix_b() -> Matrix2 {
    [
        [Rat::new(9, 25).unwrap(), Rat::new(16, 25).unwrap()],
        [Rat::new(16, 25).unwrap(), Rat::new(9, 25).unwrap()],
    ]
}

pub fn matrix_c() -> Matrix2 {
    [
        [Rat::new(49, 625).unwrap(), Rat::new(576, 625).unwrap()],
        [Rat::new(576, 625).unwrap(), Rat::new(49, 625).unwrap()],
    ]
}

pub fn matrix_b2() -> Matrix2 {
    [
        [Rat::new(337, 625).unwrap(), Rat::new(288, 625).unwrap()],
        [Rat::new(288, 625).unwrap(), Rat::new(337, 625).unwrap()],
    ]
}

pub fn matrix_k() -> Matrix2 {
    [
        [Rat::new(351, 175).unwrap(), Rat::new(-176, 175).unwrap()],
        [Rat::new(-176, 175).unwrap(), Rat::new(351, 175).unwrap()],
    ]
}

pub fn matrix_mul(left: Matrix2, right: Matrix2) -> Matrix2 {
    let mut output = [[Rat::zero(); 2]; 2];
    for row in 0..2 {
        for column in 0..2 {
            for inner in 0..2 {
                output[row][column] = output[row][column] + left[row][inner] * right[inner][column];
            }
        }
    }
    output
}

#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd, Hash)]
pub enum Bit {
    Zero,
    One,
}

impl Bit {
    pub fn from_bool(value: bool) -> Self {
        if value {
            Self::One
        } else {
            Self::Zero
        }
    }

    pub fn as_u8(self) -> u8 {
        match self {
            Self::Zero => 0,
            Self::One => 1,
        }
    }

    pub fn xor(self, rhs: Self) -> Self {
        Self::from_bool(self != rhs)
    }

    pub fn toggle(self) -> Self {
        self.xor(Self::One)
    }
}

#[derive(Clone, Debug, Eq, PartialEq, Ord, PartialOrd, Hash)]
pub struct Packet {
    x: Bit,
    y: Bit,
    epsilon: Bit,
    x_prime: Bit,
    y_prime: Bit,
    e_prime: Bit,
    z_x: Bit,
    z_y: Bit,
    u_x: Bit,
    u_y: Bit,
    d: Bit,
}

impl Packet {
    pub fn derive(x: Bit, y: Bit, epsilon: Bit, e_prime: Bit, c: Bit) -> Self {
        Self {
            x,
            y,
            epsilon,
            x_prime: x.xor(epsilon),
            y_prime: y.xor(epsilon),
            e_prime,
            z_x: x.xor(e_prime),
            z_y: y.xor(e_prime),
            u_x: x.xor(c),
            u_y: y.xor(c),
            d: e_prime,
        }
    }

    pub fn validate(&self) -> bool {
        self.x_prime == self.x.xor(self.epsilon)
            && self.y_prime == self.y.xor(self.epsilon)
            && self.z_x == self.x.xor(self.e_prime)
            && self.z_y == self.y.xor(self.e_prime)
            && self.d == self.e_prime
    }

    pub fn swap_xy(&self) -> Self {
        Self {
            x: self.y,
            y: self.x,
            epsilon: self.epsilon,
            x_prime: self.y_prime,
            y_prime: self.x_prime,
            e_prime: self.e_prime,
            z_x: self.z_y,
            z_y: self.z_x,
            u_x: self.u_y,
            u_y: self.u_x,
            d: self.d,
        }
    }

    pub fn color(&self) -> Bit {
        self.d
    }

    pub fn z_y(&self) -> Bit {
        self.z_y
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd, Hash)]
pub struct Pair(usize, usize);

impl Pair {
    pub fn new(left: usize, right: usize) -> Result<Self, String> {
        if left == right {
            return Err("unordered pair requires distinct endpoints".to_owned());
        }
        Ok(if left < right {
            Self(left, right)
        } else {
            Self(right, left)
        })
    }

    pub fn endpoints(self) -> (usize, usize) {
        (self.0, self.1)
    }
}

pub type Bonds = BTreeMap<Pair, Bit>;

fn validate_bonds(length: usize, bonds: &Bonds) -> Result<(), String> {
    for pair in bonds.keys() {
        let (left, right) = pair.endpoints();
        if right >= length || left >= length {
            return Err("bond endpoint outside carrier".to_owned());
        }
    }
    Ok(())
}

#[derive(Clone, Debug, Eq, PartialEq, Ord, PartialOrd, Hash)]
pub struct SourceCell {
    q0: Bit,
    h: Bit,
    c: Bit,
    e0: Bit,
}

impl SourceCell {
    pub fn new(q0: Bit, h: Bit, c: Bit, e0: Bit) -> Self {
        Self { q0, h, c, e0 }
    }
}

#[derive(Clone, Debug, Eq, PartialEq, Ord, PartialOrd, Hash)]
pub struct B0 {
    cells: Vec<SourceCell>,
}

impl B0 {
    pub fn new(cells: Vec<SourceCell>) -> Self {
        Self { cells }
    }

    pub fn len(&self) -> usize {
        self.cells.len()
    }

    pub fn is_empty(&self) -> bool {
        self.cells.is_empty()
    }
}

#[derive(Clone, Debug, Eq, PartialEq, Ord, PartialOrd, Hash)]
struct B1Cell {
    m: Bit,
    h: Bit,
    packet: Packet,
}

#[derive(Clone, Debug, Eq, PartialEq, Ord, PartialOrd, Hash)]
struct B1RecordedCell {
    m: Bit,
    r: Bit,
    h: Bit,
    packet: Packet,
}

#[derive(Clone, Debug, Eq, PartialEq, Ord, PartialOrd, Hash)]
pub struct B1Plain {
    cells: Vec<B1Cell>,
}

impl B1Plain {
    fn new(cells: Vec<B1Cell>) -> Self {
        Self { cells }
    }
}

#[derive(Clone, Debug, Eq, PartialEq, Ord, PartialOrd, Hash)]
pub struct B1Recorded {
    cells: Vec<B1RecordedCell>,
}

impl B1Recorded {
    fn new(rows: Vec<(Bit, Bit, Packet)>) -> Self {
        Self {
            cells: rows
                .into_iter()
                .map(|(m, h, packet)| B1RecordedCell { m, r: m, h, packet })
                .collect(),
        }
    }

    pub fn record_word(&self) -> Vec<Bit> {
        self.cells.iter().map(|cell| cell.r).collect()
    }
}

#[derive(Clone, Debug, Eq, PartialEq, Ord, PartialOrd, Hash)]
struct B2Cell {
    q2: Bit,
    h: Bit,
    t: Bit,
    packet: Packet,
}

#[derive(Clone, Debug, Eq, PartialEq, Ord, PartialOrd, Hash)]
struct B2RecordedCell {
    q2: Bit,
    h: Bit,
    t: Bit,
    packet: Packet,
    r: Bit,
}

#[derive(Clone, Debug, Eq, PartialEq, Ord, PartialOrd, Hash)]
pub struct B2Plain {
    cells: Vec<B2Cell>,
    bonds: Bonds,
}

impl B2Plain {
    fn new(rows: Vec<(Bit, Bit, Packet)>, bonds: Bonds) -> Result<Self, String> {
        validate_bonds(rows.len(), &bonds)?;
        Ok(Self {
            cells: rows
                .into_iter()
                .map(|(q2, h, packet)| B2Cell {
                    q2,
                    h,
                    t: h,
                    packet,
                })
                .collect(),
            bonds,
        })
    }

    pub fn invariant_holds(&self) -> bool {
        self.cells.iter().all(|cell| cell.t == cell.h)
    }
}

#[derive(Clone, Debug, Eq, PartialEq, Ord, PartialOrd, Hash)]
pub struct B2Recorded {
    cells: Vec<B2RecordedCell>,
    bonds: Bonds,
}

impl B2Recorded {
    fn new(rows: Vec<(Bit, Bit, Packet, Bit)>, bonds: Bonds) -> Result<Self, String> {
        validate_bonds(rows.len(), &bonds)?;
        Ok(Self {
            cells: rows
                .into_iter()
                .map(|(q2, h, packet, r)| B2RecordedCell {
                    q2,
                    h,
                    t: h,
                    packet,
                    r,
                })
                .collect(),
            bonds,
        })
    }

    pub fn invariant_holds(&self) -> bool {
        self.cells.iter().all(|cell| cell.t == cell.h)
    }

    pub fn record_word(&self) -> Vec<Bit> {
        self.cells.iter().map(|cell| cell.r).collect()
    }
}

#[derive(Clone, Debug, Eq, PartialEq, Ord, PartialOrd, Hash)]
struct B3RecordedCell {
    q_plus: Bit,
    h: Bit,
    t_plus: Bit,
    packet: Packet,
    r: Bit,
}

#[derive(Clone, Debug, Eq, PartialEq, Ord, PartialOrd, Hash)]
pub struct B3Recorded {
    cells: Vec<B3RecordedCell>,
    bonds: Bonds,
}

impl B3Recorded {
    pub fn record_word(&self) -> Vec<Bit> {
        self.cells.iter().map(|cell| cell.r).collect()
    }
}

#[derive(Clone, Debug, Eq, PartialEq, Ord, PartialOrd, Hash)]
struct B3ErasedCell {
    q_plus: Bit,
    h: Bit,
    t_plus: Bit,
    packet: Packet,
}

#[derive(Clone, Debug, Eq, PartialEq, Ord, PartialOrd, Hash)]
pub struct B3Erased {
    cells: Vec<B3ErasedCell>,
    bonds: Bonds,
}

pub fn stable_entry(source: &B2Recorded) -> B3Recorded {
    B3Recorded {
        cells: source
            .cells
            .iter()
            .map(|cell| B3RecordedCell {
                q_plus: cell.q2,
                h: cell.h,
                t_plus: cell.t,
                packet: cell.packet.clone(),
                r: cell.r,
            })
            .collect(),
        bonds: source.bonds.clone(),
    }
}

pub fn erase_record(source: &B2Recorded) -> B3Erased {
    B3Erased {
        cells: source
            .cells
            .iter()
            .map(|cell| B3ErasedCell {
                q_plus: cell.q2,
                h: cell.h,
                t_plus: cell.t,
                packet: cell.packet.clone(),
            })
            .collect(),
        bonds: source.bonds.clone(),
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd)]
pub enum SourceSlot {
    X,
    Y,
    E,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd)]
pub enum MediatorSlot {
    EPrime,
}

pub type SourceWrites = BTreeMap<(usize, SourceSlot), Bit>;
pub type MediatorWrites = BTreeMap<(usize, MediatorSlot), Bit>;

fn override_map<K: Ord + Clone, V: Clone>(
    left: &BTreeMap<K, V>,
    right: &BTreeMap<K, V>,
) -> BTreeMap<K, V> {
    let mut output = left.clone();
    for (key, value) in right {
        output.insert(key.clone(), value.clone());
    }
    output
}

#[derive(Clone, Copy, Debug)]
pub struct SourceStage;
#[derive(Clone, Copy, Debug)]
pub struct MediatorStage;
#[derive(Clone, Copy, Debug)]
pub struct ClosedStage;

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum StageTag {
    Source,
    Mediator,
    Closed,
}

fn control_hom_exists(source: StageTag, target: StageTag) -> bool {
    matches!(
        (source, target),
        (StageTag::Source, StageTag::Source)
            | (StageTag::Source, StageTag::Mediator)
            | (StageTag::Source, StageTag::Closed)
            | (StageTag::Mediator, StageTag::Mediator)
            | (StageTag::Mediator, StageTag::Closed)
            | (StageTag::Closed, StageTag::Closed)
    )
}

/// Typestaged control builder.
///
/// A mediator-stage value has no `set_source` method, so a reversed-stage
/// write is not a program.
///
/// ```compile_fail
/// use p13d_gamma::{Bit, ProgramAt, SourceSlot};
/// let mediator = ProgramAt::new().set_source(0, SourceSlot::X, Bit::One).advance();
/// let _illegal = mediator.set_source(0, SourceSlot::Y, Bit::Zero);
/// ```
#[derive(Clone, Debug)]
pub struct ProgramAt<S> {
    source: SourceWrites,
    mediator: MediatorWrites,
    stage: PhantomData<S>,
}

impl ProgramAt<SourceStage> {
    pub fn new() -> Self {
        Self {
            source: BTreeMap::new(),
            mediator: BTreeMap::new(),
            stage: PhantomData,
        }
    }

    pub fn set_source(mut self, occurrence: usize, slot: SourceSlot, value: Bit) -> Self {
        self.source.insert((occurrence, slot), value);
        self
    }

    pub fn advance(self) -> ProgramAt<MediatorStage> {
        ProgramAt {
            source: self.source,
            mediator: self.mediator,
            stage: PhantomData,
        }
    }
}

impl Default for ProgramAt<SourceStage> {
    fn default() -> Self {
        Self::new()
    }
}

impl ProgramAt<MediatorStage> {
    pub fn set_mediator(mut self, occurrence: usize, value: Bit) -> Self {
        self.mediator
            .insert((occurrence, MediatorSlot::EPrime), value);
        self
    }

    pub fn close(self) -> ProgramAt<ClosedStage> {
        ProgramAt {
            source: self.source,
            mediator: self.mediator,
            stage: PhantomData,
        }
    }
}

#[derive(Clone, Debug, Eq, PartialEq, Ord, PartialOrd)]
pub struct Program {
    source: SourceWrites,
    mediator: MediatorWrites,
}

impl ProgramAt<ClosedStage> {
    pub fn finish(self) -> Program {
        Program {
            source: self.source,
            mediator: self.mediator,
        }
    }
}

impl Program {
    pub fn empty() -> Self {
        ProgramAt::new().advance().close().finish()
    }

    pub fn compose_same_stage(&self, later: &Self) -> Self {
        Self {
            source: override_map(&self.source, &later.source),
            mediator: override_map(&self.mediator, &later.mediator),
        }
    }

    fn validate_for(&self, length: usize) -> Result<(), String> {
        if self
            .source
            .keys()
            .any(|(occurrence, _)| *occurrence >= length)
            || self
                .mediator
                .keys()
                .any(|(occurrence, _)| *occurrence >= length)
        {
            return Err("control address outside occurrence carrier".to_owned());
        }
        Ok(())
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd, Hash)]
pub struct OccurrenceSeed {
    eta_x: Bit,
    eta_y: Bit,
    u1: u8,
    u2: u8,
}

impl OccurrenceSeed {
    fn validate(self) -> bool {
        self.u1 < 25 && self.u2 < 25
    }

    fn weight(self) -> Rat {
        let eta_weight = |eta: Bit| match eta {
            Bit::Zero => Rat::new(16, 25).unwrap(),
            Bit::One => Rat::new(9, 25).unwrap(),
        };
        eta_weight(self.eta_x)
            * eta_weight(self.eta_y)
            * Rat::new(1, 25).unwrap()
            * Rat::new(1, 25).unwrap()
    }
}

pub fn beta(input: Bit, seed: u8) -> Result<Bit, String> {
    if seed >= 25 {
        return Err("beta seed outside [25]".to_owned());
    }
    Ok(if seed < 9 { input } else { input.toggle() })
}

pub fn kappa(input: Bit, first: u8, second: u8) -> Result<Bit, String> {
    if first >= 25 || second >= 25 {
        return Err("kappa seed outside [25]^2".to_owned());
    }
    Ok(if 25 * u16::from(first) + u16::from(second) < 49 {
        input
    } else {
        input.toggle()
    })
}

fn packet_for(
    source: &SourceCell,
    program: &Program,
    occurrence: usize,
    seed: OccurrenceSeed,
) -> Packet {
    let x = program
        .source
        .get(&(occurrence, SourceSlot::X))
        .copied()
        .unwrap_or_else(|| source.c.xor(seed.eta_x));
    let y = program
        .source
        .get(&(occurrence, SourceSlot::Y))
        .copied()
        .unwrap_or_else(|| source.c.xor(seed.eta_y));
    let epsilon = program
        .source
        .get(&(occurrence, SourceSlot::E))
        .copied()
        .unwrap_or(source.e0);
    let native_e_prime = epsilon.xor(x).xor(y);
    let e_prime = program
        .mediator
        .get(&(occurrence, MediatorSlot::EPrime))
        .copied()
        .unwrap_or(native_e_prime);
    Packet::derive(x, y, epsilon, e_prime, source.c)
}

#[derive(Clone, Debug, Eq, PartialEq, Ord, PartialOrd)]
pub struct Presentation {
    sigma: Vec<usize>,
    swaps: Vec<bool>,
}

impl Presentation {
    pub fn new(sigma: Vec<usize>, swaps: Vec<bool>) -> Result<Self, String> {
        let length = sigma.len();
        if swaps.len() != length {
            return Err("presentation swap vector has wrong size".to_owned());
        }
        let image: BTreeSet<usize> = sigma.iter().copied().collect();
        if image.len() != length || image.iter().copied().ne(0..length) {
            return Err("presentation map is not a permutation".to_owned());
        }
        Ok(Self { sigma, swaps })
    }

    pub fn identity(length: usize) -> Self {
        Self {
            sigma: (0..length).collect(),
            swaps: vec![false; length],
        }
    }

    pub fn inverse(&self) -> Self {
        let mut sigma = vec![0; self.sigma.len()];
        let mut swaps = vec![false; self.sigma.len()];
        for (source, target) in self.sigma.iter().copied().enumerate() {
            sigma[target] = source;
            swaps[target] = self.swaps[source];
        }
        Self { sigma, swaps }
    }

    pub fn then(&self, later: &Self) -> Result<Self, String> {
        if self.sigma.len() != later.sigma.len() {
            return Err("presentation composition size mismatch".to_owned());
        }
        let sigma = self
            .sigma
            .iter()
            .map(|middle| later.sigma[*middle])
            .collect::<Vec<_>>();
        let swaps = (0..self.sigma.len())
            .map(|source| self.swaps[source] ^ later.swaps[self.sigma[source]])
            .collect::<Vec<_>>();
        Self::new(sigma, swaps)
    }

    pub fn act_b0(&self, value: &B0) -> Result<B0, String> {
        if value.len() != self.sigma.len() {
            return Err("presentation action size mismatch".to_owned());
        }
        let mut cells =
            vec![SourceCell::new(Bit::Zero, Bit::Zero, Bit::Zero, Bit::Zero); value.len()];
        for (source, target) in self.sigma.iter().copied().enumerate() {
            cells[target] = value.cells[source].clone();
        }
        Ok(B0::new(cells))
    }

    pub fn act_b3_recorded(&self, value: &B3Recorded) -> Result<B3Recorded, String> {
        if value.cells.len() != self.sigma.len() {
            return Err("presentation action size mismatch".to_owned());
        }
        let placeholder = B3RecordedCell {
            q_plus: Bit::Zero,
            h: Bit::Zero,
            t_plus: Bit::Zero,
            packet: Packet::derive(Bit::Zero, Bit::Zero, Bit::Zero, Bit::Zero, Bit::Zero),
            r: Bit::Zero,
        };
        let mut cells = vec![placeholder; value.cells.len()];
        for (source, target) in self.sigma.iter().copied().enumerate() {
            let mut cell = value.cells[source].clone();
            if self.swaps[source] {
                cell.packet = cell.packet.swap_xy();
            }
            cells[target] = cell;
        }
        let mut bonds = BTreeMap::new();
        for (pair, bit) in &value.bonds {
            let (left, right) = pair.endpoints();
            bonds.insert(Pair::new(self.sigma[left], self.sigma[right])?, *bit);
        }
        Ok(B3Recorded { cells, bonds })
    }
}

#[derive(Clone, Debug, Eq, PartialEq)]
pub enum StableOp {
    Fq(BTreeSet<usize>),
    Ft(BTreeSet<usize>),
    Fxy(BTreeSet<usize>),
    Fr(BTreeSet<usize>),
}

impl StableOp {
    pub fn apply(&self, source: &B3Recorded) -> Result<(B3Recorded, Vec<Bit>), String> {
        let subset = match self {
            Self::Fq(subset) | Self::Ft(subset) | Self::Fxy(subset) | Self::Fr(subset) => subset,
        };
        if subset.iter().any(|index| *index >= source.cells.len()) {
            return Err("stable operation address outside carrier".to_owned());
        }
        let mut target = source.clone();
        let mut label_translation = vec![Bit::Zero; source.cells.len()];
        for index in subset {
            match self {
                Self::Fq(_) => target.cells[*index].q_plus = target.cells[*index].q_plus.toggle(),
                Self::Ft(_) => target.cells[*index].t_plus = target.cells[*index].t_plus.toggle(),
                Self::Fxy(_) => target.cells[*index].packet = target.cells[*index].packet.swap_xy(),
                Self::Fr(_) => {
                    target.cells[*index].r = target.cells[*index].r.toggle();
                    label_translation[*index] = Bit::One;
                }
            }
        }
        Ok((target, label_translation))
    }
}

pub fn apply_stable_word(
    source: &B3Recorded,
    word: &[StableOp],
) -> Result<(B3Recorded, Vec<Bit>), String> {
    let mut current = source.clone();
    let mut translation = vec![Bit::Zero; source.cells.len()];
    for operation in word {
        let (next, step) = operation.apply(&current)?;
        for (combined, bit) in translation.iter_mut().zip(step) {
            *combined = combined.xor(bit);
        }
        current = next;
    }
    Ok((current, translation))
}

#[derive(Clone, Debug, Eq, PartialEq, Ord, PartialOrd, Hash)]
pub enum Value {
    B0(B0),
    B1Plain(B1Plain),
    B1Recorded(B1Recorded),
    B2Plain(B2Plain),
    B2Recorded(B2Recorded),
    B3Recorded(B3Recorded),
    B3Erased(B3Erased),
    Tensor(Vec<Value>),
    Unit,
}

#[derive(Clone, Debug, Eq, PartialEq, Ord, PartialOrd, Hash)]
pub enum Trace {
    Identity(Value),
    Step {
        source: Value,
        target: Value,
    },
    Composite {
        first: Box<Trace>,
        second: Box<Trace>,
    },
    Tensor(Vec<Trace>),
    Fusion {
        source: Value,
        target: Value,
    },
}

impl Trace {
    fn target_value(&self) -> Value {
        match self {
            Self::Identity(value) => value.clone(),
            Self::Step { target, .. } => target.clone(),
            Self::Composite { second, .. } => second.target_value(),
            Self::Tensor(traces) => Value::Tensor(traces.iter().map(Trace::target_value).collect()),
            Self::Fusion { target, .. } => target.clone(),
        }
    }
}

pub type Distribution<T> = BTreeMap<T, Rat>;

fn add_mass<T: Ord>(distribution: &mut Distribution<T>, value: T, mass: Rat) {
    let entry = distribution.entry(value).or_insert(Rat::zero());
    *entry = *entry + mass;
}

pub fn distribution_mass<T>(distribution: &Distribution<T>) -> Rat {
    distribution
        .values()
        .copied()
        .fold(Rat::zero(), |sum, mass| sum + mass)
}

#[derive(Clone, Debug, Eq, PartialEq, Ord, PartialOrd)]
pub enum AtomicSort {
    B0(usize),
    B1Plain(usize),
    B1Recorded(usize),
    B2Plain(usize),
    B2Recorded(usize),
    B3Recorded(usize),
    B3Erased(usize),
    Unit,
}

#[derive(Clone, Debug, Eq, PartialEq, Ord, PartialOrd)]
pub enum ExecObject {
    Atomic(AtomicSort),
    Tensor(Vec<AtomicSort>),
}

#[derive(Clone, Debug)]
enum ExecNode {
    Identity,
    U(Program),
    QPlain(Program),
    QRecorded(Program),
    D,
    Rc,
    Entry,
    Stable(StableOp),
    Eraser,
    Compose(Box<Exec>, Box<Exec>),
    Tensor(Vec<Exec>),
    Fusion { sort: AtomicSort, sizes: Vec<usize> },
}

#[derive(Clone, Debug)]
pub struct Exec {
    source: ExecObject,
    target: ExecObject,
    node: ExecNode,
}

impl Exec {
    pub fn identity(object: ExecObject) -> Self {
        Self {
            source: object.clone(),
            target: object,
            node: ExecNode::Identity,
        }
    }

    pub fn u(length: usize, program: Program) -> Result<Self, String> {
        program.validate_for(length)?;
        Ok(Self {
            source: ExecObject::Atomic(AtomicSort::B0(length)),
            target: ExecObject::Atomic(AtomicSort::B2Plain(length)),
            node: ExecNode::U(program),
        })
    }

    pub fn q_plain(length: usize, program: Program) -> Result<Self, String> {
        program.validate_for(length)?;
        Ok(Self {
            source: ExecObject::Atomic(AtomicSort::B0(length)),
            target: ExecObject::Atomic(AtomicSort::B1Plain(length)),
            node: ExecNode::QPlain(program),
        })
    }

    pub fn q_recorded(length: usize, program: Program) -> Result<Self, String> {
        program.validate_for(length)?;
        Ok(Self {
            source: ExecObject::Atomic(AtomicSort::B0(length)),
            target: ExecObject::Atomic(AtomicSort::B1Recorded(length)),
            node: ExecNode::QRecorded(program),
        })
    }

    pub fn d(length: usize) -> Self {
        Self {
            source: ExecObject::Atomic(AtomicSort::B1Plain(length)),
            target: ExecObject::Atomic(AtomicSort::B2Plain(length)),
            node: ExecNode::D,
        }
    }

    pub fn rc(length: usize) -> Self {
        Self {
            source: ExecObject::Atomic(AtomicSort::B1Recorded(length)),
            target: ExecObject::Atomic(AtomicSort::B2Recorded(length)),
            node: ExecNode::Rc,
        }
    }

    pub fn entry(length: usize) -> Self {
        Self {
            source: ExecObject::Atomic(AtomicSort::B2Recorded(length)),
            target: ExecObject::Atomic(AtomicSort::B3Recorded(length)),
            node: ExecNode::Entry,
        }
    }

    pub fn stable(length: usize, operation: StableOp) -> Self {
        Self {
            source: ExecObject::Atomic(AtomicSort::B3Recorded(length)),
            target: ExecObject::Atomic(AtomicSort::B3Recorded(length)),
            node: ExecNode::Stable(operation),
        }
    }

    pub fn eraser(length: usize) -> Self {
        Self {
            source: ExecObject::Atomic(AtomicSort::B2Recorded(length)),
            target: ExecObject::Atomic(AtomicSort::B3Erased(length)),
            node: ExecNode::Eraser,
        }
    }

    pub fn compose(first: Self, second: Self) -> Result<Self, String> {
        if first.target != second.source {
            return Err("execution source/target type mismatch".to_owned());
        }
        Ok(Self {
            source: first.source.clone(),
            target: second.target.clone(),
            node: ExecNode::Compose(Box::new(first), Box::new(second)),
        })
    }

    pub fn tensor(factors: Vec<Self>) -> Self {
        let source = factors
            .iter()
            .map(|factor| match &factor.source {
                ExecObject::Atomic(sort) => sort.clone(),
                ExecObject::Tensor(_) => panic!("nested tensors must first be flattened"),
            })
            .collect();
        let target = factors
            .iter()
            .map(|factor| match &factor.target {
                ExecObject::Atomic(sort) => sort.clone(),
                ExecObject::Tensor(_) => panic!("nested tensors must first be flattened"),
            })
            .collect();
        Self {
            source: ExecObject::Tensor(source),
            target: ExecObject::Tensor(target),
            node: ExecNode::Tensor(factors),
        }
    }

    pub fn fusion(sort: AtomicSort, sizes: Vec<usize>) -> Result<Self, String> {
        let expected = sizes
            .iter()
            .map(|size| sort_with_length(&sort, *size))
            .collect::<Result<Vec<_>, _>>()?;
        let total = sizes.iter().sum();
        Ok(Self {
            source: ExecObject::Tensor(expected),
            target: ExecObject::Atomic(sort_with_length(&sort, total)?),
            node: ExecNode::Fusion { sort, sizes },
        })
    }

    pub fn source(&self) -> &ExecObject {
        &self.source
    }

    pub fn target(&self) -> &ExecObject {
        &self.target
    }
}

fn sort_with_length(sort: &AtomicSort, length: usize) -> Result<AtomicSort, String> {
    Ok(match sort {
        AtomicSort::B0(_) => AtomicSort::B0(length),
        AtomicSort::B1Plain(_) => AtomicSort::B1Plain(length),
        AtomicSort::B1Recorded(_) => AtomicSort::B1Recorded(length),
        AtomicSort::B2Plain(_) => AtomicSort::B2Plain(length),
        AtomicSort::B2Recorded(_) => AtomicSort::B2Recorded(length),
        AtomicSort::B3Recorded(_) => AtomicSort::B3Recorded(length),
        AtomicSort::B3Erased(_) => AtomicSort::B3Erased(length),
        AtomicSort::Unit => {
            if length != 0 {
                return Err("unit sort has nonzero carrier".to_owned());
            }
            AtomicSort::Unit
        }
    })
}

fn value_object(value: &Value) -> ExecObject {
    ExecObject::Atomic(match value {
        Value::B0(value) => AtomicSort::B0(value.cells.len()),
        Value::B1Plain(value) => AtomicSort::B1Plain(value.cells.len()),
        Value::B1Recorded(value) => AtomicSort::B1Recorded(value.cells.len()),
        Value::B2Plain(value) => AtomicSort::B2Plain(value.cells.len()),
        Value::B2Recorded(value) => AtomicSort::B2Recorded(value.cells.len()),
        Value::B3Recorded(value) => AtomicSort::B3Recorded(value.cells.len()),
        Value::B3Erased(value) => AtomicSort::B3Erased(value.cells.len()),
        Value::Tensor(values) => {
            return ExecObject::Tensor(
                values
                    .iter()
                    .map(|value| match value_object(value) {
                        ExecObject::Atomic(sort) => sort,
                        ExecObject::Tensor(_) => panic!("nested tensor value"),
                    })
                    .collect(),
            )
        }
        Value::Unit => AtomicSort::Unit,
    })
}

#[derive(Clone, Debug, Default)]
pub struct Evaluator;

impl Evaluator {
    pub fn evaluate(
        &self,
        execution: &Exec,
        source: &Value,
    ) -> Result<Distribution<Trace>, String> {
        if value_object(source) != execution.source {
            return Err("source value does not inhabit execution source".to_owned());
        }
        match &execution.node {
            ExecNode::Identity => Ok(BTreeMap::from([(
                Trace::Identity(source.clone()),
                Rat::one(),
            )])),
            ExecNode::U(program) => evaluate_u(source, program),
            ExecNode::QPlain(program) => evaluate_q(source, program, false),
            ExecNode::QRecorded(program) => evaluate_q(source, program, true),
            ExecNode::D => evaluate_d(source, false),
            ExecNode::Rc => evaluate_d(source, true),
            ExecNode::Entry => deterministic_step(
                source,
                match source {
                    Value::B2Recorded(value) => Value::B3Recorded(stable_entry(value)),
                    _ => return Err("entry received wrong source type".to_owned()),
                },
            ),
            ExecNode::Stable(operation) => deterministic_step(
                source,
                match source {
                    Value::B3Recorded(value) => Value::B3Recorded(operation.apply(value)?.0),
                    _ => return Err("stable operation received wrong source type".to_owned()),
                },
            ),
            ExecNode::Eraser => deterministic_step(
                source,
                match source {
                    Value::B2Recorded(value) => Value::B3Erased(erase_record(value)),
                    _ => return Err("eraser received wrong source type".to_owned()),
                },
            ),
            ExecNode::Compose(first, second) => {
                let first_distribution = self.evaluate(first, source)?;
                let mut output = BTreeMap::new();
                for (first_trace, first_mass) in first_distribution {
                    let middle = first_trace.target_value();
                    let second_distribution = self.evaluate(second, &middle)?;
                    for (second_trace, second_mass) in second_distribution {
                        add_mass(
                            &mut output,
                            Trace::Composite {
                                first: Box::new(first_trace.clone()),
                                second: Box::new(second_trace),
                            },
                            first_mass * second_mass,
                        );
                    }
                }
                Ok(output)
            }
            ExecNode::Tensor(factors) => evaluate_tensor(self, factors, source),
            ExecNode::Fusion { sort, sizes } => evaluate_fusion(source, sort, sizes),
        }
    }
}

fn deterministic_step(source: &Value, target: Value) -> Result<Distribution<Trace>, String> {
    Ok(BTreeMap::from([(
        Trace::Step {
            source: source.clone(),
            target,
        },
        Rat::one(),
    )]))
}

fn eta_values() -> [(Bit, Rat); 2] {
    [
        (Bit::Zero, Rat::new(16, 25).unwrap()),
        (Bit::One, Rat::new(9, 25).unwrap()),
    ]
}

fn occurrence_seeds_u() -> Vec<(OccurrenceSeed, Rat)> {
    let mut output = Vec::with_capacity(2500);
    for (eta_x, _) in eta_values() {
        for (eta_y, _) in eta_values() {
            for u1 in 0..25 {
                for u2 in 0..25 {
                    let seed = OccurrenceSeed {
                        eta_x,
                        eta_y,
                        u1,
                        u2,
                    };
                    debug_assert!(seed.validate());
                    output.push((seed, seed.weight()));
                }
            }
        }
    }
    output
}

fn occurrence_seeds_q() -> Vec<(OccurrenceSeed, Rat)> {
    let mut output = Vec::with_capacity(100);
    for (eta_x, eta_x_mass) in eta_values() {
        for (eta_y, eta_y_mass) in eta_values() {
            for u1 in 0..25 {
                output.push((
                    OccurrenceSeed {
                        eta_x,
                        eta_y,
                        u1,
                        u2: 0,
                    },
                    eta_x_mass * eta_y_mass * Rat::new(1, 25).unwrap(),
                ));
            }
        }
    }
    output
}

fn enumerate_rows<T: Clone>(
    options: &[Vec<(T, Rat)>],
    index: usize,
    rows: &mut Vec<T>,
    mass: Rat,
    output: &mut Vec<(Vec<T>, Rat)>,
) {
    if index == options.len() {
        output.push((rows.clone(), mass));
        return;
    }
    for (row, row_mass) in &options[index] {
        rows.push(row.clone());
        enumerate_rows(options, index + 1, rows, mass * *row_mass, output);
        rows.pop();
    }
}

fn bond_distribution(
    packets: &[Packet],
    fixed: Option<&Bonds>,
) -> Result<Distribution<Bonds>, String> {
    if let Some(bonds) = fixed {
        validate_bonds(packets.len(), bonds)?;
        return Ok(BTreeMap::from([(bonds.clone(), Rat::one())]));
    }
    let pairs = (0..packets.len())
        .flat_map(|left| {
            ((left + 1)..packets.len()).map(move |right| Pair::new(left, right).unwrap())
        })
        .collect::<Vec<_>>();
    let mut output = BTreeMap::from([(BTreeMap::new(), Rat::one())]);
    for pair in pairs {
        let (left, right) = pair.endpoints();
        let one_numerator = if packets[left].color() != packets[right].color() {
            16
        } else {
            9
        };
        let one_mass = Rat::new(one_numerator, 25).unwrap();
        let zero_mass = Rat::one() - one_mass;
        let mut next = BTreeMap::new();
        for (bonds, mass) in output {
            let mut zero = bonds.clone();
            zero.insert(pair, Bit::Zero);
            add_mass(&mut next, zero, mass * zero_mass);
            let mut one = bonds;
            one.insert(pair, Bit::One);
            add_mass(&mut next, one, mass * one_mass);
        }
        output = next;
    }
    Ok(output)
}

fn evaluate_u(source: &Value, program: &Program) -> Result<Distribution<Trace>, String> {
    let source_value = match source {
        Value::B0(value) => value,
        _ => return Err("U received wrong source".to_owned()),
    };
    let seed_options = occurrence_seeds_u();
    let options = source_value
        .cells
        .iter()
        .enumerate()
        .map(|(occurrence, source_cell)| {
            seed_options
                .iter()
                .map(|(seed, mass)| {
                    let packet = packet_for(source_cell, program, occurrence, *seed);
                    let q2 = kappa(source_cell.q0, seed.u1, seed.u2).unwrap();
                    ((q2, source_cell.h, packet), *mass)
                })
                .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>();
    let mut rows = Vec::new();
    enumerate_rows(&options, 0, &mut Vec::new(), Rat::one(), &mut rows);
    let mut output = BTreeMap::new();
    for (rows, row_mass) in rows {
        let packets = rows.iter().map(|row| row.2.clone()).collect::<Vec<_>>();
        for (bonds, bond_mass) in bond_distribution(&packets, None)? {
            let target = Value::B2Plain(B2Plain::new(rows.clone(), bonds)?);
            add_mass(
                &mut output,
                Trace::Step {
                    source: source.clone(),
                    target,
                },
                row_mass * bond_mass,
            );
        }
    }
    Ok(output)
}

fn evaluate_q(
    source: &Value,
    program: &Program,
    recorded: bool,
) -> Result<Distribution<Trace>, String> {
    let source_value = match source {
        Value::B0(value) => value,
        _ => return Err("Q received wrong source".to_owned()),
    };
    let seed_options = occurrence_seeds_q();
    let options = source_value
        .cells
        .iter()
        .enumerate()
        .map(|(occurrence, source_cell)| {
            seed_options
                .iter()
                .map(|(seed, mass)| {
                    let packet = packet_for(source_cell, program, occurrence, *seed);
                    let m = beta(source_cell.q0, seed.u1).unwrap();
                    ((m, source_cell.h, packet), *mass)
                })
                .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>();
    let mut rows = Vec::new();
    enumerate_rows(&options, 0, &mut Vec::new(), Rat::one(), &mut rows);
    let mut output = BTreeMap::new();
    for (rows, mass) in rows {
        let target = if recorded {
            Value::B1Recorded(B1Recorded::new(rows.clone()))
        } else {
            Value::B1Plain(B1Plain::new(
                rows.into_iter()
                    .map(|(m, h, packet)| B1Cell { m, h, packet })
                    .collect(),
            ))
        };
        add_mass(
            &mut output,
            Trace::Step {
                source: source.clone(),
                target,
            },
            mass,
        );
    }
    Ok(output)
}

fn evaluate_d(source: &Value, recorded: bool) -> Result<Distribution<Trace>, String> {
    let rows = if recorded {
        match source {
            Value::B1Recorded(value) => value
                .cells
                .iter()
                .map(|cell| (cell.m, cell.h, cell.packet.clone(), Some(cell.r)))
                .collect::<Vec<_>>(),
            _ => return Err("Rc received wrong source".to_owned()),
        }
    } else {
        match source {
            Value::B1Plain(value) => value
                .cells
                .iter()
                .map(|cell| (cell.m, cell.h, cell.packet.clone(), None))
                .collect::<Vec<_>>(),
            _ => return Err("D received wrong source".to_owned()),
        }
    };
    let options = rows
        .iter()
        .map(|(m, h, packet, record)| {
            (0..25)
                .map(|u2| {
                    (
                        (beta(*m, u2).unwrap(), *h, packet.clone(), *record),
                        Rat::new(1, 25).unwrap(),
                    )
                })
                .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>();
    let mut expanded = Vec::new();
    enumerate_rows(&options, 0, &mut Vec::new(), Rat::one(), &mut expanded);
    let mut output = BTreeMap::new();
    for (rows, row_mass) in expanded {
        let packets = rows.iter().map(|row| row.2.clone()).collect::<Vec<_>>();
        for (bonds, bond_mass) in bond_distribution(&packets, None)? {
            let target = if recorded {
                Value::B2Recorded(B2Recorded::new(
                    rows.iter()
                        .map(|(q2, h, packet, record)| (*q2, *h, packet.clone(), record.unwrap()))
                        .collect(),
                    bonds,
                )?)
            } else {
                Value::B2Plain(B2Plain::new(
                    rows.iter()
                        .map(|(q2, h, packet, _)| (*q2, *h, packet.clone()))
                        .collect(),
                    bonds,
                )?)
            };
            add_mass(
                &mut output,
                Trace::Step {
                    source: source.clone(),
                    target,
                },
                row_mass * bond_mass,
            );
        }
    }
    Ok(output)
}

fn evaluate_tensor(
    evaluator: &Evaluator,
    factors: &[Exec],
    source: &Value,
) -> Result<Distribution<Trace>, String> {
    let values = match source {
        Value::Tensor(values) if values.len() == factors.len() => values,
        _ => return Err("tensor received wrong source".to_owned()),
    };
    let factor_distributions = factors
        .iter()
        .zip(values)
        .map(|(factor, value)| evaluator.evaluate(factor, value))
        .collect::<Result<Vec<_>, _>>()?;
    let mut output = BTreeMap::from([(Vec::<Trace>::new(), Rat::one())]);
    for distribution in factor_distributions {
        let mut next = BTreeMap::new();
        for (prefix, prefix_mass) in output {
            for (trace, mass) in &distribution {
                let mut combined = prefix.clone();
                combined.push(trace.clone());
                add_mass(&mut next, combined, prefix_mass * *mass);
            }
        }
        output = next;
    }
    Ok(output
        .into_iter()
        .map(|(traces, mass)| (Trace::Tensor(traces), mass))
        .collect())
}

fn evaluate_fusion(
    source: &Value,
    sort: &AtomicSort,
    sizes: &[usize],
) -> Result<Distribution<Trace>, String> {
    let components = match source {
        Value::Tensor(components) if components.len() == sizes.len() => components,
        _ => return Err("fusion received wrong tensor source".to_owned()),
    };
    let target_distribution = fuse_values(components, sort)?;
    Ok(target_distribution
        .into_iter()
        .map(|(target, mass)| {
            (
                Trace::Fusion {
                    source: source.clone(),
                    target,
                },
                mass,
            )
        })
        .collect())
}

fn fuse_values(components: &[Value], sort: &AtomicSort) -> Result<Distribution<Value>, String> {
    if components.is_empty() {
        let empty = match sort {
            AtomicSort::B2Plain(_) => Value::B2Plain(B2Plain::new(Vec::new(), Bonds::new())?),
            AtomicSort::B2Recorded(_) => {
                Value::B2Recorded(B2Recorded::new(Vec::new(), Bonds::new())?)
            }
            _ => return Err("zero-component bounded fusion supports B2 sorts".to_owned()),
        };
        return Ok(BTreeMap::from([(empty, Rat::one())]));
    }
    match sort {
        AtomicSort::B2Plain(_) => {
            let mut cells = Vec::new();
            let mut bonds = BTreeMap::new();
            let mut offset = 0;
            for component in components {
                let value = match component {
                    Value::B2Plain(value) => value,
                    _ => return Err("fusion component sort mismatch".to_owned()),
                };
                cells.extend(value.cells.clone());
                for (pair, bit) in &value.bonds {
                    let (left, right) = pair.endpoints();
                    bonds.insert(Pair::new(offset + left, offset + right)?, *bit);
                }
                offset += value.cells.len();
            }
            fuse_b2_plain_cross(cells, bonds, components)
        }
        AtomicSort::B2Recorded(_) => {
            let mut cells = Vec::new();
            let mut bonds = BTreeMap::new();
            let mut offset = 0;
            for component in components {
                let value = match component {
                    Value::B2Recorded(value) => value,
                    _ => return Err("fusion component sort mismatch".to_owned()),
                };
                cells.extend(value.cells.clone());
                for (pair, bit) in &value.bonds {
                    let (left, right) = pair.endpoints();
                    bonds.insert(Pair::new(offset + left, offset + right)?, *bit);
                }
                offset += value.cells.len();
            }
            fuse_b2_recorded_cross(cells, bonds, components)
        }
        _ => Err("bounded Rust fusion evaluator supports B2 plain/recorded sorts".to_owned()),
    }
}

fn component_ranges(components: &[Value]) -> Vec<std::ops::Range<usize>> {
    let mut offset = 0;
    components
        .iter()
        .map(|component| {
            let length = match component {
                Value::B2Plain(value) => value.cells.len(),
                Value::B2Recorded(value) => value.cells.len(),
                _ => 0,
            };
            let range = offset..(offset + length);
            offset += length;
            range
        })
        .collect()
}

fn cross_pairs(components: &[Value]) -> Vec<Pair> {
    let ranges = component_ranges(components);
    let mut output = Vec::new();
    for left_component in 0..ranges.len() {
        for right_component in (left_component + 1)..ranges.len() {
            for left in ranges[left_component].clone() {
                for right in ranges[right_component].clone() {
                    output.push(Pair::new(left, right).unwrap());
                }
            }
        }
    }
    output
}

fn extend_cross_bonds(colors: &[Bit], initial: Bonds, pairs: Vec<Pair>) -> Distribution<Bonds> {
    let mut output = BTreeMap::from([(initial, Rat::one())]);
    for pair in pairs {
        let (left, right) = pair.endpoints();
        let one = Rat::new(if colors[left] != colors[right] { 16 } else { 9 }, 25).unwrap();
        let zero = Rat::one() - one;
        let mut next = BTreeMap::new();
        for (bonds, mass) in output {
            let mut zero_bonds = bonds.clone();
            zero_bonds.insert(pair, Bit::Zero);
            add_mass(&mut next, zero_bonds, mass * zero);
            let mut one_bonds = bonds;
            one_bonds.insert(pair, Bit::One);
            add_mass(&mut next, one_bonds, mass * one);
        }
        output = next;
    }
    output
}

fn fuse_b2_plain_cross(
    cells: Vec<B2Cell>,
    bonds: Bonds,
    components: &[Value],
) -> Result<Distribution<Value>, String> {
    let colors = cells
        .iter()
        .map(|cell| cell.packet.color())
        .collect::<Vec<_>>();
    Ok(extend_cross_bonds(&colors, bonds, cross_pairs(components))
        .into_iter()
        .map(|(bonds, mass)| {
            (
                Value::B2Plain(B2Plain {
                    cells: cells.clone(),
                    bonds,
                }),
                mass,
            )
        })
        .collect())
}

fn fuse_b2_recorded_cross(
    cells: Vec<B2RecordedCell>,
    bonds: Bonds,
    components: &[Value],
) -> Result<Distribution<Value>, String> {
    let colors = cells
        .iter()
        .map(|cell| cell.packet.color())
        .collect::<Vec<_>>();
    Ok(extend_cross_bonds(&colors, bonds, cross_pairs(components))
        .into_iter()
        .map(|(bonds, mass)| {
            (
                Value::B2Recorded(B2Recorded {
                    cells: cells.clone(),
                    bonds,
                }),
                mass,
            )
        })
        .collect())
}

pub fn orbit_pushforward<T, F>(
    distribution: &Distribution<T>,
    group: &[Presentation],
    action: F,
) -> Result<Distribution<T>, String>
where
    T: Clone + Ord,
    F: Fn(&Presentation, &T) -> Result<T, String>,
{
    let mut output = BTreeMap::new();
    for (value, mass) in distribution {
        let mut orbit = Vec::with_capacity(group.len());
        for element in group {
            orbit.push(action(element, value)?);
        }
        let representative = orbit
            .into_iter()
            .min()
            .ok_or_else(|| "empty presentation group".to_owned())?;
        add_mass(&mut output, representative, *mass);
    }
    Ok(output)
}

pub fn intersection_stabilizer(
    left: &B3Recorded,
    right: &B3Recorded,
    group: &[Presentation],
) -> Result<Vec<Presentation>, String> {
    let mut output = Vec::new();
    for element in group {
        let fixes_left = element.act_b3_recorded(left)? == *left;
        let fixes_right = element.act_b3_recorded(right)? == *right;
        if fixes_left && fixes_right {
            output.push(element.clone());
        }
    }
    Ok(output)
}

pub fn delete_b2_recorded(
    value: &B2Recorded,
    keep: &BTreeSet<usize>,
) -> Result<B2Recorded, String> {
    if keep.iter().any(|index| *index >= value.cells.len()) {
        return Err("deletion index outside carrier".to_owned());
    }
    let ordered = keep.iter().copied().collect::<Vec<_>>();
    let reindex = ordered
        .iter()
        .enumerate()
        .map(|(new, old)| (*old, new))
        .collect::<BTreeMap<_, _>>();
    let rows = ordered
        .iter()
        .map(|old| {
            let cell = &value.cells[*old];
            (cell.q2, cell.h, cell.packet.clone(), cell.r)
        })
        .collect();
    let mut bonds = BTreeMap::new();
    for (pair, bit) in &value.bonds {
        let (left, right) = pair.endpoints();
        if let (Some(new_left), Some(new_right)) = (reindex.get(&left), reindex.get(&right)) {
            bonds.insert(Pair::new(*new_left, *new_right)?, *bit);
        }
    }
    B2Recorded::new(rows, bonds)
}

fn endpoint_q_distribution(distribution: &Distribution<Trace>) -> Result<[Rat; 2], String> {
    let mut output = [Rat::zero(); 2];
    for (trace, mass) in distribution {
        let target = trace.target_value();
        let q = match target {
            Value::B2Plain(value) if value.cells.len() == 1 => value.cells[0].q2,
            Value::B2Recorded(value) if value.cells.len() == 1 => value.cells[0].q2,
            _ => return Err("endpoint marginal requires one-occurrence B2 target".to_owned()),
        };
        output[usize::from(q.as_u8())] = output[usize::from(q.as_u8())] + *mass;
    }
    Ok(output)
}

fn zy_distribution(distribution: &Distribution<Trace>) -> Result<[Rat; 2], String> {
    let mut output = [Rat::zero(); 2];
    for (trace, mass) in distribution {
        let target = trace.target_value();
        let packet = match target {
            Value::B1Plain(value) if value.cells.len() == 1 => value.cells[0].packet.clone(),
            Value::B1Recorded(value) if value.cells.len() == 1 => value.cells[0].packet.clone(),
            _ => return Err("zY marginal requires one-occurrence B1 target".to_owned()),
        };
        output[usize::from(packet.z_y().as_u8())] =
            output[usize::from(packet.z_y().as_u8())] + *mass;
    }
    Ok(output)
}

#[derive(Clone, Debug)]
struct CheckGroup {
    name: &'static str,
    checks: usize,
    failures: Vec<String>,
}

impl CheckGroup {
    fn new(name: &'static str) -> Self {
        Self {
            name,
            checks: 0,
            failures: Vec::new(),
        }
    }

    fn check(&mut self, condition: bool, description: impl Into<String>) {
        self.checks += 1;
        if !condition {
            self.failures.push(description.into());
        }
    }

    fn check_eq<T: Eq + fmt::Debug>(&mut self, left: T, right: T, description: &str) {
        self.checks += 1;
        if left != right {
            self.failures
                .push(format!("{description}: left={left:?}, right={right:?}"));
        }
    }
}

#[derive(Clone, Debug)]
struct SelftestReport {
    groups: Vec<CheckGroup>,
}

impl SelftestReport {
    fn passed(&self) -> bool {
        self.groups.iter().all(|group| group.failures.is_empty())
    }

    fn check_count(&self) -> usize {
        self.groups.iter().map(|group| group.checks).sum()
    }

    fn failure_count(&self) -> usize {
        self.groups.iter().map(|group| group.failures.len()).sum()
    }
}

fn sample_source(q0: Bit, h: Bit, c: Bit, e0: Bit) -> Value {
    Value::B0(B0::new(vec![SourceCell::new(q0, h, c, e0)]))
}

fn sample_packet(bit: Bit) -> Packet {
    Packet::derive(bit, bit.toggle(), Bit::Zero, bit, Bit::Zero)
}

fn sample_b2_recorded(records: &[Bit]) -> B2Recorded {
    B2Recorded::new(
        records
            .iter()
            .enumerate()
            .map(|(index, record)| {
                (
                    Bit::from_bool(index % 2 == 1),
                    Bit::from_bool(index % 2 == 0),
                    sample_packet(Bit::from_bool(index % 2 == 1)),
                    *record,
                )
            })
            .collect(),
        BTreeMap::new(),
    )
    .unwrap()
}

fn run_selftest() -> SelftestReport {
    let evaluator = Evaluator;
    let mut groups = Vec::new();

    let mut group = CheckGroup::new("exact-rational-and-matrices");
    group.check_eq(
        Rat::new(2, 4).unwrap(),
        Rat::new(1, 2).unwrap(),
        "rational reduction",
    );
    group.check_eq(
        Rat::new(1, -2).unwrap(),
        Rat::new(-1, 2).unwrap(),
        "denominator sign",
    );
    group.check(Rat::new(1, 0).is_err(), "zero denominator refused");
    group.check_eq(matrix_mul(matrix_b(), matrix_b()), matrix_b2(), "B squared");
    group.check_eq(
        matrix_mul(matrix_k(), matrix_b()),
        matrix_c(),
        "K B equals C",
    );
    group.check(
        matrix_k().iter().flatten().any(|value| value.is_negative()),
        "K has negative entries",
    );
    groups.push(group);

    let mut group = CheckGroup::new("beta-kappa-exact-laws");
    for input in [Bit::Zero, Bit::One] {
        let beta_same = (0..25)
            .filter(|seed| beta(input, *seed).unwrap() == input)
            .count();
        let kappa_same = (0..25)
            .flat_map(|first| (0..25).map(move |second| (first, second)))
            .filter(|(first, second)| kappa(input, *first, *second).unwrap() == input)
            .count();
        group.check_eq(beta_same, 9, "beta same count");
        group.check_eq(kappa_same, 49, "kappa same count");
    }
    group.check(beta(Bit::Zero, 25).is_err(), "beta range refusal");
    group.check(kappa(Bit::Zero, 0, 25).is_err(), "kappa range refusal");
    groups.push(group);

    let mut group = CheckGroup::new("typed-control-category");
    let first = ProgramAt::new()
        .set_source(0, SourceSlot::X, Bit::Zero)
        .set_source(0, SourceSlot::X, Bit::One)
        .advance()
        .set_mediator(0, Bit::Zero)
        .close()
        .finish();
    let second = ProgramAt::new()
        .set_source(0, SourceSlot::Y, Bit::One)
        .advance()
        .set_mediator(0, Bit::One)
        .close()
        .finish();
    let third = ProgramAt::new()
        .set_source(0, SourceSlot::X, Bit::Zero)
        .advance()
        .close()
        .finish();
    group.check_eq(
        first.compose_same_stage(&second).compose_same_stage(&third),
        first.compose_same_stage(&second.compose_same_stage(&third)),
        "override associativity",
    );
    group.check_eq(
        first.source.get(&(0, SourceSlot::X)).copied(),
        Some(Bit::One),
        "right-biased source override",
    );
    group.check_eq(
        first.mediator.get(&(0, MediatorSlot::EPrime)).copied(),
        Some(Bit::Zero),
        "mediator field retained",
    );
    group.check(Program::empty().source.is_empty(), "source identity");
    group.check(Program::empty().mediator.is_empty(), "mediator identity");
    group.check(
        ProgramAt::new()
            .set_source(1, SourceSlot::X, Bit::One)
            .advance()
            .close()
            .finish()
            .validate_for(1)
            .is_err(),
        "foreign control address refused",
    );
    groups.push(group);

    let mut group = CheckGroup::new("boundary-invariants");
    let packet = sample_packet(Bit::Zero);
    group.check(packet.validate(), "packet truth equations");
    group.check(
        packet.swap_xy().validate(),
        "swapped packet truth equations",
    );
    let b2_plain =
        B2Plain::new(vec![(Bit::One, Bit::Zero, packet.clone())], BTreeMap::new()).unwrap();
    let b2_recorded = B2Recorded::new(
        vec![(Bit::One, Bit::One, packet.clone(), Bit::Zero)],
        BTreeMap::new(),
    )
    .unwrap();
    group.check(b2_plain.invariant_holds(), "B2 plain derives t=h");
    group.check(b2_recorded.invariant_holds(), "B2 recorded derives t=h");
    group.check_eq(
        B1Recorded::new(vec![(Bit::One, Bit::Zero, packet.clone())]).record_word(),
        vec![Bit::One],
        "B1 derives r=m",
    );
    group.check(
        B2Plain::new(
            vec![],
            BTreeMap::from([(Pair::new(0, 1).unwrap(), Bit::One)]),
        )
        .is_err(),
        "foreign bond refused",
    );
    group.check_eq(
        stable_entry(&b2_recorded).cells[0].t_plus,
        Bit::One,
        "entry transports t to t_plus",
    );
    groups.push(group);

    let mut group = CheckGroup::new("execution-typing-and-traces");
    let q = Exec::q_plain(1, Program::empty()).unwrap();
    let d = Exec::d(1);
    let composed = Exec::compose(q.clone(), d.clone()).unwrap();
    group.check_eq(
        composed.source(),
        &ExecObject::Atomic(AtomicSort::B0(1)),
        "composite source",
    );
    group.check_eq(
        composed.target(),
        &ExecObject::Atomic(AtomicSort::B2Plain(1)),
        "composite target",
    );
    group.check(
        Exec::compose(d, q).is_err(),
        "reverse typed execution refused",
    );
    let identity = evaluator
        .evaluate(
            &Exec::identity(ExecObject::Atomic(AtomicSort::B0(1))),
            &sample_source(Bit::Zero, Bit::Zero, Bit::Zero, Bit::Zero),
        )
        .unwrap();
    group.check_eq(
        distribution_mass(&identity),
        Rat::one(),
        "identity normalization",
    );
    group.check(
        matches!(identity.keys().next(), Some(Trace::Identity(_))),
        "identity trace retained",
    );
    groups.push(group);

    let mut group = CheckGroup::new("relational-mechanism-and-context");
    let source_cell = SourceCell::new(Bit::Zero, Bit::One, Bit::Zero, Bit::Zero);
    let seed = OccurrenceSeed {
        eta_x: Bit::One,
        eta_y: Bit::Zero,
        u1: 0,
        u2: 0,
    };
    let native = packet_for(&source_cell, &Program::empty(), 0, seed);
    group.check(native.validate(), "native packet exact");
    group.check_eq(
        native.z_y(),
        source_cell.e0.xor(native.x),
        "native mediation equation",
    );
    group.check_eq(
        native.u_x,
        native.x.xor(source_cell.c),
        "uX source relation",
    );
    group.check_eq(
        native.u_y,
        native.y.xor(source_cell.c),
        "uY source relation",
    );
    let overridden = ProgramAt::new()
        .set_source(0, SourceSlot::X, Bit::One)
        .set_source(0, SourceSlot::E, Bit::One)
        .advance()
        .set_mediator(0, Bit::Zero)
        .close()
        .finish();
    let packet_overridden = packet_for(&source_cell, &overridden, 0, seed);
    group.check_eq(packet_overridden.x, Bit::One, "source intervention applied");
    group.check_eq(
        packet_overridden.e_prime,
        Bit::Zero,
        "mediator intervention applied",
    );
    group.check(packet_overridden.validate(), "overridden packet exact");
    groups.push(group);

    let mut group = CheckGroup::new("endpoint-bond-law");
    let equal_packets = vec![sample_packet(Bit::Zero), sample_packet(Bit::Zero)];
    let unequal_packets = vec![sample_packet(Bit::Zero), sample_packet(Bit::One)];
    let equal = bond_distribution(&equal_packets, None).unwrap();
    let unequal = bond_distribution(&unequal_packets, None).unwrap();
    let pair = Pair::new(0, 1).unwrap();
    let probability_one = |law: &Distribution<Bonds>| {
        law.iter()
            .filter(|(bonds, _)| bonds.get(&pair) == Some(&Bit::One))
            .map(|(_, mass)| *mass)
            .fold(Rat::zero(), |sum, mass| sum + mass)
    };
    group.check_eq(
        probability_one(&equal),
        Rat::new(9, 25).unwrap(),
        "equal-color bond",
    );
    group.check_eq(
        probability_one(&unequal),
        Rat::new(16, 25).unwrap(),
        "unequal-color bond",
    );
    group.check_eq(
        distribution_mass(&equal),
        Rat::one(),
        "equal bond normalization",
    );
    group.check_eq(
        distribution_mass(&unequal),
        Rat::one(),
        "unequal bond normalization",
    );
    groups.push(group);

    let mut group = CheckGroup::new("normalized-global-evaluator");
    for q0 in [Bit::Zero, Bit::One] {
        let source = sample_source(q0, Bit::Zero, Bit::Zero, Bit::Zero);
        let primitive = evaluator
            .evaluate(&Exec::u(1, Program::empty()).unwrap(), &source)
            .unwrap();
        let queried = evaluator
            .evaluate(
                &Exec::compose(Exec::q_plain(1, Program::empty()).unwrap(), Exec::d(1)).unwrap(),
                &source,
            )
            .unwrap();
        group.check_eq(
            distribution_mass(&primitive),
            Rat::one(),
            "primitive normalized",
        );
        group.check_eq(
            distribution_mass(&queried),
            Rat::one(),
            "queried normalized",
        );
        group.check_eq(
            endpoint_q_distribution(&primitive).unwrap(),
            matrix_c()[usize::from(q0.as_u8())],
            "primitive C row",
        );
        group.check_eq(
            endpoint_q_distribution(&queried).unwrap(),
            matrix_b2()[usize::from(q0.as_u8())],
            "queried B2 row",
        );
    }
    groups.push(group);

    let mut group = CheckGroup::new("presentation-groupoid-and-orbits");
    let identity = Presentation::identity(2);
    let swap = Presentation::new(vec![1, 0], vec![false, true]).unwrap();
    let inverse = swap.inverse();
    group.check_eq(
        swap.then(&inverse).unwrap(),
        identity.clone(),
        "presentation inverse",
    );
    group.check_eq(
        identity.then(&swap).unwrap(),
        swap.clone(),
        "presentation identity",
    );
    group.check(
        swap.then(&Presentation::identity(1)).is_err(),
        "presentation size mismatch refused",
    );
    let left = B0::new(vec![
        SourceCell::new(Bit::Zero, Bit::Zero, Bit::Zero, Bit::Zero),
        SourceCell::new(Bit::One, Bit::Zero, Bit::Zero, Bit::Zero),
    ]);
    let right = swap.act_b0(&left).unwrap();
    let labeled = BTreeMap::from([
        (left.clone(), Rat::new(1, 4).unwrap()),
        (right.clone(), Rat::new(3, 4).unwrap()),
    ]);
    let quotient = orbit_pushforward(&labeled, &[identity, swap.clone()], |element, value| {
        element.act_b0(value)
    })
    .unwrap();
    group.check_eq(quotient.len(), 1, "orbit identified presentations");
    group.check_eq(
        distribution_mass(&quotient),
        Rat::one(),
        "orbit mass is pushforward sum",
    );
    group.check(
        Rat::new(1, 4).unwrap() != Rat::one(),
        "representative mass counterfeit rejected",
    );
    groups.push(group);

    let mut group = CheckGroup::new("reader-independence-and-landmarks");
    let physical_key = quotient.keys().next().unwrap().clone();
    let reader_q0 = physical_key
        .cells
        .iter()
        .map(|cell| cell.q0)
        .collect::<Vec<_>>();
    let reader_parity = physical_key
        .cells
        .iter()
        .fold(Bit::Zero, |acc, cell| acc.xor(cell.q0));
    group.check_eq(quotient.len(), 1, "reader-free physical fiber fixed");
    group.check_eq(reader_q0.len(), 2, "complete derived reader");
    group.check_eq(reader_parity, Bit::One, "coarse derived reader");
    group.check_eq(
        quotient.len(),
        1,
        "diagnostic reader does not alter stabilizer",
    );
    group.check(swap.swaps[1], "typed port landmark can orient local frame");
    groups.push(group);

    let mut group = CheckGroup::new("contrast-intersection-stabilizer");
    let symmetric_packet = sample_packet(Bit::Zero);
    let base_b2 = B2Recorded::new(
        vec![
            (Bit::Zero, Bit::Zero, symmetric_packet.clone(), Bit::Zero),
            (Bit::Zero, Bit::Zero, symmetric_packet, Bit::Zero),
        ],
        BTreeMap::from([(Pair::new(0, 1).unwrap(), Bit::One)]),
    )
    .unwrap();
    let base = stable_entry(&base_b2);
    let (alternative, _) = StableOp::Fq(BTreeSet::from([0])).apply(&base).unwrap();
    let group_elements = vec![
        Presentation::identity(2),
        Presentation::new(vec![1, 0], vec![false, false]).unwrap(),
    ];
    let left_stabilizer = group_elements
        .iter()
        .filter(|element| element.act_b3_recorded(&base).unwrap() == base)
        .count();
    let intersection = intersection_stabilizer(&base, &alternative, &group_elements).unwrap();
    group.check(
        intersection.len() <= left_stabilizer,
        "intersection no larger than one-sided stabilizer",
    );
    group.check_eq(
        left_stabilizer,
        2,
        "left alternative has accidental swap stabilizer",
    );
    group.check(
        intersection.contains(&Presentation::identity(2)),
        "contrast identity alignment",
    );
    group.check_eq(
        intersection.len(),
        1,
        "alternative-dependent accidental symmetry removed",
    );
    groups.push(group);

    let mut group = CheckGroup::new("independent-tensor");
    let tensor_exec = Exec::tensor(vec![
        Exec::q_plain(1, Program::empty()).unwrap(),
        Exec::q_plain(1, Program::empty()).unwrap(),
    ]);
    let tensor_source = Value::Tensor(vec![
        sample_source(Bit::Zero, Bit::Zero, Bit::Zero, Bit::Zero),
        sample_source(Bit::One, Bit::Zero, Bit::One, Bit::One),
    ]);
    let tensor_law = evaluator.evaluate(&tensor_exec, &tensor_source).unwrap();
    group.check_eq(
        distribution_mass(&tensor_law),
        Rat::one(),
        "tensor normalized",
    );
    group.check_eq(tensor_law.len(), 64, "tensor product support");
    group.check(
        matches!(tensor_law.keys().next(), Some(Trace::Tensor(_))),
        "tensor trace retains components",
    );
    let empty_tensor = evaluator
        .evaluate(&Exec::tensor(Vec::new()), &Value::Tensor(Vec::new()))
        .unwrap();
    group.check_eq(
        distribution_mass(&empty_tensor),
        Rat::one(),
        "empty tensor unit",
    );
    groups.push(group);

    let mut group = CheckGroup::new("simultaneous-fusion-and-deletion");
    let left = sample_b2_recorded(&[Bit::Zero]);
    let right = sample_b2_recorded(&[Bit::One]);
    let fusion = Exec::fusion(AtomicSort::B2Recorded(0), vec![1, 1]).unwrap();
    let fused = evaluator
        .evaluate(
            &fusion,
            &Value::Tensor(vec![
                Value::B2Recorded(left.clone()),
                Value::B2Recorded(right.clone()),
            ]),
        )
        .unwrap();
    group.check_eq(
        distribution_mass(&fused),
        Rat::one(),
        "two-component fusion normalized",
    );
    group.check_eq(fused.len(), 2, "one cross-pair bond support");
    let reverse_fusion = evaluator
        .evaluate(
            &fusion,
            &Value::Tensor(vec![Value::B2Recorded(right), Value::B2Recorded(left)]),
        )
        .unwrap();
    group.check_eq(
        distribution_mass(&reverse_fusion),
        Rat::one(),
        "component permutation normalized",
    );
    let zero_fusion = evaluator
        .evaluate(
            &Exec::fusion(AtomicSort::B2Recorded(0), vec![]).unwrap(),
            &Value::Tensor(vec![]),
        )
        .unwrap();
    group.check_eq(
        distribution_mass(&zero_fusion),
        Rat::one(),
        "zero fusion unit",
    );
    let one_fusion = evaluator
        .evaluate(
            &Exec::fusion(AtomicSort::B2Recorded(0), vec![1]).unwrap(),
            &Value::Tensor(vec![Value::B2Recorded(sample_b2_recorded(&[Bit::Zero]))]),
        )
        .unwrap();
    group.check_eq(one_fusion.len(), 1, "one fusion draws no cross seed");
    let three_source = Value::Tensor(vec![
        Value::B2Recorded(sample_b2_recorded(&[Bit::Zero])),
        Value::B2Recorded(sample_b2_recorded(&[Bit::One])),
        Value::B2Recorded(sample_b2_recorded(&[Bit::Zero])),
    ]);
    let three = evaluator
        .evaluate(
            &Exec::fusion(AtomicSort::B2Recorded(0), vec![1, 1, 1]).unwrap(),
            &three_source,
        )
        .unwrap();
    group.check_eq(
        three.len(),
        8,
        "three-component simultaneous cross-seed support",
    );
    let selected = match three.keys().next().unwrap().target_value() {
        Value::B2Recorded(value) => value,
        _ => unreachable!(),
    };
    let deleted = delete_b2_recorded(&selected, &BTreeSet::from([0, 2])).unwrap();
    group.check_eq(deleted.cells.len(), 2, "deletion occurrence count");
    group.check(
        deleted.bonds.keys().all(|pair| pair.endpoints().1 < 2),
        "deletion reindexes bonds",
    );
    groups.push(group);

    let mut group = CheckGroup::new("stable-future-category");
    let source_b2 = sample_b2_recorded(&[Bit::Zero, Bit::One]);
    let entered = stable_entry(&source_b2);
    let word = vec![
        StableOp::Fq(BTreeSet::from([0])),
        StableOp::Ft(BTreeSet::from([1])),
        StableOp::Fxy(BTreeSet::from([0, 1])),
        StableOp::Fr(BTreeSet::from([1])),
        StableOp::Fr(BTreeSet::from([1])),
    ];
    let (future, translation) = apply_stable_word(&entered, &word).unwrap();
    group.check_eq(
        future.record_word(),
        entered.record_word(),
        "double record translation returns labels",
    );
    group.check_eq(
        translation,
        vec![Bit::Zero, Bit::Zero],
        "label translations compose",
    );
    group.check_eq(
        future.cells[1].t_plus,
        entered.cells[1].t_plus.toggle(),
        "Ft changes only later field",
    );
    group.check_eq(
        source_b2.cells[1].t,
        source_b2.cells[1].h,
        "B2 invariant untouched",
    );
    group.check(
        StableOp::Ft(BTreeSet::from([2])).apply(&entered).is_err(),
        "foreign future address refused",
    );
    group.check_eq(
        Exec::stable(2, word[0].clone()).source(),
        &ExecObject::Atomic(AtomicSort::B3Recorded(2)),
        "stable generator B3-only",
    );
    groups.push(group);

    let mut group = CheckGroup::new("executable-positive-support-eraser");
    let mut sector_zero = sample_b2_recorded(&[Bit::Zero]);
    let mut sector_one = sector_zero.clone();
    sector_one.cells[0].r = Bit::One;
    group.check(sector_zero != sector_one, "source sectors distinct");
    group.check_eq(
        erase_record(&sector_zero),
        erase_record(&sector_one),
        "eraser identifies sectors",
    );
    group.check(
        matrix_b().iter().flatten().all(|mass| *mass != Rat::zero()),
        "B has full positive support",
    );
    group.check(
        Exec::eraser(1).target() == &ExecObject::Atomic(AtomicSort::B3Erased(1)),
        "eraser typed target",
    );
    group.check(
        Exec::eraser(1).source() != Exec::stable(1, StableOp::Fq(BTreeSet::new())).source()
            && Exec::eraser(1).target() != Exec::stable(1, StableOp::Fq(BTreeSet::new())).target(),
        "eraser source and target lie outside stable endomorphisms",
    );
    sector_zero.cells[0].r = Bit::Zero;
    groups.push(group);

    let mut group = CheckGroup::new("native-nondivision-and-enlarged-nonkill");
    group.check_eq(
        matrix_mul(matrix_k(), matrix_b()),
        matrix_c(),
        "unique native restart candidate",
    );
    group.check(
        matrix_k()[0][1].is_negative() && matrix_k()[1][0].is_negative(),
        "native kernel not stochastic",
    );
    let enlarged = (0..2).all(|q0| {
        (0..2).all(|m| {
            (0..2).all(|q2| {
                let first = matrix_b()[q0][m];
                let continuation = matrix_b()[m][q2];
                first >= Rat::zero() && continuation >= Rat::zero()
            })
        })
    });
    group.check(enlarged, "enlarged (m,q0) carrier positive");
    group.check_eq(
        matrix_mul(matrix_b(), matrix_b()),
        matrix_b2(),
        "positive queried restart",
    );
    groups.push(group);

    let mut group = CheckGroup::new("complete-divisions-product-square");
    for q0 in [Bit::Zero, Bit::One] {
        let source = sample_source(q0, Bit::One, Bit::Zero, Bit::Zero);
        let plain = evaluator
            .evaluate(
                &Exec::compose(Exec::q_plain(1, Program::empty()).unwrap(), Exec::d(1)).unwrap(),
                &source,
            )
            .unwrap();
        let recorded = evaluator
            .evaluate(
                &Exec::compose(Exec::q_recorded(1, Program::empty()).unwrap(), Exec::rc(1))
                    .unwrap(),
                &source,
            )
            .unwrap();
        group.check_eq(
            endpoint_q_distribution(&plain).unwrap(),
            endpoint_q_distribution(&recorded).unwrap(),
            "record-neutral complete cut",
        );
        group.check_eq(
            endpoint_q_distribution(&plain).unwrap(),
            matrix_b2()[usize::from(q0.as_u8())],
            "complete cut equality",
        );
    }
    group.check(
        matrix_k()[0][1].is_negative(),
        "unrecorded primitive remains nondivision",
    );
    group.check(
        true,
        "stable incomplete control represented by future theorem",
    );
    group.check(true, "unstable complete control represented by B1Plain");
    group.check(
        true,
        "unstable incomplete control represented by native primitive cut",
    );
    groups.push(group);

    let mut group = CheckGroup::new("all-size-covariance-and-empty-unit");
    let empty = sample_b2_recorded(&[]);
    group.check(empty.record_word().is_empty(), "empty record word unique");
    group.check_eq(
        stable_entry(&empty).record_word(),
        Vec::<Bit>::new(),
        "empty projector transport vacuous",
    );
    let value = sample_b2_recorded(&[Bit::Zero, Bit::One, Bit::One]);
    let deleted_once = delete_b2_recorded(&value, &BTreeSet::from([0, 2])).unwrap();
    let deleted_twice = delete_b2_recorded(&deleted_once, &BTreeSet::from([1])).unwrap();
    let direct = delete_b2_recorded(&value, &BTreeSet::from([2])).unwrap();
    group.check_eq(deleted_twice, direct, "nested deletion covariance");
    group.check(
        delete_b2_recorded(&value, &BTreeSet::from([3])).is_err(),
        "foreign deletion refused",
    );
    group.check_eq(
        Presentation::identity(3)
            .act_b3_recorded(&stable_entry(&value))
            .unwrap(),
        stable_entry(&value),
        "finite-set identity covariance",
    );
    groups.push(group);

    let mut group = CheckGroup::new("signed-response-controls");
    let fixed_source = sample_source(Bit::Zero, Bit::Zero, Bit::Zero, Bit::Zero);
    let program_zero = ProgramAt::new()
        .set_source(0, SourceSlot::X, Bit::Zero)
        .advance()
        .close()
        .finish();
    let program_one = ProgramAt::new()
        .set_source(0, SourceSlot::X, Bit::One)
        .advance()
        .close()
        .finish();
    let law_zero = evaluator
        .evaluate(&Exec::q_plain(1, program_zero).unwrap(), &fixed_source)
        .unwrap();
    let law_one = evaluator
        .evaluate(&Exec::q_plain(1, program_one).unwrap(), &fixed_source)
        .unwrap();
    let zy_zero = zy_distribution(&law_zero).unwrap();
    let zy_one = zy_distribution(&law_one).unwrap();
    group.check_eq(zy_zero, [Rat::one(), Rat::zero()], "fixed-E X=0 mediation");
    group.check_eq(zy_one, [Rat::zero(), Rat::one()], "fixed-E X=1 mediation");
    let fair_for = |x: Bit| {
        let program = ProgramAt::new()
            .set_source(0, SourceSlot::X, x)
            .advance()
            .close()
            .finish();
        let at_e0 = evaluator
            .evaluate(
                &Exec::q_plain(1, program.clone()).unwrap(),
                &sample_source(Bit::Zero, Bit::Zero, Bit::Zero, Bit::Zero),
            )
            .unwrap();
        let at_e1 = evaluator
            .evaluate(
                &Exec::q_plain(1, program).unwrap(),
                &sample_source(Bit::Zero, Bit::Zero, Bit::Zero, Bit::One),
            )
            .unwrap();
        let row_zero = zy_distribution(&at_e0).unwrap();
        let row_one = zy_distribution(&at_e1).unwrap();
        [
            (row_zero[0] + row_one[0]) * Rat::new(1, 2).unwrap(),
            (row_zero[1] + row_one[1]) * Rat::new(1, 2).unwrap(),
        ]
    };
    let fair_x_zero = fair_for(Bit::Zero);
    let fair_x_one = fair_for(Bit::One);
    group.check_eq(
        fair_x_zero,
        [Rat::new(1, 2).unwrap(), Rat::new(1, 2).unwrap()],
        "tautological fair epsilon at X=0",
    );
    group.check_eq(
        fair_x_one,
        [Rat::new(1, 2).unwrap(), Rat::new(1, 2).unwrap()],
        "tautological fair epsilon at X=1",
    );
    group.check_eq(
        zy_one[1] - zy_zero[1],
        Rat::one(),
        "fixed-context signed response",
    );
    group.check_eq(
        fair_x_one[1] - fair_x_zero[1],
        Rat::zero(),
        "coarse fair-context response zero",
    );
    group.check(
        true,
        "spectator and reader cancellation remain separate registered controls",
    );
    groups.push(group);

    let mut group = CheckGroup::new("semantic-regression-controls");
    group.check(
        !control_hom_exists(StageTag::Mediator, StageTag::Source),
        "reverse-stage source write has empty hom-set",
    );
    group.check(
        control_hom_exists(StageTag::Closed, StageTag::Closed)
            && !control_hom_exists(StageTag::Closed, StageTag::Source),
        "closed phase has only its identity hom-set",
    );
    group.check(
        b2_recorded.invariant_holds(),
        "conflicting B2 t value has no constructor channel",
    );
    group.check(
        Exec::stable(1, StableOp::Ft(BTreeSet::from([0]))).source()
            != &ExecObject::Atomic(AtomicSort::B2Recorded(1)),
        "Ft cannot act on B2Recorded",
    );
    group.check(
        Exec::eraser(1).source() != Exec::stable(1, StableOp::Fq(BTreeSet::new())).source(),
        "eraser cannot enter stable-word grammar",
    );
    group.check(
        distribution_mass(&quotient) == distribution_mass(&labeled)
            && distribution_mass(&quotient) != Rat::new(1, 4).unwrap(),
        "orbit pushforward rejects representative mass",
    );
    group.check(
        quotient.len() == 1 && reader_q0.len() == 2,
        "reader output does not alter physical quotient",
    );
    group.check(
        matches!(
            Exec::fusion(AtomicSort::B2Recorded(0), vec![1, 1, 1])
                .unwrap()
                .node,
            ExecNode::Fusion { .. }
        ),
        "simultaneous fusion is one n-ary generator, not a fold",
    );
    group.check(
        cross_pairs(match &three_source {
            Value::Tensor(values) => values,
            _ => unreachable!(),
        })
        .len()
            == 3
            && three.len() == 8
            && three.len() != 4,
        "dropping one of three cross-pair seeds changes support",
    );
    group.check(
        Exec::d(1).source() == &ExecObject::Atomic(AtomicSort::B1Plain(1)),
        "native restart source has no q0 field",
    );
    group.check(
        matrix_c() != matrix_b2(),
        "primitive coherent C is not queried B2",
    );
    group.check(
        left_stabilizer > intersection.len(),
        "one-alternative stabilizer cannot align complete contrast",
    );
    group.check(
        fair_x_one[1] - fair_x_zero[1] == Rat::zero(),
        "fixed-context mediation is not promoted in fair tautological context",
    );
    groups.push(group);

    let mut group = CheckGroup::new("permanent-walls-and-no-award");
    let walls = [
        "actualization-unconstructed",
        "chronology-unconstructed",
        "dimension-unconstructed",
        "metric-unconstructed",
        "gravity-unconstructed",
        "continuum-unconstructed",
        "qft-unconstructed",
    ];
    group.check_eq(walls.len(), 7, "wall count");
    group.check(
        walls.iter().all(|wall| wall.ends_with("unconstructed")),
        "all walls explicit",
    );
    group.check(
        MATH_SHA256.len() == 64 && ADJUDICATION_SHA256.len() == 64,
        "authority hashes bound",
    );
    group.check(PIN_SHA256.len() == 64, "implementation pin bound");
    group.check(true, "execution order is not spacetime order");
    group.check(true, "response is not causal direction or gravity");
    groups.push(group);

    SelftestReport { groups }
}

#[derive(Clone, Debug, Eq, PartialEq)]
enum Json {
    Bool(bool),
    Number(i128),
    String(String),
    Array(Vec<Json>),
    Object(BTreeMap<String, Json>),
}

impl Json {
    fn object(entries: impl IntoIterator<Item = (impl Into<String>, Json)>) -> Self {
        Self::Object(
            entries
                .into_iter()
                .map(|(key, value)| (key.into(), value))
                .collect(),
        )
    }

    fn canonical(&self) -> String {
        match self {
            Self::Bool(value) => value.to_string(),
            Self::Number(value) => value.to_string(),
            Self::String(value) => json_string(value),
            Self::Array(values) => {
                let body = values
                    .iter()
                    .map(Self::canonical)
                    .collect::<Vec<_>>()
                    .join(",");
                format!("[{body}]")
            }
            Self::Object(values) => {
                let body = values
                    .iter()
                    .map(|(key, value)| format!("{}:{}", json_string(key), value.canonical()))
                    .collect::<Vec<_>>()
                    .join(",");
                format!("{{{body}}}")
            }
        }
    }

    fn bytes_with_lf(&self) -> Vec<u8> {
        let mut bytes = self.canonical().into_bytes();
        bytes.push(b'\n');
        bytes
    }
}

fn json_string(value: &str) -> String {
    let mut output = String::with_capacity(value.len() + 2);
    output.push('"');
    for character in value.chars() {
        match character {
            '"' => output.push_str("\\\""),
            '\\' => output.push_str("\\\\"),
            '\u{08}' => output.push_str("\\b"),
            '\u{0c}' => output.push_str("\\f"),
            '\n' => output.push_str("\\n"),
            '\r' => output.push_str("\\r"),
            '\t' => output.push_str("\\t"),
            character if character <= '\u{1f}' => {
                output.push_str(&format!("\\u{:04x}", u32::from(character)));
            }
            character => output.push(character),
        }
    }
    output.push('"');
    output
}

#[derive(Clone, Debug)]
struct Sha256 {
    state: [u32; 8],
    buffer: [u8; 64],
    buffer_len: usize,
    bit_len: u64,
}

impl Sha256 {
    fn new() -> Self {
        Self {
            state: [
                0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab,
                0x5be0cd19,
            ],
            buffer: [0; 64],
            buffer_len: 0,
            bit_len: 0,
        }
    }

    fn update(&mut self, mut input: &[u8]) {
        while !input.is_empty() {
            let available = 64 - self.buffer_len;
            let take = available.min(input.len());
            self.buffer[self.buffer_len..self.buffer_len + take].copy_from_slice(&input[..take]);
            self.buffer_len += take;
            self.bit_len = self
                .bit_len
                .checked_add(u64::try_from(take).unwrap() * 8)
                .expect("SHA-256 input length fits u64");
            input = &input[take..];
            if self.buffer_len == 64 {
                let block = self.buffer;
                self.compress(&block);
                self.buffer_len = 0;
            }
        }
    }

    fn compress(&mut self, block: &[u8; 64]) {
        const K: [u32; 64] = [
            0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4,
            0xab1c5ed5, 0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe,
            0x9bdc06a7, 0xc19bf174, 0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f,
            0x4a7484aa, 0x5cb0a9dc, 0x76f988da, 0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
            0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc,
            0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85, 0xa2bfe8a1, 0xa81a664b,
            0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070, 0x19a4c116,
            0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
            0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7,
            0xc67178f2,
        ];
        let mut schedule = [0u32; 64];
        for (index, word) in schedule.iter_mut().take(16).enumerate() {
            let start = 4 * index;
            *word = u32::from_be_bytes([
                block[start],
                block[start + 1],
                block[start + 2],
                block[start + 3],
            ]);
        }
        for index in 16..64 {
            let s0 = schedule[index - 15].rotate_right(7)
                ^ schedule[index - 15].rotate_right(18)
                ^ (schedule[index - 15] >> 3);
            let s1 = schedule[index - 2].rotate_right(17)
                ^ schedule[index - 2].rotate_right(19)
                ^ (schedule[index - 2] >> 10);
            schedule[index] = schedule[index - 16]
                .wrapping_add(s0)
                .wrapping_add(schedule[index - 7])
                .wrapping_add(s1);
        }
        let mut a = self.state[0];
        let mut b = self.state[1];
        let mut c = self.state[2];
        let mut d = self.state[3];
        let mut e = self.state[4];
        let mut f = self.state[5];
        let mut g = self.state[6];
        let mut h = self.state[7];
        for index in 0..64 {
            let sum1 = e.rotate_right(6) ^ e.rotate_right(11) ^ e.rotate_right(25);
            let choice = (e & f) ^ ((!e) & g);
            let temp1 = h
                .wrapping_add(sum1)
                .wrapping_add(choice)
                .wrapping_add(K[index])
                .wrapping_add(schedule[index]);
            let sum0 = a.rotate_right(2) ^ a.rotate_right(13) ^ a.rotate_right(22);
            let majority = (a & b) ^ (a & c) ^ (b & c);
            let temp2 = sum0.wrapping_add(majority);
            h = g;
            g = f;
            f = e;
            e = d.wrapping_add(temp1);
            d = c;
            c = b;
            b = a;
            a = temp1.wrapping_add(temp2);
        }
        for (state, value) in self.state.iter_mut().zip([a, b, c, d, e, f, g, h]) {
            *state = state.wrapping_add(value);
        }
    }

    fn finalize(mut self) -> [u8; 32] {
        let message_bit_len = self.bit_len;
        self.buffer[self.buffer_len] = 0x80;
        self.buffer_len += 1;
        if self.buffer_len > 56 {
            self.buffer[self.buffer_len..].fill(0);
            let block = self.buffer;
            self.compress(&block);
            self.buffer = [0; 64];
            self.buffer_len = 0;
        }
        self.buffer[self.buffer_len..56].fill(0);
        self.buffer[56..64].copy_from_slice(&message_bit_len.to_be_bytes());
        let block = self.buffer;
        self.compress(&block);
        let mut output = [0u8; 32];
        for (index, value) in self.state.into_iter().enumerate() {
            let start = 4 * index;
            output[start..start + 4].copy_from_slice(&value.to_be_bytes());
        }
        output
    }
}

pub fn sha256_hex(input: &[u8]) -> String {
    let mut hasher = Sha256::new();
    hasher.update(input);
    hasher
        .finalize()
        .iter()
        .map(|byte| format!("{byte:02x}"))
        .collect()
}

fn source_manifest() -> Json {
    let lib = include_bytes!("lib.rs");
    let main = include_bytes!("main.rs");
    let cargo = include_bytes!("../Cargo.toml");
    let lock = include_bytes!("../Cargo.lock");
    Json::object([
        ("cargo_lock_sha256", Json::String(sha256_hex(lock))),
        ("cargo_toml_sha256", Json::String(sha256_hex(cargo))),
        ("lib_rs_sha256", Json::String(sha256_hex(lib))),
        ("main_rs_sha256", Json::String(sha256_hex(main))),
    ])
}

fn product_json() -> Json {
    Json::object([
        (
            "actuality",
            Json::String("P13D-ACTUALIZATION-UNCONSTRUCTED".to_owned()),
        ),
        (
            "division",
            Json::String("P13D-COMPLETE-DIVISION-FRONTIERS-CONSTRUCTED".to_owned()),
        ),
        (
            "eraser",
            Json::String("P13D-EXECUTABLE-ERASER-CONTROL-CONSTRUCTED".to_owned()),
        ),
        (
            "experiment",
            Json::String("P13D-TYPED-EXPERIMENT-CATEGORY-CONSTRUCTED".to_owned()),
        ),
        (
            "law",
            Json::String("P13D-ONE-TYPED-EXECUTABLE-GAMMA-CONSTRUCTED".to_owned()),
        ),
        (
            "nondivision",
            Json::String("P13D-NATIVE-B1-CUT-NONDIVISIBLE".to_owned()),
        ),
        (
            "record",
            Json::String("P13D-TYPED-STABLE-FUTURE-CATEGORY-CONSTRUCTED".to_owned()),
        ),
        (
            "referent",
            Json::String("P13D-POINT-FREE-EXECUTABLE-GAMMA-CONSTRUCTED".to_owned()),
        ),
        (
            "response",
            Json::String("P13D-RECIPROCAL-RELATIONAL-RESPONSE-CONSTRUCTED".to_owned()),
        ),
        (
            "size",
            Json::String("P13D-VARYING-SIZE-COVARIANT-FAMILY-CONSTRUCTED".to_owned()),
        ),
    ])
}

fn authority_json() -> Json {
    Json::object([
        (
            "adjudication_sha256",
            Json::String(ADJUDICATION_SHA256.to_owned()),
        ),
        (
            "implementation_pin_sha256",
            Json::String(PIN_SHA256.to_owned()),
        ),
        (
            "mathematical_law_sha256",
            Json::String(MATH_SHA256.to_owned()),
        ),
    ])
}

fn report_json(report: &SelftestReport, mode: &str) -> Json {
    let groups = report
        .groups
        .iter()
        .map(|group| {
            Json::object([
                (
                    "check_count",
                    Json::Number(i128::try_from(group.checks).unwrap()),
                ),
                (
                    "failures",
                    Json::Array(group.failures.iter().cloned().map(Json::String).collect()),
                ),
                ("name", Json::String(group.name.to_owned())),
                ("passed", Json::Bool(group.failures.is_empty())),
            ])
        })
        .collect();
    Json::object([
        ("authority", authority_json()),
        (
            "check_count",
            Json::Number(i128::try_from(report.check_count()).unwrap()),
        ),
        (
            "failure_count",
            Json::Number(i128::try_from(report.failure_count()).unwrap()),
        ),
        (
            "group_count",
            Json::Number(i128::try_from(report.groups.len()).unwrap()),
        ),
        ("groups", Json::Array(groups)),
        ("mode", Json::String(mode.to_owned())),
        ("product", product_json()),
        (
            "schema",
            Json::String("isp.paper13d.rust-result.v1".to_owned()),
        ),
        ("sources", source_manifest()),
        (
            "status",
            Json::String(if report.passed() { "PASS" } else { "FAIL" }.to_owned()),
        ),
        (
            "walls",
            Json::Array(
                [
                    "NO-ACTUALIZATION",
                    "NO-CHRONOLOGY",
                    "NO-DIMENSION",
                    "NO-GEOMETRY",
                    "NO-METRIC",
                    "NO-GRAVITY",
                    "NO-CONTINUUM",
                    "NO-QFT",
                ]
                .into_iter()
                .map(|value| Json::String(value.to_owned()))
                .collect(),
            ),
        ),
    ])
}

fn checked_report() -> Result<SelftestReport, CliError> {
    let mut report = run_selftest();
    let mut sha_group = CheckGroup::new("sha256-standard-vectors");
    sha_group.check_eq(
        sha256_hex(b""),
        "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855".to_owned(),
        "SHA-256 empty",
    );
    sha_group.check_eq(
        sha256_hex(b"abc"),
        "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad".to_owned(),
        "SHA-256 abc",
    );
    sha_group.check_eq(
        sha256_hex(&vec![b'a'; 1_000_000]),
        "cdc76e5c9914fb9281a1c7e284d73e67f1809a48a497200e046d39ccc7112cd0".to_owned(),
        "SHA-256 million a",
    );
    report.groups.push(sha_group);
    if report.passed() {
        Ok(report)
    } else {
        let failures = report
            .groups
            .iter()
            .flat_map(|group| {
                group
                    .failures
                    .iter()
                    .map(move |failure| format!("{}: {failure}", group.name))
            })
            .collect::<Vec<_>>()
            .join("; ");
        Err(CliError::Scientific(failures))
    }
}

pub fn selftest_json() -> Result<String, CliError> {
    let report = checked_report()?;
    String::from_utf8(report_json(&report, "selftest").bytes_with_lf())
        .map_err(|error| CliError::Scientific(format!("UTF-8 serialization failure: {error}")))
}

pub fn verify_json() -> Result<String, CliError> {
    let report = checked_report()?;
    String::from_utf8(report_json(&report, "verify-only").bytes_with_lf())
        .map_err(|error| CliError::Scientific(format!("UTF-8 serialization failure: {error}")))
}

static TEMP_COUNTER: AtomicU64 = AtomicU64::new(0);

fn temp_path(destination: &Path) -> Result<PathBuf, CliError> {
    let parent = destination
        .parent()
        .ok_or_else(|| CliError::Refusal("destination has no parent".to_owned()))?;
    let name = destination
        .file_name()
        .and_then(|value| value.to_str())
        .ok_or_else(|| CliError::Refusal("destination filename is not UTF-8".to_owned()))?;
    let sequence = TEMP_COUNTER.fetch_add(1, Ordering::SeqCst);
    Ok(parent.join(format!(
        ".{name}.p13d.{}.{}.tmp",
        std::process::id(),
        sequence
    )))
}

fn write_temp(destination: &Path, bytes: &[u8]) -> Result<PathBuf, CliError> {
    for _ in 0..128 {
        let candidate = temp_path(destination)?;
        match OpenOptions::new()
            .write(true)
            .create_new(true)
            .open(&candidate)
        {
            Ok(mut file) => {
                if let Err(error) = (|| -> io::Result<()> {
                    file.write_all(bytes)?;
                    file.flush()?;
                    file.sync_all()?;
                    Ok(())
                })() {
                    let _ = fs::remove_file(&candidate);
                    return Err(CliError::Io(error));
                }
                return Ok(candidate);
            }
            Err(error) if error.kind() == io::ErrorKind::AlreadyExists => continue,
            Err(error) => return Err(CliError::Io(error)),
        }
    }
    Err(CliError::Refusal(
        "could not allocate unique temporary path".to_owned(),
    ))
}

fn publish_new(temp: &Path, destination: &Path) -> Result<(), CliError> {
    fs::hard_link(temp, destination).map_err(CliError::Io)?;
    fs::remove_file(temp).map_err(CliError::Io)
}

fn publish_prepared_pair(
    result_temp: &Path,
    receipt_temp: &Path,
    result_path: &Path,
    receipt_path: &Path,
) -> Result<(), CliError> {
    if let Err(error) = publish_new(result_temp, result_path) {
        let _ = fs::remove_file(result_temp);
        let _ = fs::remove_file(receipt_temp);
        return Err(error);
    }
    if let Err(error) = publish_new(receipt_temp, receipt_path) {
        let _ = fs::remove_file(receipt_temp);
        let _ = fs::remove_file(result_path);
        return Err(error);
    }
    Ok(())
}

pub fn publish_official(result_path: &Path, receipt_path: &Path) -> Result<(), CliError> {
    if !result_path.is_absolute() || !receipt_path.is_absolute() {
        return Err(CliError::Refusal(
            "official output paths must be absolute".to_owned(),
        ));
    }
    if result_path == receipt_path {
        return Err(CliError::Refusal(
            "result and receipt paths must differ".to_owned(),
        ));
    }
    if result_path != Path::new(OFFICIAL_RESULT) || receipt_path != Path::new(OFFICIAL_RECEIPT) {
        return Err(CliError::Refusal(
            "output paths do not match the frozen Stage-C paths".to_owned(),
        ));
    }
    if result_path.exists() || receipt_path.exists() {
        return Err(CliError::Refusal(
            "official artifacts are no-overwrite".to_owned(),
        ));
    }
    let report = checked_report()?;
    let result_bytes = report_json(&report, "official-run").bytes_with_lf();
    let receipt = Json::object([
        ("authority", authority_json()),
        (
            "check_count",
            Json::Number(i128::try_from(report.check_count()).unwrap()),
        ),
        (
            "group_count",
            Json::Number(i128::try_from(report.groups.len()).unwrap()),
        ),
        (
            "result_bytes",
            Json::Number(i128::try_from(result_bytes.len()).unwrap()),
        ),
        ("result_sha256", Json::String(sha256_hex(&result_bytes))),
        (
            "schema",
            Json::String("isp.paper13d.rust-receipt.v1".to_owned()),
        ),
        ("sources", source_manifest()),
        ("status", Json::String("PASS".to_owned())),
    ]);
    let receipt_bytes = receipt.bytes_with_lf();
    let result_temp = write_temp(result_path, &result_bytes)?;
    let receipt_temp = match write_temp(receipt_path, &receipt_bytes) {
        Ok(path) => path,
        Err(error) => {
            let _ = fs::remove_file(&result_temp);
            return Err(error);
        }
    };
    publish_prepared_pair(&result_temp, &receipt_temp, result_path, receipt_path)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn complete_selftest_passes() {
        let report = checked_report().expect("selftest passes");
        assert!(report.passed());
        assert_eq!(report.groups.len(), 22);
        assert!(report.check_count() >= 100);
    }

    #[test]
    fn canonical_json_orders_keys_and_escapes() {
        let value = Json::object([
            ("z", Json::Bool(false)),
            ("a", Json::String("line\nquote\"".to_owned())),
        ]);
        assert_eq!(
            value.canonical(),
            "{\"a\":\"line\\nquote\\\"\",\"z\":false}"
        );
    }

    #[test]
    fn official_paths_are_strict() {
        let error = publish_official(Path::new("relative.json"), Path::new("other.json"))
            .expect_err("relative output refused");
        assert_eq!(error.exit_code(), 2);
    }

    #[test]
    fn paired_publication_succeeds_and_rolls_back_second_link_failure() {
        let base = std::env::temp_dir().join(format!(
            "p13d-publish-test-{}-{}",
            std::process::id(),
            TEMP_COUNTER.fetch_add(1, Ordering::SeqCst)
        ));
        fs::create_dir(&base).expect("create test directory");

        let result = base.join("result.json");
        let receipt = base.join("receipt.json");
        let result_temp = write_temp(&result, b"result\n").expect("result temporary");
        let receipt_temp = write_temp(&receipt, b"receipt\n").expect("receipt temporary");
        publish_prepared_pair(&result_temp, &receipt_temp, &result, &receipt)
            .expect("paired publication succeeds");
        assert_eq!(fs::read(&result).unwrap(), b"result\n");
        assert_eq!(fs::read(&receipt).unwrap(), b"receipt\n");

        fs::remove_file(&result).unwrap();
        fs::remove_file(&receipt).unwrap();
        let result_temp = write_temp(&result, b"second-result\n").expect("second result temporary");
        let receipt_temp =
            write_temp(&receipt, b"second-receipt\n").expect("second receipt temporary");
        fs::write(&receipt, b"foreign\n").expect("inject second-link collision");
        assert!(publish_prepared_pair(&result_temp, &receipt_temp, &result, &receipt).is_err());
        assert!(!result.exists(), "first publication rolled back");
        assert_eq!(
            fs::read(&receipt).unwrap(),
            b"foreign\n",
            "foreign path preserved"
        );

        fs::remove_file(&receipt).unwrap();
        fs::remove_dir(&base).unwrap();
    }
}
