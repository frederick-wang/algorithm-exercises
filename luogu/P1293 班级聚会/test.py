# P1293 班级聚会 https://www.luogu.com.cn/problem/P1293

from typing import List


class City:
    num: int
    distance: int
    name: str

    def __init__(self, num: int, distance: int, name: str):
        self.num = num
        self.distance = distance
        self.name = name

    def __repr__(self) -> str:
        return f'City(num={self.num}, distance={self.distance}, name={self.name})'


cities: List[City] = []
while True:
    raw_input = input().split()
    num = int(raw_input[0])
    distance = int(raw_input[1])
    name = raw_input[2]
    cities.append(City(num, distance, name))
    if name == 'Moscow':
        break


def get_all_distance(ci: City) -> int:
    return sum(
        abs(cj.num * (ci.distance - cj.distance)) for cj in cities if ci != cj)


min_distance = int(1e9)
min_city: City = cities[0]

for city in cities:
    distance = get_all_distance(city)
    if distance >= min_distance and distance == min_distance and city.distance < min_city.distance or distance < min_distance:
        min_distance = distance
        min_city = city
print(f'{min_city.name} {min_distance}')
