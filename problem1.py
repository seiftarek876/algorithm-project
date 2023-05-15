def schedule_jobs(jobs):
    # Sort the jobs in descending order of profits
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Find the maximum deadline among all jobs
    max_deadline = max(jobs, key=lambda x: x[1])[1]

    # Initialize an array to keep track of the scheduled jobs
    result = [-1] * max_deadline

    # Initialize variables for counting the number of jobs done and the maximum profit
    num_jobs_done = 0
    max_profit = 0

    # Iterate over the jobs and schedule them
    for job in jobs:
        deadline = job[1]
        profit = job[2]

        # Find the latest available slot for the job
        slot = deadline - 1
        while slot >= 0 and result[slot] != -1:
            slot -= 1

        # If a slot is available, schedule the job
        if slot >= 0:
            result[slot] = job[0]
            num_jobs_done += 1
            max_profit += profit

    return num_jobs_done, max_profit


# Example usage
jobs = [(1, 4, 20), (2, 1, 10), (3, 1, 40), (4, 1, 30)]
num_jobs_done, max_profit = schedule_jobs(jobs)

print("Number of jobs done:", num_jobs_done)
print("Maximum profit:", max_profit)
