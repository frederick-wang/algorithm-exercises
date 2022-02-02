# P5728 【深基5.例5】旗鼓相当的对手 https://www.luogu.com.cn/problem/P5728

from typing import List, Tuple

N = int(input())

students = []  # type: List[Tuple[int, int, int]]
result = 0

for i in range(N):
    c, m, e = map(int, input().split())
    for c_, m_, e_ in students:
        if abs(c - c_) <= 5 and abs(m - m_) <= 5 and abs(e - e_) <= 5 and abs(
                c + m + e - c_ - m_ - e_) <= 10:
            result += 1
    students.append((c, m, e))

print(result)
