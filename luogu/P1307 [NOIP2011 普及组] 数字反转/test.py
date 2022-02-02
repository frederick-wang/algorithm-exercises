# P1307 [NOIP2011 普及组] 数字反转 https://www.luogu.com.cn/problem/P1307

N = int(input())

reversed_str = str(N)[::-1]

if reversed_str[-1] == '-':
    reversed_str = '-' + reversed_str[:-1]

print(int(reversed_str))
