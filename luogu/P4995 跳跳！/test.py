# P4995 跳跳！ https://www.luogu.com.cn/problem/P4995

N = int(input())
nums = list(map(int, input().split()))
nums.sort()
result = (nums[-1])**2
i = N - 1
while (l := len(nums)) > 1:
    if not i:
        i = l - 1
        result += (nums[-1] - nums.pop(0))**2
    else:
        i = 0
        result += (nums.pop() - nums[0])**2
print(result)
