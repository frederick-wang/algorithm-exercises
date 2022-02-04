# P5734 【深基6.例6】文字处理软件 https://www.luogu.com.cn/problem/P5734

n = int(input())
doc = input().strip()

while n:
    raw_input = input().strip().split()
    op = raw_input[0]
    if op == '4':
        print(doc.find(raw_input[1]))
    else:
        if op == '1':
            doc = doc + raw_input[1]
        elif op == '2':
            a, b = map(int, raw_input[1:])
            doc = doc[a:a + b]
        elif op == '3':
            a = int(raw_input[1])
            doc = doc[:a] + raw_input[2] + doc[a:]
        print(doc)
    n -= 1
