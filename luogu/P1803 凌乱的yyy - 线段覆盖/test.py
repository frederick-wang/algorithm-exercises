# P1803 凌乱的yyy / 线段覆盖 https://www.luogu.com.cn/problem/P1803
# https://www.luogu.com.cn/record/70530896

N = int(input())
competitions = sorted([tuple(map(int,
                                 input().split())) for _ in range(N)],
                      key=lambda x: x[1])
end_time = 0
cnt = 0
for a, b in competitions:
    if a >= end_time:
        cnt += 1
        end_time = b
print(cnt)
