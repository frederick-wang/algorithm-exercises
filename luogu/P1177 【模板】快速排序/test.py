# P1177 【模板】快速排序 https://www.luogu.com.cn/problem/P1177

from typing import List
import random

N = int(input())
nums = list(map(int, input().split()))[:N]


def quick_sort(arr: List[int], left: int, right: int):
    if left >= right:
        return

    # 一定要随机选一个 pivot，而不是直接用 arr[left]，否则如果数据本身有序，会巨慢
    pivot_idx = random.randint(left, right)
    pivot = arr[pivot_idx]
    arr[left], arr[pivot_idx] = arr[pivot_idx], arr[left]
    i, j, k = left + 1, left, right + 1

    while i < k:
        if arr[i] == pivot:
            i += 1
        elif arr[i] < pivot:
            arr[i], arr[j + 1] = arr[j + 1], arr[i]
            j += 1
            i += 1
        else:
            arr[i], arr[k - 1] = arr[k - 1], arr[i]
            k -= 1
    arr[left], arr[j] = arr[j], arr[left]

    quick_sort(arr, left, j - 1)
    quick_sort(arr, k, right)


quick_sort(nums, 0, len(nums) - 1)

print(' '.join(map(str, nums)))
