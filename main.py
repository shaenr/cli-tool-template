import sys
from argparse import Namespace
from pathlib import Path
from cli import get_argv, set_log_level
from constants import REQ_PY_VER


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
    context = {
        'log_level': set_log_level(argv),
        'input': argv.input,
        'output': argv.output
    }

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
    main(get_argv())



