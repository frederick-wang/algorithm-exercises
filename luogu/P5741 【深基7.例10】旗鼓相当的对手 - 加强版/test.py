# P5741 【深基7.例10】旗鼓相当的对手 - 加强版 https://www.luogu.com.cn/problem/P5741
from typing import List, NamedTuple


class Student(NamedTuple):
    name: str
    chinese: int
    math: int
    english: int


N = int(input())

students = []  # type: List[Student]
for _ in range(N):
    raw = input().split()
    students.append(Student(raw[0], *map(int, raw[1:])))

for res in ((s1.name, s2.name)
            for s1 in students
            for s2 in students
            if s1.name != s2.name and abs(s1.chinese - s2.chinese) <= 5 and
            abs(s1.math - s2.math) <= 5 and abs(s1.english - s2.english) <= 5
            and abs(sum(s1[1:]) - sum(s2[1:])) <= 10 and s1.name < s2.name):
    print(*res)
