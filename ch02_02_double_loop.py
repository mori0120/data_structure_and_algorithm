# 計算量O(n^2)の例

n = int(input('Number: '))
count = 0
for i in range(n):
    for j in range(n):
        count += 1
