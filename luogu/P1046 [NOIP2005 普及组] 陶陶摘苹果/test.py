# P1046 [NOIP2005 普及组] 陶陶摘苹果 https://www.luogu.com.cn/problem/P1046

apples_height = map(int, input().split())
taotao_height = int(input())

result = 0
for apple_height in apples_height:
    if taotao_height + 30 >= apple_height:
        result += 1

print(result)
