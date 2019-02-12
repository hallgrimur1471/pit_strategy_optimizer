#!/usr/bin/env python3.7

# Standard library
from datetime import timedelta
from typing import Generator, Tuple, Dict, List, Any
from dataclasses import dataclass

# This project
import src.combinatorics as combinatorics


@dataclass
class Solution:
    pit_stop_laps: List[int]
    pit_tyre_choices: List[str]


def calculate_optimal_pit_stop_strategy(
    laptimes: Dict[str, timedelta], extra_info: Dict[str, Any]
) -> Tuple[Solution, int]:
    possible_solutions = _generate_possible_solutions(
        extra_info["max_laps_per_tank"], extra_info["laps_in_race"]
    )
    scores = map(_evaluate_solution, possible_solutions)
    pairs = zip(possible_solutions, scores)
    return max(pairs, key=lambda p: p[1])


def _generate_possible_solutions(
    max_laps_per_tank, laps_in_race
) -> Generator[Solution, None, None]:
    lap_list = list(range(1, laps_in_race + 1))
    max_pit_stops = 5

    for num_pit_stops in range(0, max_pit_stops + 1):
        # _generate_solutions_with_num_pit_stops(laps_in_race, num_pit_stops)
        pit_stop_laps_combinations = combinatorics.gen_k_combinations(
            lap_list, num_pit_stops
        )
        for pit_stop_laps in pit_stop_laps_combinations:
            pit_tyre_choices_combs = combinatorics.gen_k_multicombinations(
                ["RH", "RM", "RS"], num_pit_stops
            )
            for pit_tyre_choices in pit_tyre_choices_combs:
                yield Solution(
                    pit_stop_laps=pit_stop_laps,
                    pit_tyre_choices=pit_tyre_choices,
                )

    #    for solution in _generate_n_choose_k_solutions(
    #        laps_in_race, num_pit_stops
    #    ):
    #        possible_solutions.append(solution)
    # print(f"len(possible_solutions): {len(possible_solutions)}")
    # possible_solutions = list(
    #    filter(does_not_run_out_of_fuel, possible_solutions)
    # )
    # pit_stop_solutions = _generate_n_choose_k_solutions(29, 5)
    # for solution in pit_stop_solutions:
    #    print(solution)
    # print(f"num_pit_stop_solutions: {len(pit_stop_solutions)}")

    for number in range(10):
        yield Solution(pit_stop_laps=[], pit_tyre_choices=[])


def does_not_run_out_of_fuel(pit_stop_solution):
    pass


def _evaluate_solution(solution: Solution) -> int:
    return 1  # random score
