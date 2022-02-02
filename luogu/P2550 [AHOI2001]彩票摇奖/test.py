# P2550 [AHOI2001]彩票摇奖 https://www.luogu.com.cn/problem/P2550

n = int(input())
prized_nums = set(input().split())

result = [0] * 8
for _ in range(n):
    num = len(set(input().split()) & prized_nums)
    result[7 - num] += 1

print(*result[:-1], sep=' ')
