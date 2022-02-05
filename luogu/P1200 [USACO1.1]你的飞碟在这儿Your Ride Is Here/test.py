# P1200 [USACO1.1]你的飞碟在这儿Your Ride Is Here https://www.luogu.com.cn/problem/P1200

from functools import reduce
from operator import mul

comet_name = input().strip()
team_name = input().strip()


def calc_num(s):  # type: (str) -> int
    return reduce(mul, map(lambda x: ord(x) - 64, s)) % 47


if calc_num(comet_name) == calc_num(team_name):
    print('GO')
else:
    print('STAY')
