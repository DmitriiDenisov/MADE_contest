# num_work, num_jobs, dif = map(int, (input().split(" ")))

# for i in range(1):
#    workers = list(map(int, (input().split(" "))))
#    jobs = list(map(int, (input().split(" "))))

workers = [18, 1, 3, 10, 8, 14]
jobs = [1, 4, 12, 11, 20, 5, 6]
num_work = len(workers)
num_jobs = len(jobs)
dif = 4


rate = []

for i in range(num_work):
    rate += [sum(map(lambda x, y, k: abs(x - y) <= k, [workers[i]] * num_jobs, jobs, [dif] * num_jobs))]

print(max(enumerate(rate), key=lambda tpl: tpl[1])[0] + 1)
