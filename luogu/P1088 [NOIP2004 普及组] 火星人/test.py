# P1088 [NOIP2004 普及组] 火星人 https://www.luogu.com.cn/problem/P1088

from typing import List

N = int(input())
M = int(input())
nums = list(map(int, input().split()))
templ = '%d ' * N
tail = N - 1


def next_permutation(nums: List[int]):
    pivot = 0
    for i in range(tail, 0, -1):
        if nums[i - 1] < nums[i]:
            pivot = i - 1
            break
    for j in range(tail, pivot, -1):
        if nums[pivot] < nums[j]:
            nums[pivot], nums[j] = nums[j], nums[pivot]
            nums[pivot + 1:] = reversed(nums[pivot + 1:])
            return


for _ in range(M):
    next_permutation(nums)

print(templ % tuple(nums))
