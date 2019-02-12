#!/usr/bin/env python3.7


def gen_n_choose_k(n: List[int], k: int) -> List[List[int]]:
    if (k == 0) or (len(n) < k):
        return []
    if k == 1:
        return list(map(lambda x: [x], n))
    case1 = list(
        map(lambda solution: solution + [n[-1]], _gen_n_choose_k(n[:-1], k - 1))
    )
    case2 = _gen_n_choose_k(n[1:], k)
    return case1 + case2
