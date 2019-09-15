num_forbid, num_req = map(int, (input().split(" ")))


def is_forb(a, b):
    tmp1 = b.find(a[0])
    if tmp1 < 0:
        return False
    tmp2 = b.rfind(a[1])
    if tmp2 < 0:
        return False
    if tmp1 < tmp2:
        return (True)
    else:
        return (False)


def is_good(a, b):
    for i in a:
        if is_forb(i, b):
            return 'NO'
    return 'YES'


forbiden = []
for i in range(num_forbid):
    forbiden.append(str(input()))

for i in range(num_req):
    print(is_good(forbiden, input()))
