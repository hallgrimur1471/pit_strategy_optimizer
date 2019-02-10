#!/usr/bin/env python3.7

from typing import Generator, Tuple, Dict, Any


class Solution:
    def __init__(self):
        pass


def evaluate_solution(solution: Solution) -> int:
    return 1  # random score


def generate_possible_solutions() -> Generator[Solution, None, None]:
    for number in range(10):
        yield Solution()


def calculate_optimal_pit_stop_strategy(
    race_data: Dict[Any, Any]
) -> Tuple[Solution, int]:
    possible_solutions = generate_possible_solutions()
    scores = map(evaluate_solution, possible_solutions)
    pairs = zip(possible_solutions, scores)
    return max(pairs, key=lambda p: p[1])
