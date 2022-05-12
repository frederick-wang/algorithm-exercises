# P3405 [USACO16DEC]Cities and States S https://www.luogu.com.cn/problem/P3405

from typing import Dict

N = int(input())
cities: Dict[str, Dict[str, int]] = {}
for _ in range(N):
    city = input()
    city_name, state_code = city.split()
    city_abbr = city_name[:2]
    if state_code in cities:
        state = cities[state_code]
        if city_abbr in state:
            state[city_abbr] += 1
        else:
            state[city_abbr] = 1
    else:
        cities[state_code] = {city_abbr: 1}
ans = 0
for state_code, city_abbrs in cities.items():
    for city_abbr, city_num in city_abbrs.items():
        if state_code != city_abbr and city_abbr in cities and state_code in cities[
                city_abbr]:
            ans += city_num * cities[city_abbr][state_code]
print(ans // 2)
