# P1628 合并序列 https://www.luogu.com.cn/problem/P1628

N = int(input())
words = [input().strip() for _ in range(N)]
T = input().strip()
print('\n'.join(sorted(word for word in words if word.startswith(T))))
