# ペアの全探索
# K以上となるペア和の最小値

import sys

n = int(input('Num of array: '))
k = int(input('Minimun num of a[i]+b[j]: '))
a = [int(input(f'a[{_}] = : ')) for _ in range(n)]
b = [int(input(f'b[{_}] = : ')) for _ in range(n)]

min_num = sys.maxsize

for i in range(n):
    for j in range(n):
        if a[i]+b[j]<k:
            continue

        if min_num > a[i]+b[j]:
            min_num = a[i]+b[j]

print(f'The minimum sum of the pairs which is greater than or equal to {k} is {min_num}.')