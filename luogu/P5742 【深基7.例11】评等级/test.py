# P5742 【深基7.例11】评等级 https://www.luogu.com.cn/problem/P5742
from typing import List, NamedTuple


class Student(NamedTuple):
    id: int
    academic: int
    quality: int
    overall: float

    @property
    def toal(self):
        return self.academic + self.quality


def is_excellent(student: Student) -> bool:
    return student.overall >= 80 and student.toal > 140


N = int(input())

students = []  # type: List[Student]
for _ in range(N):
    id, academic, quality = map(int, input().split())
    student = Student(id, academic, quality, academic * 0.7 + quality * 0.3)
    print('Excellent' if is_excellent(student) else 'Not excellent')
