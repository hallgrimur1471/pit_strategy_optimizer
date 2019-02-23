#!/usr/bin/env python3.7

# Standard library
import argparse

# This project
import src.spreadsheet as spreadsheet
import src.optimizer as optimizer
from src.optimizer import Solution


def main():
    arguments = parse_command_line_arguments()
    racedata = arguments.RACEDATA
    if not racedata:
        racedata = fetch_url_from_config()
    (lap_times, extra_info) = spreadsheet.read_data(racedata)
    optimal_solution = optimizer.calculate_optimal_pit_stop_strategy(
        lap_times, extra_info, average_pit_time=arguments.average_pit_time, laps_in_race_override=arguments.laps_in_race
    )
    print_solution(optimal_solution)

def fetch_url_from_config():
    try:
        with open('config.cfg') as fd:
            for line in fd:
                return line.strip()
    except IOError:
        print("Error, you must specify the argument --racedata")
        exit(1)



def parse_command_line_arguments():
    parser = argparse.ArgumentParser()
    parser.description = (
        "Calculates optimal pit strategy based on RACEDATA. The results are "
        "printed to stdout as a human-readable text."
    )
    parser.add_argument(
        "--racedata-url",
        dest="RACEDATA",
        help=(
            "Link to a Google spreadsheet containing data about the race. "
            "To see how the spreadsheet should be set up take a look at "
            "this example: https://docs.google.com/spreadsheets/d/"
            "1P3fT81u8-2S7sSsx5KlRKCovWY10ZBDjImO-9myxo9U/edit?usp=sharing "
            "if this argument is not provided the url can also be set in a "
            "configuration file named config.cfg in the root of the project, "
            "the first line in the config file should be the url to the "
            "spreadsheet."
        ),
    )
    parser.add_argument("--average-pit-time", dest="average_pit_time", type=float)
    parser.add_argument("--laps-in-race", dest="laps_in_race", type=int)
    arguments = parser.parse_args()
    return arguments


def print_solution(solution):
    print(f"The best found solution is: {solution}")


if __name__ == "__main__":
    main()
