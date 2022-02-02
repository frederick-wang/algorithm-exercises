# P5730 【深基5.例10】显示屏 https://www.luogu.com.cn/problem/P5730

num = [[
    'XXX',
    'X.X',
    'X.X',
    'X.X',
    'XXX',
], [
    '..X',
    '..X',
    '..X',
    '..X',
    '..X',
], [
    'XXX',
    '..X',
    'XXX',
    'X..',
    'XXX',
], [
    'XXX',
    '..X',
    'XXX',
    '..X',
    'XXX',
], [
    'X.X',
    'X.X',
    'XXX',
    '..X',
    '..X',
], [
    'XXX',
    'X..',
    'XXX',
    '..X',
    'XXX',
], [
    'XXX',
    'X..',
    'XXX',
    'X.X',
    'XXX',
], [
    'XXX',
    '..X',
    '..X',
    '..X',
    '..X',
], [
    'XXX',
    'X.X',
    'XXX',
    'X.X',
    'XXX',
], [
    'XXX',
    'X.X',
    'XXX',
    '..X',
    'XXX',
]]

result = [''] * 5

N = int(input())
digits = map(int, list(filter(lambda x: x.isdigit(), input())))

for i, n in enumerate(digits):
    for j, row in enumerate(num[n]):
        result[j] += row
        if i < N - 1:
            result[j] += '.'

print('\n'.join(result))
