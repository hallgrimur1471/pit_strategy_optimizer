#!/usr/bin/env python3.7

# Standard library
import argparse

# This project
import src.spreadsheet as spreadsheet
import src.optimizer as optimizer
from src.optimizer import Solution


def main():
    arguments = parse_command_line_arguments()
    (lap_times, extra_info) = spreadsheet.read_data(arguments.RACEDATA)
    optimal_solution = optimizer.calculate_optimal_pit_stop_strategy(
        lap_times, extra_info
    )
    print_solution(optimal_solution)


def parse_command_line_arguments():
    parser = argparse.ArgumentParser()
    parser.description = (
        "Calculates optimal pit strategy based on RACEDATA. The results are "
        "printed to stdout as a human-readable text."
    )
    parser.add_argument(
        "RACEDATA",
        help=(
            "Link to a Google spreadhseet containing data about the race. "
            "To see how the spreadhseet should be set up take a look at "
            "this example: https://docs.google.com/spreadsheets/d/"
            "1P3fT81u8-2S7sSsx5KlRKCovWY10ZBDjImO-9myxo9U/edit?usp=sharing"
        ),
    )
    arguments = parser.parse_args()
    return arguments


def print_solution(solution):
    print(f"The best found solution is: {solution}")


if __name__ == "__main__":
    main()
