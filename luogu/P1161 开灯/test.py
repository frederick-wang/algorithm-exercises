# P1161 开灯 https://www.luogu.com.cn/problem/P1161

n = int(input())

result = 0
for _ in range(n):
    raw_input = input().split()
    a, t = float(raw_input[0]), int(raw_input[1])
    for k in [int(i * a) for i in range(1, t + 1)]:
        result ^= k
print(result)

# from typing import Dict

# n = int(input())
# road = {}  # type: Dict[int, bool]

# for _ in range(n):
#     raw_input = input().split()
#     a, t = float(raw_input[0]), int(raw_input[1])
#     for k in [int(i * a) for i in range(1, t + 1)]:
#         if road.get(k):
#             road[k] = False
#         else:
#             road[k] = True

# for i in road:
#     if road[i]:
#         print(i)
#         break
