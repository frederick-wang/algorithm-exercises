# P1308 [NOIP2011 普及组] 统计单词数 https://www.luogu.com.cn/problem/P1308

word = input().strip().lower()
s = input().lower()

n = s.split().count(word) or -1
print(n, end='')

if n == -1:
    print()
else:
    print(' %d' % (' ' + s + ' ').index(' ' + word + ' '))

# word = input().strip().lower()
# s = input().lower()
# words = s.split()
# n = words.count(word) or -1
# print(n, end='')

# word_len = len(word)
# if n == -1:
#     print()
# else:
#     for i in range(len(s) - word_len + 1):
#         if word == s[i:i + word_len] and (s[i - 1] == ' ' or
#                                           i == 0) and (i + word_len == len(s) or
#                                                        s[i + word_len] == ' '):
#             print(' %d' % i)
#             break
