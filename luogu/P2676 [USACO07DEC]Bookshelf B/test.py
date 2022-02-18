# P2676 [USACO07DEC]Bookshelf B https://www.luogu.com.cn/problem/P2676

N, b = map(int, input().split())

nums = [int(input()) for _ in range(N)]
nums.sort(reverse=True)

i = 0
while b > 0:
    b -= nums[i]
    i += 1
print(i)
