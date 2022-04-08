# P1229 遍历问题 https://www.luogu.com.cn/problem/P1229

pre = input().strip()
post = input().strip()
pre_len = len(pre)

cnt = 1

for i in range(len(pre)):
    j = post.index(pre[i])
    if i + 1 < pre_len and j >= 1 and pre[i + 1] == post[j - 1]:
        cnt *= 2
print(cnt)
