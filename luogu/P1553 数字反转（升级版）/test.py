# P1553 数字反转（升级版） https://www.luogu.com.cn/problem/P1553

s = input().strip()

if '.' in s:
    int_part, fractional_part = s.split('.')
    print('%d.%s' % (int(int_part[::-1]), str(int(fractional_part))[::-1]))
elif '/' in s:
    numerator, denominator = s.split('/')
    print('%d/%d' % (int(numerator[::-1]), int(denominator[::-1])))
    pass
elif '%' in s:
    print('%d%%' % int(s[-2::-1]))
    pass
else:
    print(int(s[::-1]))
