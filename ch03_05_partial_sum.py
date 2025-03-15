# 部分和問題: 与えられた配列の部分和に指定の値wが存在するか。

n = int(input('Number of the array: '))
w = int(input('Target sum: '))
array = [int(input(f'array[{_}] = ')) for _ in range(n)]
exist = False

for bit in range(1 << n):
    sum = 0
    for i in range(n):
        if bit & (1 << i):
            sum += array[i]
    if sum == w:
        exist = True
        break

print('Yes' if exist else 'No')