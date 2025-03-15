# 線形探索法の例その2

n = int(input('Total number: '))
target = int(input('Target: '))

array = [int(input(f'array[{_}] = ')) for _ in range(n)]
index = -1

for i in range(n):
    if array[i] == target:
        index = i
        break

print(f'Index of the target in the array is {index}. -1 means that it is not exist.')