# P3654 First Step (ファーストステップ) https://www.luogu.com.cn/problem/P3654
# https://www.luogu.com.cn/record/70165566

R, C, K = map(int, input().split())
result = 0


def get_cnt(s: str):
    return sum(
        map(lambda x: x - K + 1, filter(lambda n: n >= K,
                                        map(len, s.split('#')))))


court = ['' for _ in range(R)]
for i in range(R):
    court[i] = input().strip()
    result += get_cnt(court[i])
if K > 1:
    result += sum(
        map(lambda j: get_cnt(''.join(map(lambda x: x[j], court))), range(C)))
print(result)
