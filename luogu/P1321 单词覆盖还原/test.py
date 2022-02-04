# P1321 单词覆盖还原 https://www.luogu.com.cn/problem/P1321

from itertools import combinations

s = input().strip()

com_boy = (
    'boy',
    *map(''.join, combinations('boy', 2)),
    *'boy',
)
com_girl = (
    'girl',
    *map(''.join, combinations('girl', 3)),
    *map(''.join, combinations('girl', 2)),
    *'girl',
)
num_boy = 0
num_girl = 0

for frag in com_boy:
    num_boy += s.count(frag)
    s = s.replace(frag, '.')

for frag in com_girl:
    num_girl += s.count(frag)
    s = s.replace(frag, '.')

print(num_boy)
print(num_girl)

# from itertools import combinations

# s = input().replace('.', ' ').strip()

# com_boy = (
#     'boy',
#     *map(''.join, combinations('boy', 2)),
#     *'boy',
# )
# com_girl = (
#     'girl',
#     *map(''.join, combinations('girl', 3)),
#     *map(''.join, combinations('girl', 2)),
#     *'girl',
# )

# num_boy = 0
# num_girl = 0

# while s:
#     for frag in com_boy:
#         idx = s.find(frag)
#         if idx != -1:
#             s = s[:idx] + ' ' + s[idx + len(frag):]
#             num_boy += 1
#             break
#     for frag in com_girl:
#         idx = s.find(frag)
#         if idx != -1:
#             s = s[:idx] + ' ' + s[idx + len(frag):]
#             num_girl += 1
#             break
#     s = s.strip()

# print(num_boy)
# print(num_girl)
