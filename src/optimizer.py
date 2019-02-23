#!/usr/bin/env python3.7

# Standard library
from datetime import timedelta
from typing import Generator, Tuple, Dict, List, Any
from dataclasses import dataclass
from time import time
from time import sleep
import pprint

# This project
import src.combinatorics as combinatorics


@dataclass
class Solution:
    pit_stop_laps: List[int]
    pit_tyre_choices: List[str]

    def __repr__(self):
        return str(self)

    def __str__(self):
        s = "Solution:"
        for lap_index, lap in enumerate(self.pit_stop_laps):
            if lap_index == 0:
                s = s + f" Start with {self.pit_tyre_choices[lap_index]} tyres. "
            else:
                s = (
                    s
                    + f" On lap nr. {self.pit_stop_laps[lap_index]} stop and use tyre type: {self.pit_tyre_choices[lap_index]}."
                )
        return s


def _add_cumulative_to_laptimes(laptimes):
    tyre_types = list(laptimes.keys())
    for tyre_type in tyre_types:
        cumulative_time_per_lap = []
        cumulative_time = 0
        for delta in laptimes[tyre_type]:
            cumulative_time += delta.total_seconds()
            cumulative_time_per_lap.append(cumulative_time)
        laptimes[tyre_type + "c"] = cumulative_time_per_lap
    return laptimes


def calculate_optimal_pit_stop_strategy(
    laptimes: Dict[str, timedelta], extra_info: Dict[str, Any]
) -> Tuple[Solution, int]:

    _add_cumulative_to_laptimes(laptimes)

    print("Data from extra info:")
    for key, value in extra_info.items():
        print(f"  {key}: {value}")

    print("laptimes: ")
    for tyre_type, deltas in sorted(laptimes.items()):
        print(f"{tyre_type}: ")
        i = 0
        for delta in deltas:
            s = ""
            lap_nr = i+1
            if isinstance(delta, timedelta):
                s = delta.total_seconds()
            else:
                s = delta
            print(f"{lap_nr:>2n}:{s:>7.1f}", end=" ")
            i += 1
            if i % 5 == 0:
                print()


    print("Generating possible solutions ...")

    laps_in_race = extra_info["laps_in_race"]
    average_pit_stop_time = extra_info["average_pit_time"]
    max_laps_per_tank = extra_info["max_laps_per_tank"]

    res = _does_not_run_out_of_fuel(
        Solution(pit_stop_laps=[3], pit_tyre_choices=["RH"]),
        max_laps_per_tank,
        laps_in_race,
    )
    ##print(f"res: {res}")

    # test solutions
    # test1 = Solution(pit_stop_laps= [5, 10, 20, 27], pit_tyre_choices= ['RH', 'RH', 'RS', 'RM'])
    # test1score = _evaluate_solution(test1, laps_in_race, average_pit_stop_time, laptimes)
    # return (test1, test1score)

    start_time = time()
    possible_solutions = _generate_possible_solutions(max_laps_per_tank, laps_in_race)
    generation_time = time() - start_time
    print(f"Generating possible solutions ... done in {generation_time} seconds")
    print("Evaluating solutions ...")
    start_time = time()
    scores = map(
        lambda s: _evaluate_solution(s, laps_in_race, average_pit_stop_time, laptimes),
        possible_solutions,
    )

    pairs = zip(possible_solutions, scores)
    best_score = min(pairs, key=lambda p: p[1])
    evaluation_time = time() - start_time
    print(f"Evaluating solutions ... done in {evaluation_time} seconds")
    return best_score


