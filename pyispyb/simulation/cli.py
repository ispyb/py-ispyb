import argparse
import logging

from .datacollection import SimulateDataCollection


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def run() -> None:
    try:
        sdc = SimulateDataCollection()
    except AttributeError as e:
        exit(f"Simulation Error: {e}")

    parser = argparse.ArgumentParser(description="ISPyB simulation tool")
    parser.add_argument(
        "beamline", help="Beamline to run simulation against", choices=sdc.beamlines
    )

    parser.add_argument(
        "experiment", help="Experiment to simluate", choices=sdc.experiment_types
    )

    parser.add_argument(
        "--delay",
        default=5,
        type=int,
        dest="delay",
        help="Delay between plugin start and end events",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug output",
    )

    args = parser.parse_args()

    root = logging.getLogger()
    root.setLevel(level=logging.DEBUG if args.debug else logging.INFO)

    try:
        sdc.do_run(args.beamline, args.experiment, delay=args.delay)
    except Exception as e:
        if args.debug:
            logger.exception("Simulation Error")
            print(e)
        else:
            print(f"Simulation Error: {e}")
