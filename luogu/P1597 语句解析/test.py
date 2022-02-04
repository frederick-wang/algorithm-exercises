# P1597 语句解析 https://www.luogu.com.cn/problem/P1597

d = {'a': 0, 'b': 0, 'c': 0}
for var, val in map(lambda x: x.split(':='),
                    input().replace('\r', '').replace(';', ' ').split()):
    d[var] = int(val) if val.isdigit() else d[val]

print(*d.values())
