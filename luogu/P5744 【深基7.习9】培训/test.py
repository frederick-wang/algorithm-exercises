# P5744 【深基7.习9】培训 https://www.luogu.com.cn/problem/P5744
from typing import NamedTuple


class Student(NamedTuple):
    name: str
    age: int
    score: int


N = int(input())


def study(student):  # type: (Student) -> Student
    score = student.score // 5 * 6
    return Student(student.name, student.age + 1, score if score < 600 else 600)


for _ in range(N):
    raw = input().split()
    name, (age, score) = raw[0], map(int, raw[1:])
    student = study(Student(name, age, score))
    print(*student)
