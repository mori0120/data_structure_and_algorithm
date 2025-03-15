# 再帰の例。
# 同じ関数の呼び出しが重複するため、計算量は多くなる。

def fibo(n: int) -> int:
    print(f'fibo({n}) is called.')
    if n==0:
        return 0
    if n==1:
        return 1
    
    result = fibo(n-1) + fibo(n-2)
    print(f'項目 = {result}')
    return result

n = int(input('fibo(N) will be called.\nN = '))
print(f'result = {fibo(n)}')