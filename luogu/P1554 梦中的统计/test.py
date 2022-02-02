# P1554 梦中的统计 https://www.luogu.com.cn/problem/P1554

# M, N = map(int, input().split())

# result = [0] * 10
# str_2_num = {
#     '0': 0,
#     '1': 1,
#     '2': 2,
#     '3': 3,
#     '4': 4,
#     '5': 5,
#     '6': 6,
#     '7': 7,
#     '8': 8,
#     '9': 9
# }

# for i in range(M, N + 1):
#     for n in str(i):
#         result[str_2_num[n]] += 1

# print(*result)

M, N = map(int, input().split())
s = ''.join(map(str, range(M, N + 1)))
print(*map(lambda x: s.count(str(x)), range(10)))
