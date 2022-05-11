# P1317 低洼地 https://www.luogu.com.cn/problem/P1317

N = int(input())
nums = list(map(int, input().split()))
prev = nums[0]
i = 1
while nums[i] > prev:
    prev = nums[i]
    i += 1
ans = 0
while i < N:
    if nums[i] > prev:
        while nums[i] > prev:
            prev = nums[i]
            i += 1
        ans += 1
    prev = nums[i]
    i += 1
print(ans)
