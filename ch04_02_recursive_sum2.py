def recursive_sum(n: int) -> int:
    print(f'{n}を呼び出しました。')

    if n==0:
        return 0
    
    result = n + recursive_sum(n-1)
    print(f'{n}までの和 = {result}')
    
    return result

recursive_sum(int(input('N = ')))