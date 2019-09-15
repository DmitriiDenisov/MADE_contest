# num_work, num_jobs, k = map(int, (input().split(" ")))
# workers = list(map(int, (input().split(" "))))
# jobs = list(map(int, (input().split(" "))))
workers = [18, 1, 3, 10, 8, 14]
jobs = [1, 4, 12, 11, 20, 5, 6]
k = 4

success_workers = []
for worker in workers:
    done_job = 0
    for job in jobs:
        if abs(worker - job) <= k:
            done_job += 1
    success_workers.append(done_job)

print(success_workers.index(max(success_workers)) + 1)
