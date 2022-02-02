# P2141 [NOIP2014 普及组] 珠心算测验 https://www.luogu.com.cn/problem/P2141

n = int(input())
nums = set(map(int, input().split()))
sum_set = set(i + j for i in nums for j in nums if i != j)
print(len(nums & sum_set))
