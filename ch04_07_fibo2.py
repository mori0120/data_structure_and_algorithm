# メモ化、キャッシュ化を用いて計算量を改善する。

n = int(input('fibo(N) will be called.\nN = '))
array: list[int] = [0] * (n+1)
array[1] = 1

for i in range(2, n+1):
    array[i] = array[i-2] + array[i-1]
    print(f'項目 = {array[i]}')