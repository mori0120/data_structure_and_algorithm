# 動的計画法の代表的課題。ナップサック問題。
# 重さと価値がそれぞれweights[i]とvalues[i]であるn個の品物があり、
# 重さの総和がwを超えないように、価値の総和を最大化する。
# 計算量をO(nw)に抑えることができる。
# dp[i+1][w] = i番目までの品物から重さの総和がwを超えないように選んだときの価値の総和の最大値
# i番目(0 ~ N-1)までの品物から重さがj(0 ~ w)を超えないように選んだときの価値の総和の最大値を繰り返し求める。

n = int(input('Total number of items: '))
w = int(input('Total weight: '))
weights = [0] * n
values = [0] * n
for i in range(n):
    weights[i], values[i] = map(int, input(f'weights[{i}] values[{i}] = ').split())

dp = [[0] * (w+1) for _ in range(n+1)]

for i in range(n):
    for j in range(w+1):
        # i番目の品物を選ぶ場合
        if j - weights[i] >= 0:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j-weights[i]] + values[i])
        # i番目の品物を選ばない場合
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])

print(dp[n][w])