# P1067 [NOIP2009 普及组] 多项式输出 https://www.luogu.com.cn/problem/P1067

n = int(input())
coefficients = map(int, input().split())

is_head = True
while n >= 0:
    coeff = next(coefficients)
    if coeff != 0:
        sign = ('' if is_head else '+') if coeff > 0 else '-'
        c = ('' if coeff in (-1, 1) else abs(coeff)) if n > 0 else abs(coeff)
        x = 'x' if n > 0 else ''
        p = f'^{n}' if n > 1 else ''
        print(f'{sign}{c}{x}{p}', end='')
    if is_head:
        is_head = False
    n -= 1
print()
