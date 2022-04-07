# P1887 乘积最大3 https://www.luogu.com.cn/problem/P1887

N, M = map(int, input().split())
a = N // M
diff = N - a * M
nums = [a] * M
i = M - 1
while diff:
    nums[i] += 1
    i = i - 1 if i else M - 1
    diff -= 1
print(' '.join(map(str, nums)))
