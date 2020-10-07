import logging
import sys
import argparse
# pylint: disable=import-error

from upstream_gen.server.entrypoint import configure_parser as server_parser
from upstream_gen.util.cli import *
from upstream_gen.__init__ import __version__
from upstream_gen.util.log import *
# # setting up custom trace debug level
LOGGER = logging.getLogger(__name__)
logging.addLevelName(logging.DEBUG - 5, 'TRACE')
addLoggingLevel('TRACE', logging.DEBUG - 5)


def main():
    log_levels = ['TRACE', 'DEBUG', 'INFO']
    parser = argparse.ArgumentParser(
        description='server/client utility for usage as a mock upstream')
    parser.add_argument(
        "-l",
        "--log",
        dest="logLevel",
        type=MakeCaseAgnostic(log_levels),
        choices=log_levels,
        help="Set the logging level (default Empty)")
    sub_parsers = parser.add_subparsers(
        title='Commands',
        description='Available Upstream Subcommands',
        help='Choose a upstream subcommand ')
    # adding subcommand parsers
    server_parser(sub_parsers)
    args = vars(parser.parse_args())
    if args:
        logLevel = args['logLevel']
        if logLevel:
            logging.basicConfig(
                format='%(asctime)s [%(threadName)-12.12s] [%(levelname)-8.8s]  %(message)s',
                stream=sys.stdout,
                level=getattr(logging, logLevel)
            )
        subcommand = args.pop('func', '')
        if subcommand:
            subcommand(args)

    else:
        parser.print_usage()

    LOGGER.debug(
        f"main() - "
        f"version={__version__} ")


if __name__ == "__main__":
    main()
