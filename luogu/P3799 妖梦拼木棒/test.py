# P3799 妖梦拼木棒 https://www.luogu.com.cn/problem/P3799
# 用 PyPy3 提交: https://www.luogu.com.cn/record/70263791

N = int(input())
nums = [0] * N
counter = [0] * 5001
i = 0
while i < N:
    for num in map(int, input().split()):
        nums[i] = num
        counter[num] += 1
        i += 1
nums.sort()
result = 0
i = 0
while i < N:
    a = nums[i]
    a_cnt = counter[a]
    if a_cnt > 1:
        c = 2 * a
        if c <= 5000:
            c_cnt = counter[c]
            if c_cnt > 1:
                result += c_cnt * (c_cnt - 1) * a_cnt * (a_cnt - 1) >> 2
    j = i + a_cnt
    while j < N:
        b = nums[j]
        b_cnt = counter[b]
        c = a + b
        if c <= 5000:
            c_cnt = counter[c]
            if c_cnt > 1:
                result += c_cnt * (c_cnt - 1) * a_cnt * b_cnt >> 1
        j += b_cnt
    i += a_cnt
print(result % 1000000007)
