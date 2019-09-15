def define_one_phrase(row, s, indicators):
    for i, letter in enumerate(row):
        for j, banned_phrase in enumerate(s):
            if letter == banned_phrase[indicators[j]]:
                indicators[j] += 1
                if indicators[j] > 1:
                    return 'NO'
    return 'YES'


n, m = input().split(" ")
n, m = int(n), int(m)
s = []
for i in range(n):
    temp = input()
    s.append(temp)
t = []
for i in range(m):
    temp = input()
    t.append(temp)
# n = 3
# m = 5
# s = ['nE', 'NY', 'va']
# t = ['qBDT9', 'valF', 'jdP6MH', 'rnELH', 'aQ9pn']
indicators = [0] * len(s)

for row in t:
    print(define_one_phrase(row, s, indicators[:]))
    # print(indicators)
