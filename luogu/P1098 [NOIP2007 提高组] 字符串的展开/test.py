# P1098 [NOIP2007 提高组] 字符串的展开 https://www.luogu.com.cn/problem/P1098

p1, p2, p3 = map(int, input().split())
s = input().strip()

i = 0
while i < len(s):
    if i < len(s) - 2:
        cl, cm, cr = s[i], s[i + 1], s[i + 2]
        if cm == '-':
            if cl.isdecimal() and cr.isdecimal():
                if ord(cr) <= ord(cl):
                    print(f'{cl}-', end='')
                elif ord(cr) == ord(cl) + 1:
                    print(f'{cl}', end='')
                else:
                    seq = ''.join(('*' if p1 == 3 else chr(i)) * p2
                                for i in range(ord(cl) + 1, ord(cr)))
                    print(f'{cl}{seq if p3 == 1 else seq[::-1]}', end='')
                i += 2
            elif cl.isalpha() and cl.islower() and cr.isalpha() and cr.islower():
                if ord(cr) <= ord(cl):
                    print(f'{cl}-', end='')
                elif ord(cr) == ord(cl) + 1:
                    print(f'{cl}', end='')
                else:
                    seq = ''.join(('*' if p1 == 3 else
                                (chr(i).upper() if p1 == 2 else chr(i))) * p2
                                for i in range(ord(cl) + 1, ord(cr)))
                    print(f'{cl}{seq if p3 == 1 else seq[::-1]}', end='')
                i += 2
            else:
                print(cl, end='')
                i += 1
        else:
            print(cl, end='')
            i += 1
    else:
        print(s[i], end='')
        i += 1
print()
