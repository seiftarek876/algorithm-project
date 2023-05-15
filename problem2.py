def find_max_profit(jobs):
    # Sort jobs based on end times in ascending order
    jobs.sort(key=lambda x: x[1])

    n = len(jobs)
    dp = [0] * n
    dp[0] = jobs[0][2]  # Initialize dp[0] with the profit of the first job

    for i in range(1, n):
        # Find the last non-overlapping job
        last_non_overlap = -1
        for j in range(i - 1, -1, -1):
            if jobs[j][1] <= jobs[i][0]:
                last_non_overlap = j
                break

        # Calculate the maximum profit at the current job
        include_profit = jobs[i][2]
        if last_non_overlap != -1:
            include_profit += dp[last_non_overlap]

        # Calculate the maximum profit without including the current job
        exclude_profit = dp[i - 1]

        # Take the maximum profit between including and excluding the current job
        dp[i] = max(include_profit, exclude_profit)

    # Return the maximum profit achievable
    return dp[n - 1]


# Example usage
jobs = [[1, 6, 6], [2, 5, 5], [5, 7, 5], [6, 8, 3]]
max_profit = find_max_profit(jobs)
print("Maximum profit:", max_profit)
