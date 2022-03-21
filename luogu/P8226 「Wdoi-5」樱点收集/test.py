# P8226 「Wdoi-5」樱点收集 https://www.luogu.com.cn/problem/P8226

N, M, K = map(int, input().split())
b = [0] * int(3e5 + 1)
for i in map(int, input().split()):
    b[i] = 1
a = [0] + list(map(lambda x: int(x) % K, input().split()))
s = [0] * (N + 1)
for i in range(1, N + 1):
    s[i] = (s[i - 1] + a[i]) % K
cnt = [0] * (N + 1)
for i in range(1, N + 1):
    cnt[i] = cnt[i - 1] if s[i] else cnt[i - 1] + b[i]
max_cnt = cnt[N]
x = [0] * K  # x_m 为 s_{j+1} 到 s_n 中和 a_j 模 K 同余 m 的数的个数
# 即 s_{j+1} 到 s_n 全部减去 a_j 后，新的 s_{j+1} 到 s_n 中可以被 K 整除且被灵梦要求的数的个数）
for j in reversed(range(1, N + 1)):
    # 太慢
    # x = [0] * K
    # for k in range(j + 1, N + 1):
    #     x[s[k]] += b[k]
    max_cnt = max(max_cnt, cnt[j - 1] + x[a[j]])
    x[s[j]] += b[j]
print(max_cnt)
