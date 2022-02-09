# P1328 [NOIP2014 提高组] 生活大爆炸版石头剪刀布 https://www.luogu.com.cn/problem/P1328

rule = {
    0: {
        0: 0,
        1: 0,
        2: 1,
        3: 1,
        4: 0
    },
    1: {
        0: 1,
        1: 0,
        2: 0,
        3: 1,
        4: 0
    },
    2: {
        0: 0,
        1: 1,
        2: 0,
        3: 0,
        4: 1
    },
    3: {
        0: 0,
        1: 0,
        2: 1,
        3: 0,
        4: 1
    },
    4: {
        0: 1,
        1: 1,
        2: 0,
        3: 0,
        4: 0
    }
}

N, N_A, N_B = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

score_a = 0
score_b = 0
for i in range(N):
    a_i = A[i % N_A]
    b_i = B[i % N_B]
    score_a += rule[a_i][b_i]
    score_b += rule[b_i][a_i]

print(score_a, score_b)
