# P1106 删数问题 https://www.luogu.com.cn/problem/P1106

nums = list(map(int, input().strip()))
K = int(input())
n = len(nums)
for _ in range(K):
    max_diff = 10**(n - 1) * nums[0]
    max_idx = 0
    s = 0
    for i in range(1, n):
        k = n - 1 - i
        s += 9 * nums[i - 1] * 10**k
        diff = s + 10**k * nums[i]
        if diff > max_diff:
            max_idx = i
            max_diff = diff
    del nums[max_idx]
    n -= 1
print(''.join(map(str, nums)).lstrip('0') or 0)
