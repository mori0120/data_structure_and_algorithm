# 偶数の列挙。計算量O(n)の例

n = int(input('Number: '))
for i in range(2, n+1, 2):
    print(i)