import argparse
import sys
import traceback
import signal
from turtle import st
from consoleffects import decorate


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    parsed_args = get_args(args)

    try:
        return decorate(parsed_args.text, bold=parsed_args.bold,
                        dim=parsed_args.dim, it=parsed_args.it,
                        uline=parsed_args.uline, blink=parsed_args.blink,
                        strike=parsed_args.strike, duline=parsed_args.duline)
    except KeyboardInterrupt:
        # Shell standard is 128 + signum = 130 (SIGINT = 2)
        sys.stdout.write("\n")
        return 128 + signal.SIGINT
    except Exception as e:
        # stderr and exit code 255
        sys.stderr.write("\n")
        sys.stderr.write(f"\033[91m{type(e).__name__}: {str(e)}\033[0;0m")
        sys.stderr.write("\n")
        # at this point, you're guaranteed to have args and thus log_level
        if parsed_args.log_level:
            if parsed_args.log_level < 10:
                # traceback prints to stderr by default
                traceback.print_exc()

        return 255


def get_args(args):
    """Parse arguments passed in from shell."""
    return get_parser().parse_args(args)


def get_parser():
    parser = argparse.ArgumentParser(description="Apply console effects")
    parser.add_argument('-b', '--bold', dest='bold',
                        action='store_true', help='Bold text')
    parser.add_argument('-d', '--dim', dest='dim',
                        action='store_true', help='Dim text')
    parser.add_argument('-i', '--italic', dest='it',
                        action='store_true', help='Italic text')
    parser.add_argument('-u', '--underline', dest='uline',
                        action='store_true', help='Underline text')
    parser.add_argument('-k', '--blink', dest='blink',
                        action='store_true', help='Blinking text')
    parser.add_argument('-s', '--strikethrough', dest='strike',
                        action='store_true', help='Strike-through text')
    parser.add_argument('-w', '--doubleunderline', dest='duline',
                        action='store_true', help='Double-underline text')

    parser.add_argument("text", type=str, help="Text")
    return parser
