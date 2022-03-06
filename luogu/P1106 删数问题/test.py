# P1106 删数问题 https://www.luogu.com.cn/problem/P1106

nums = list(map(int, input().strip()))
n = len(nums)
k = int(input())
i = 0
while k:
    if i < n - 1:
        if nums[i] > nums[i + 1]:
            del nums[i]
            k -= 1
            n -= 1
            i = 0
        else:
            i += 1
    elif i == n - 1:
        del nums[i]
        k -= 1
        n -= 1
    else:
        i = n - 1
print(''.join(map(str, nums)).lstrip('0') or 0)
