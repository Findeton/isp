use std::env;
use std::path::PathBuf;
use std::process::ExitCode;

use p13d_gamma::{publish_official, selftest_json, verify_json, CliError};

fn usage() -> &'static str {
    "USAGE: p13d-gamma --selftest | --verify-only | --run RESULT_PATH RECEIPT_PATH"
}

fn run() -> Result<(), CliError> {
    let args: Vec<String> = env::args().skip(1).collect();
    match args.as_slice() {
        [mode] if mode == "--selftest" => {
            print!("{}", selftest_json()?);
            Ok(())
        }
        [mode] if mode == "--verify-only" => {
            print!("{}", verify_json()?);
            Ok(())
        }
        [mode, result, receipt] if mode == "--run" => {
            publish_official(&PathBuf::from(result), &PathBuf::from(receipt))
        }
        _ => Err(CliError::Usage(usage().to_owned())),
    }
}

fn main() -> ExitCode {
    match run() {
        Ok(()) => ExitCode::SUCCESS,
        Err(error) => {
            eprintln!("{error}");
            ExitCode::from(error.exit_code())
        }
    }
}
