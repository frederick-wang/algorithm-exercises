# P1226 【模板】快速幂||取余运算 https://www.luogu.com.cn/problem/P1226

A, B, P = map(int, input().split())
m = pow(A, B, P)
print(f'{A}^{B} mod {P}={m}')
