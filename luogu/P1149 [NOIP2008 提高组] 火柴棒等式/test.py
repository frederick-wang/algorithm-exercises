# P1149 [NOIP2008 提高组] 火柴棒等式 https://www.luogu.com.cn/problem/P1149
# https://www.luogu.com.cn/record/70261238

N = int(input())
MAX_NUM = N - 4

matches = (6, 2, 5, 5, 4, 5, 6, 3, 7, 6)
matches_num = [0] * 1999
result = 0


def get_matches_num(n: int):
    if not matches_num[n]:
        matches_num[n] = sum(map(matches.__getitem__, map(int, str(n))))
    return matches_num[n]


nums = sorted(map(lambda x: (get_matches_num(x), x), range(1000)))
for a_num, a in nums:
    if a_num > MAX_NUM:
        break
    for b_num, b in nums:
        if a_num + b_num > MAX_NUM:
            break
        c = a + b
        c_num = get_matches_num(c)
        if a_num + b_num + c_num == MAX_NUM:
            result += 1
print(result)
