# P1090 [NOIP2004 提高组] 合并果子 / [USACO06NOV] Fence Repair G https://www.luogu.com.cn/problem/P1090
# https://www.luogu.com.cn/record/70845423

N = int(input())
nums = list(map(int, input().split()))
result = 0
while len(nums) > 1:
    nums.sort(reverse=True)
    tmp = nums.pop() + nums.pop()
    result += tmp
    nums.append(tmp)
print(result)
