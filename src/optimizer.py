#!/usr/bin/env python3.7

# Standard library
from datetime import timedelta
from typing import Generator, Tuple, Dict, List, Any
from dataclasses import dataclass
from time import time
from time import sleep

# This project
import src.combinatorics as combinatorics


@dataclass
class Solution:
    pit_stop_laps: List[int]
    pit_tyre_choices: List[str]


def calculate_optimal_pit_stop_strategy(
    laptimes: Dict[str, timedelta], extra_info: Dict[str, Any]
) -> Tuple[Solution, int]:
    print("Generating possible solutions ...")
    possible_solutions = _generate_possible_solutions(
        extra_info["max_laps_per_tank"], extra_info["laps_in_race"]
    )
    # print(f"len(possible_solutions): {len([x for x in possible_solutions])}")
    print("Evaluating solutions ...")
    start_time = time()
    scores = map(_evaluate_solution, possible_solutions)
    pairs = zip(possible_solutions, scores)
    best_score = min(pairs, key=lambda p: p[1])
    print("Ealuating solutions took approx: {0:f} [s]".format(time() - start_time));
    return best_score


def _generate_possible_solutions(
    max_laps_per_tank: int, laps_in_race: int
) -> Generator[Solution, None, None]:
    lap_list = list(range(1, laps_in_race))
    max_pit_stops = 4

    possible_solutions = []
    for num_pit_stops in range(0, max_pit_stops + 1):
        for solution in _generate_solutions_with_num_pit_stops(
            laps_in_race, num_pit_stops
        ):
            possible_solutions.append(solution)
    print(f"len(possible_solutions): {len(possible_solutions)}")

    # filter because of fuel limit
    possible_solutions = list(
        filter(
            lambda solution: _does_not_run_out_of_fuel(
                solution, max_laps_per_tank, laps_in_race
            ),
            possible_solutions,
        )
    )
    print(f"len(possible_solutions): {len(possible_solutions)}")

    # filter out pit stops that are ridiculously close together
    possible_solutions = list(
        filter(_pit_stops_not_ridiculously_close_together, possible_solutions)
    )
    print(f"len(possible_solutions): {len(possible_solutions)}")

    for solution in possible_solutions:
        yield solution


def _generate_solutions_with_num_pit_stops(
    laps_in_race: int, num_pit_stops: int
) -> List[Solution]:
    lap_list = list(range(1, laps_in_race))
    pit_stop_laps_combinations = combinatorics.gen_k_combinations(
        lap_list, num_pit_stops
    )
    solutions = []
    for pit_stop_laps in pit_stop_laps_combinations:
        pit_tyre_choices_combinations = combinatorics.gen_k_multicombinations(
            ["RH", "RM", "RS"], num_pit_stops
        )
        for pit_tyre_choices in pit_tyre_choices_combinations:
            solutions.append(
                Solution(
                    pit_stop_laps=pit_stop_laps,
                    pit_tyre_choices=pit_tyre_choices,
                )
            )
    return solutions


def _does_not_run_out_of_fuel(solution, max_laps_per_tank, laps_in_race):
    lap_diffs = _calculate_lap_diffs(solution.pit_stop_laps)
    if max(lap_diffs) > max_laps_per_tank:
        return False
    return True
    # if not lap_diffs:
    #    return
    # pass


def _pit_stops_not_ridiculously_close_together(solution):
    lap_diffs = _calculate_lap_diffs(solution.pit_stop_laps)
    if min(lap_diffs) < 3:
        return False
    return True


def _calculate_lap_diffs(pit_stop_laps):
    v = pit_stop_laps
    v = [0] + v
    lap_diffs = [b - a for (a, b) in list(zip(v[::2], v[1::2]))]
    return lap_diffs


def _evaluate_solution(solution: Solution) -> int:
    return 1  # random score
