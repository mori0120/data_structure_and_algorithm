# 動的計画法の例：Frog問題(push-base)
import sys

n: int = int(input('Total num = '))
nums = [int(input(f'nums[{i}] = ')) for i in range(n)]

dp = [sys.maxsize] * n
dp[0] = 0

for i in range(n):
    if i+1 < n:
        dp[i+1] = min(dp[i+1], dp[i] + abs(nums[i+1] - nums[i]))
    if i+2 < n:
        dp[i+2] = min(dp[i+2], dp[i] + abs(nums[i+2] - nums[i]))

print(f'result = {dp[n-1]}')