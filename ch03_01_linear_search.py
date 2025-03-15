# 線形探索法の例

n = int(input('Total number: '))
target = int(input('Target: '))

array = [int(input(f'array[{_}] = ')) for _ in range(n)]
exist = False

for i in range(n):
    if array[i] == target:
        exist = True

print('Exist' if exist else 'Not exist')