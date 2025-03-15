# 動的計画を使わない悪い例をメモ化で改善する
# 再帰関数により全探索するが、メモ化で探索の重複を避ける

import sys

n = int(input('Total number of stones: '))
heights = [int(input(f'heights[{i}] = ')) for i in range(n)]
INF = sys.maxsize
dp = [INF] * n

def recursive_frog(i):
    if dp[i] < INF:
        return dp[i]
    
    if i == 0:
        return 0
    
    res = INF
    res = min(res, recursive_frog(i-1) + abs(heights[i] - heights[i-1]))
    if i > 1:
        res = min(res, recursive_frog(i-2) + abs(heights[i] - heights[i-2]))

    dp[i] = res
    return res

print(recursive_frog(n-1))