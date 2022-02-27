# P1149 [NOIP2008 提高组] 火柴棒等式 https://www.luogu.com.cn/problem/P1149
# https://www.luogu.com.cn/record/70258902

from typing import List

N = int(input())

matches = {
    '1': 2,
    '+': 2,
    '=': 2,
    '7': 3,
    '4': 4,
    '2': 5,
    '3': 5,
    '5': 5,
    '0': 6,
    '6': 6,
    '9': 6,
    '8': 7
}

used = {'+': False, '=': False}
result = 0


def get_matches_num(n: int):
    return sum(map(matches.__getitem__, str(n)))


def dfs(n: int, cur: str, nums: List[str]):
    global result
    if n == N:
        if used['+'] and used['='] and cur != '=' and int(nums[0]) + int(
                nums[1]) == int(nums[2]):
            result += 1
        return
    for c, num in matches.items():
        if n + num > N:
            break
        if c == '+' and (n == 0 or used['+']):
            continue
        if c == '=' and (n == 0 or used['='] or not used['+'] or cur == '+'):
            continue
        if c in ('+', '='):
            used[c] = True
        if cur in ('', '+', '='):
            dfs(n + num, c, nums + [c])
        else:
            if c in ('', '+', '='):
                dfs(n + num, c, nums)
            else:
                if nums[-1] != '0':
                    dfs(n + num, c, nums[:-1] + [nums[-1] + c])
        if c in ('+', '='):
            used[c] = False


dfs(0, '', [])
print(result)
