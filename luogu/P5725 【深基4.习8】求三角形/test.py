n = int(input())

for i in range(1, n**2 + 1):
    print('%02d' % i, end='')
    if i % n == 0:
        print()

print()

line_width_max = 1
current_line_width = 0
for i in range(1, n * (n + 1) // 2 + 1):
    if current_line_width == 0:
        print('  ' * (n - line_width_max), end='')
    print('%02d' % i, end='')
    current_line_width += 1
    if current_line_width == line_width_max:
        print()
        line_width_max += 1
        current_line_width = 0
