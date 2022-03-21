import sys
import logging
from argparse import Namespace
from pathlib import Path
from cli import get_argv
from shaen_logger import slog
from shaen_logger.log import set_log_level
from constants import REQ_PY_VER


def get_log_level(ns: Namespace):
    return (ns.verbose - ns.quiet) * 10


def read_all_input_files(ns: Namespace,
                         read_in: str = ""):
    """Read in all infile data iteratively using helper generator"""
    for inp in _read_input_helper(ns):
        read_in += inp.read()
    return read_in


def _read_input_helper(ns: Namespace):
    """Iterate over input files."""
    for path in ns.input:
        if path == '-':
            yield sys.stdin
        else:
            yield Path(path).open('r', encoding='utf-8')


def main(argv: Namespace):
    set_log_level(get_log_level(argv))

    slog.info("=" * 20)
    slog.info("STARTING NEW EXECUTION...")
    slog.info("Running main.py")
    slog.info("=" * 20)
    slog.debug(f"slog: handlers={slog.handlers}, level={slog.level}")

    slog.info(f"Writing {argv.input} files to {argv.output}...")
    with argv.output as fo:
        fo.write(
            read_all_input_files(argv)
        )


if __name__ == '__main__':

    if sys.version_info < REQ_PY_VER:
        sys.stderr.write(
            f"Use python {REQ_PY_VER[0]}.{REQ_PY_VER[1]} or later to run this "
        )
        sys.exit(1)

    try:
        if isinstance(slog, logging.Logger):
            main(get_argv())
    except ValueError as e:
        print(f"There is a failure referencing slog from shaen_logger: {e}")
        sys.exit(1)



