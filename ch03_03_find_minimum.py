# 線形探索法の例その3：最小値を求める

import sys


n = int(input('Total number: '))
array = [int(input(f'array[{_}] = ')) for _ in range(n)]
min_num = sys.maxsize

for i in range(n):
    if array[i] < min_num:
        min_num = array[i]

print(f'Minimum number in the array is {min_num}.')