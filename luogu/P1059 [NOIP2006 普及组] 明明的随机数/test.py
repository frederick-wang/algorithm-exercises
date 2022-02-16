# P1059 [NOIP2006 普及组] 明明的随机数 https://www.luogu.com.cn/problem/P1059

N = int(input())
nums = sorted(set(map(int, input().split())))
print(len(nums))
print(*nums)
