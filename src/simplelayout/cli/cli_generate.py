import argparse
import sys


def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("--board_grid", type=int)
    parser.add_argument("--unit_grid", type=int)
    parser.add_argument("--unit_n", type=int)
    parser.add_argument("--positions", type=int, nargs="+")
    parser.add_argument("--outdir", type=str)
    parser.add_argument("--file_name", type=str)
    options = parser.parse_args()

    if options.board_grid % options.unit_grid != 0:
        sys.exit()

    upper_value = (options.board_grid / options.unit_grid)**2
    if len(options.positions) == options.unit_n:
        if min(options.positions) < 1 or max(options.positions) > upper_value:
            sys.exit()
    else:
        sys.exit()

    return options
