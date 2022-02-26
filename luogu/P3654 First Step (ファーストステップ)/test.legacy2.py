# P3654 First Step (ファーストステップ) https://www.luogu.com.cn/problem/P3654
# https://www.luogu.com.cn/record/70169896

R, C, K = map(int, input().split())


def get_cnt(s: str) -> int:
    cnt = 0
    j = 0
    while j < C:
        if s[j] == '#':
            j += 1
            continue
        jj = j
        while jj < C and s[jj] == '.':
            jj += 1
        seg_len = jj - j
        if seg_len >= K:
            cnt += seg_len - K + 1
        j = jj
    return cnt


result = 0
court = ['' for _ in range(R)]
for i in range(R):
    court[i] = input().strip()
    result += get_cnt(court[i])
if K > 1:
    for j in range(C):
        result += get_cnt(''.join(map(lambda x: x[j], court)))
print(result)
