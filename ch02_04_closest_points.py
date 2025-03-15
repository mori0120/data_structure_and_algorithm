# 最近点対問題に対する全探索
# 計算量O(n^2)の例
import sys
import math

def calc_dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2))

n = int(input('Total number: '))
x = [0]*n
y = [0]*n
min_dist = sys.maxsize

for i in range(n):
    x[i], y[i] = map(int, input('x y: ').split())

for i in range(n):
    for j in range(i+1, n):
        tmp = calc_dist(x[i], y[i], x[j], y[j])
        min_dist = min(min_dist, tmp)

print(min_dist)