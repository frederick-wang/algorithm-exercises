# P5461 赦免战俘 https://www.luogu.com.cn/problem/P5461
from array import array

N = int(input())
SIDE_LEN = 2**N

s = array('b', [1]) * SIDE_LEN**2


def pardon(x: int, y: int, side_len: int):
    if side_len == 1:
        return
    half_len = side_len // 2
    for i in range(x, x + half_len):
        for j in range(y, y + half_len):
            s[i * SIDE_LEN + j] = 0
    pardon(x + half_len, y, half_len)
    pardon(x, y + half_len, half_len)
    pardon(x + half_len, y + half_len, half_len)


pardon(0, 0, SIDE_LEN)

for i in range(SIDE_LEN):
    print(*s[i * SIDE_LEN:(i + 1) * SIDE_LEN])
