# P1088 [NOIP2004 普及组] 火星人 https://www.luogu.com.cn/problem/P1088

N = int(input())
M = int(input())
nums = list(map(int, input().split()))

# 将数字的排列转化为序号的排列
remains = list(range(1, N + 1))
for i, n in enumerate(nums):
    serial_num = remains.index(n)
    nums[i] = serial_num
    del remains[serial_num]

# 模拟加法
for _ in range(M):
    nums[-2] += 1
    for i in range(len(nums) - 1, 0, -1):
        upper_bound = N - i
        while nums[i] >= upper_bound:
            nums[i] -= upper_bound
            nums[i - 1] += 1

# 将序号的排列转回数字的排列
remains = list(range(1, N + 1))
for i, s_n in enumerate(nums):
    nums[i] = remains[s_n]
    del remains[s_n]

print(' '.join(map(str, nums)))
