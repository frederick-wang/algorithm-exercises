# P3741 honoka的键盘 https://www.luogu.com.cn/problem/P3741

n = int(input())
s = input().replace('\r', '')


def change(c):  # type: (str) -> str
    chars = ['V', 'K']
    return chars[1 - chars.index(c)]


max_num = s.count('VK')
for i, c in enumerate(s):
    s_new = s[:i] + change(c) + s[i + 1:]
    num = s_new.count('VK')
    if num > max_num:
        max_num = num

print(max_num)
