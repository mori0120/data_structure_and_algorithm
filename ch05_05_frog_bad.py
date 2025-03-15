# 動的計画を使わない悪い例
# 再帰関数により全探索する
# 計算時間が指数時間になる

import sys

n = int(input('Total number of stones: '))
heights = [int(input(f'heights[{i}] = ')) for i in range(n)]
INF = sys.maxsize

def recursive_frog(i):
    if i == 0:
        return 0
    
    res = INF
    res = min(res, recursive_frog(i-1) + abs(heights[i] - heights[i-1]))
    if i > 1:
        res = min(res, recursive_frog(i-2) + abs(heights[i] - heights[i-2]))
    return res

print(recursive_frog(n-1))