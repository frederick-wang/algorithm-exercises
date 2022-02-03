# P2911 [USACO08OCT]Bovine Bones G https://www.luogu.com.cn/problem/P2911

from collections import Counter

S1, S2, S3 = map(int, input().split())
result = Counter(s1 + s2 + s3 for s1 in range(1, S1 + 1)
                 for s2 in range(1, S2 + 1) for s3 in range(1, S3 + 1))
print(result.most_common()[0][0])
