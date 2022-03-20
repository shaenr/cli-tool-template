import sys
from argparse import (
    Namespace,
    FileType,
    ArgumentParser,
    RawDescriptionHelpFormatter
)
from pathlib import Path


def set_log_level(ns: Namespace):
    return ns.verbose - ns.quiet


def get_argv():
    parser = ArgumentParser(
        description=__doc__,
        formatter_class=RawDescriptionHelpFormatter
    )

    parser.add_argument('input',
                        nargs='*',
                        default=sys.stdin,
                        help="Optionally Read this File")

    verbosity_group = parser.add_mutually_exclusive_group(required=False)
    verbosity_group.add_argument("-v", "--verbose", default=1, action="count",
                                 help="increase logging level.")
    verbosity_group.add_argument("-q", "--quiet", default=0, action="count",
                                 help="decrease logging level.")

    parser.add_argument("--on", action="store_true",
                        help="include to enable")
    parser.add_argument("--off", action="store_false",
                        help="include to disable")

    parser.add_argument("-o", "--output",
                        type=FileType('w',
                                      encoding='utf-8'),
                        default=sys.stdout,
                        help="Output to a text file.")

    # parser.add_argument("positional_int", type=int,
    #                     help="req number")

    # group1 = parser.add_mutually_exclusive_group(required=True)
    # group1.add_argument('--enable', action="store_true")
    # group1.add_argument('--disable', action="store_false")

    return parser.parse_args()

