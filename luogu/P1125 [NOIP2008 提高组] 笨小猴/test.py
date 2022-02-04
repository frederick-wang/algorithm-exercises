# P1125 [NOIP2008 提高组] 笨小猴 https://www.luogu.com.cn/problem/P1125

from collections import Counter

word = Counter(input().strip()).most_common()
n = word[0][1] - word[-1][1]

is_lucky = True

if n < 2:
    is_lucky = False
elif n > 2:
    i = 3
    while i * i <= n:
        if n % i == 0:
            is_lucky = False
            break
        i += 2

if is_lucky:
    print('Lucky Word')
    print(n)
else:
    print('No Answer')
    print(0)