def _generate_possible_solutions(
    max_laps_per_tank: int, laps_in_race: int
) -> List[Solution]:
    lap_list = list(range(1, laps_in_race))
    max_pit_stops = 4

    possible_solutions = []
    for num_pit_stops in range(0, max_pit_stops + 1):
        for solution in _generate_solutions_with_num_pit_stops(
            laps_in_race, num_pit_stops
        ):
            possible_solutions.append(solution)

    number_of_possible_solutions = len(possible_solutions)

    # filter because of fuel limit
    possible_solutions = list(
        filter(
            lambda solution: _does_not_run_out_of_fuel(
                solution, max_laps_per_tank, laps_in_race
            ),
            possible_solutions,
        )
    )

    # filter out pit stops that are ridiculously close together
    possible_solutions = list(
        filter(
            lambda s: _pit_stops_not_too_close_together(s, laps_in_race),
            possible_solutions,
        )
    )
    print(f"len(possible_solutions): {len(possible_solutions)}")
    number_of_possible_solutions_after_filtering = len(possible_solutions)
    number_of_filtered_solutions = (
        number_of_possible_solutions - number_of_possible_solutions_after_filtering
    )
    print(
        f"{number_of_possible_solutions} possible solutions remain after filtering {number_of_filtered_solutions} out"
    )

    new_solutions = []

    for solution in possible_solutions:
        for tyre_type in ["RH", "RM", "RS"]:
            new_solution = Solution(
                pit_stop_laps=([0] + solution.pit_stop_laps),
                pit_tyre_choices=([tyre_type] + solution.pit_tyre_choices),
            )
            new_solutions.append(new_solution)

    return new_solutions


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
                Solution(pit_stop_laps=pit_stop_laps, pit_tyre_choices=pit_tyre_choices)
            )
    return solutions


def _does_not_run_out_of_fuel(solution, max_laps_per_tank, laps_in_race):
    lap_diffs = _calculate_lap_diffs(solution.pit_stop_laps, laps_in_race)
    # print(f"lap_diffs: {lap_diffs}")
    if max(lap_diffs) >= max_laps_per_tank:
        return False
    return True


def _pit_stops_not_too_close_together(solution, laps_in_race):
    lap_diffs = _calculate_lap_diffs(solution.pit_stop_laps, laps_in_race)
    if min(lap_diffs) < 3:
        return False
    return True


def _calculate_lap_diffs(pit_stop_laps, laps_in_race):
    v = pit_stop_laps
    lap_diffs = [b - a for (a, b) in list(zip([0] + v, v + [laps_in_race + 1]))]
    return lap_diffs


def _get_time(laps_on_tyres, tyre_type, laptimes):
    # print(f"laptimes: {laptimes}")
    # print(f"tyre_type {tyre_type}")
    # print(f"laps_on_tyres: {laps_on_tyres}")
    # print("############")
    # print(laptimes[tyre_type + 'c'][laps_on_tyres])
    if len(laptimes[tyre_type + "c"]) <= laps_on_tyres:
        print(f"illegal lap number {laps_on_tyres}")
    time = laptimes[tyre_type + "c"][laps_on_tyres]
    # print(f"{laps_on_tyres} laps on {tyre_type} take {time} seconds")
    return time


def _evaluate_solution(
    solution: Solution, laps_in_race: int, average_pit_stop_time: float, laptimes: Any
) -> int:
    solution.pit_stop_laps.append(laps_in_race + 1)
    solution.pit_tyre_choices.append("End")
    time = 0
    last_tyre_type = "RH"
    last_lap = 0

    # print(f"evaluating solution: {solution}")
    # print(f"laps_in_race: {laps_in_race}")
    # print(f"average_pit_stop_time: {average_pit_stop_time}")

    for lap, tyre_type in zip(solution.pit_stop_laps, solution.pit_tyre_choices):
        laps_on_tyres = lap - last_lap
        time += (
            _get_time(laps_on_tyres, last_tyre_type, laptimes) + average_pit_stop_time
        )
        last_lap = lap
        last_tyre_type = tyre_type
        # print("lap", lap, "tyre_type", tyre_type, f"time so far: {time}")

    solution.pit_stop_laps.pop()
    solution.pit_tyre_choices.pop()

    # print(f"total time for solution: {time} seconds")

    return time
