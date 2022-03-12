# P2404 自然数的拆分问题
# https://www.luogu.com.cn/record/71254007

N = int(input())
nums = [0] * N


def dfs(i: int, residue: int):
    if not residue:
        print('+'.join(map(str, nums[:i])))
        return
    for j in range(nums[i - 1] if i else 1, residue + 1 if i else N):
        nums[i] = j
        dfs(i + 1, residue - j)


dfs(0, N)
