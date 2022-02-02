# P4956 [COCI2017-2018#6] Davor https://www.luogu.com.cn/problem/P4956

N = int(input())

N_week = N // 52

for x in range(100, 0, -1):
    sum_x = 7 * x
    if sum_x >= N_week:
        continue
    else:
        residue = N_week - sum_x
        if residue % 21 == 0:
            print(x)
            print(residue // 21)
            break
        else:
            continue
