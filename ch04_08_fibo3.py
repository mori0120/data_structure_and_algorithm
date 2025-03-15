n = int(input('fibo(N) will be called.\nN = '))
cache: list[int] = [-1] * (n+1)

def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if cache[n] != -1:
        return cache[n]
    cache[n] = fibo(n-1) + fibo(n-2)
    return cache[n]

fibo(n)
for i in range(2, n+1):
    print(f'項目 = {cache[i]}')