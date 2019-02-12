#!/usr/bin/env python3.7

# Standard library
from typing import List, Any
from functools import reduce
import operator


def gen_k_combinations(n: List[Any], k: int) -> List[List[Any]]:
    """
    Also known as 'n choose k'
    """
    if (k == 0) or (len(n) < k):
        return []
    if k == 1:
        return list(map(lambda x: [x], n))
    case1 = list(
        map(
            lambda combination: combination + [n[-1]], gen_k_combinations(n[:-1], k - 1)
        )
    )
    case2 = gen_k_combinations(n[:-1], k)
    return case1 + case2


def gen_k_multicombinations(n: List[Any], k: int) -> List[List[Any]]:
    """
    Also known as 'n choose k with repetition'
    """
    return _gen_k_multicombinations(n, k, [])


def _gen_k_multicombinations(n: List[Any], k: int, y: List[Any]) -> List[List[Any]]:
    if k == 0:
        return [y]
    combinations = list(map(lambda x: _gen_k_multicombinations(n, k - 1, y + [x]), n))
    combinations = reduce(operator.add, combinations)
    return combinations


def test():
    print("gen_k_combinations([1,2,3], 2)")
    print(gen_k_combinations([1, 2, 3], 2))
    print("gen_k_multicombinations([1,2,3], 2)")
    print(gen_k_multicombinations([1, 2, 3], 2))


if __name__ == "__main__":
    test()
