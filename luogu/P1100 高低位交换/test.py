# P1100 高低位交换 https://www.luogu.com.cn/problem/P1100

n = int(input())
print(n >> 16 | n << 16 & 0xffffffff)
