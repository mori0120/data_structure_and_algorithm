# 動的計画法の例：Frog問題(pull-base)

n: int = int(input('Total num = '))
nums = [int(input(f'nums[{i}] = ')) for i in range(n)]

dp = [0] * n

for i in range(1, n):
    if i==1:
        dp[i] = abs(nums[i-1] - nums[i])
    else:
        dp[i] = min(dp[i-2] + abs(nums[i-2] - nums[i]), dp[i-1] + abs(nums[i-1] - nums[i]))

print(f'result = {dp[n-1]}')