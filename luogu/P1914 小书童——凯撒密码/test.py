# P1914 小书童——凯撒密码 https://www.luogu.com.cn/problem/P1914

n = int(input())
print(''.join(map(lambda c: chr((ord(c) + n - 97) % 26 + 97), input())))
