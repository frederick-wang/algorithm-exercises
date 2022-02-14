# P2392 kkksc03考前临时抱佛脚 https://www.luogu.com.cn/problem/P2392

from typing import Tuple, Set

used: Set[int] = set()


def get_min_time(
    total: int,
    L: Tuple[int, ...],
    left_sum: int,
    right_sum: int,
) -> int:
    global min_time
    L_LEN = len(L)

    if total == L_LEN:
        t = max(left_sum, right_sum)
        min_time = min(min_time, t)
        return t

    for i in range(L_LEN):
        if i not in used:
            new_left_sum = left_sum + L[i]
            new_right_sum = right_sum + L[i]
            nlgm = new_left_sum >= min_time
            nrgm = new_right_sum >= min_time
            res = min_time
            if nlgm and nrgm:
                return res
            used.add(i)
            if nlgm and not nrgm:
                res = min(min_time,
                          get_min_time(total + 1, L, left_sum, new_right_sum))
            elif not nlgm and nrgm:
                res = min(min_time,
                          get_min_time(total + 1, L, new_left_sum, right_sum))
            else:
                res = min(get_min_time(
                    total + 1,
                    L,
                    new_left_sum,
                    right_sum,
                ), get_min_time(
                    total + 1,
                    L,
                    left_sum,
                    new_right_sum,
                ))
            used.remove(i)
            return res

    return min_time


s1, s2, s3, s4 = map(int, input().split())

result = 0
for _ in range(4):
    min_time = 1000000
    result += get_min_time(0, tuple(map(int, input().split())), 0, 0)

print(result)
