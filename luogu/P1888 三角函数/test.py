# P1888 三角函数 https://www.luogu.com.cn/problem/P1888

a, b, c = sorted(list(map(int, input().split())))

# factor = 2

# while factor**2 <= a:
#     if a % factor == 0 and c % factor == 0:
#         a //= factor
#         c //= factor
#         factor = 2
#     factor += 1

d1, d2 = c, a
while d1 % d2:
    d1, d2 = d2, d1 % d2

print('%d/%d' % (a // d2, c // d2))
