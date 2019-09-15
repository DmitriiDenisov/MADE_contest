# n = input()
# a = list(map(int, input().split(' ')))
a = [1, 3, 1, 2, 1, 1, 4]
b = [[], [], [], []] # [1 ,2, 3 ,4]
for i, j in enumerate(a):
    b[j - 1].append(i + 1)
all = 0
for i in b[3]: # только для 4
    all += 1
k = min(len(b[0]), len(b[2])) # минимум из 1 и 3
for l, i in enumerate(b[2]):
    if k < (l + 1): break
    all += 1
if k < len(b[2]):
    for i in range(len(b[2]) - k):
        all += 1
k2 = len(b[1]) // 2

for i in range(k2):
    all += 1

n1 = 0
if len(b[1]) % 2 == 1:
    if len(b[0]) == k:
        all += 1
    else:
        if len(b[0]) - k >= 2:
            n1 += 2
            all += 1
        if len(b[0]) - k == 1:
            n1 += 1
            all += 1
k1 = (len(b[0]) - k - n1) // 4
ispol = k + n1
for i in range(k1):
    all += 1
rest = len(b[0]) - (k1 * 4 + ispol)
l = b[0][-rest:]
if rest > 0:
    all += 1

print(all)

for i in b[3]:
    print(1, i)
k = min(len(b[0]), len(b[2]))
for l, i in enumerate(b[2]):
    if k < (l + 1): break
    print(2, i, b[0][l])
if k < len(b[2]):
    for i in range(len(b[2]) - k):
        print(1, b[2][-(i + 1)])
k2 = len(b[1]) // 2
for i in range(k2):
    print(2, b[1][2 * i], b[1][2 * i + 1])

n1 = 0
if len(b[1]) % 2 == 1:
    if len(b[0]) == k:
        print(1, b[1][-1])
    else:
        if len(b[0]) - k >= 2:
            n1 += 2
            print(3, b[1][-1], b[0][k], b[0][k + 1])
        if len(b[0]) - k == 1:
            n1 += 1
            print(2, b[1][-1], b[0][k])
k1 = (len(b[0]) - k - n1) // 4
ispol = k + n1
for i in range(k1):
    print(4, b[0][ispol + i * 4], b[0][ispol + i * 4 + 1], b[0][ispol + i * 4 + 2], b[0][ispol + i * 4 + 3])
rest = len(b[0]) - (k1 * 4 + ispol)
l = b[0][-rest:]
if rest > 0: print(rest, ' '.join(map(str, l)))
