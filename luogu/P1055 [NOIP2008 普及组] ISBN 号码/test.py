# P1055 [NOIP2008 普及组] ISBN 号码 https://www.luogu.com.cn/problem/P1055

raw_input = input().split('-')
a, b, c = map(int, raw_input[:3])
# 测试点 4 末尾的 X 之后好像有空格，不能直接判断是否等于 X
d = int(raw_input[3]) if raw_input[3].isdigit() else 10

id_code = 0
for i, v in enumerate(map(int, str(a) + str(b) + str(c))):
    id_code += v * (i + 1)
id_code = id_code % 11

id_code_str = 'X' if id_code == 10 else str(id_code)

print('Right' if (id_code == d) else (
    '{:d}-{:d}-{:d}-{:s}'.format(a, b, c, id_code_str)))
