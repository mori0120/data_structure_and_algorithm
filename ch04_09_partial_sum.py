# 再帰を用いた部分和問題。
# N個の問題をN-1個の問題へ分割して考える分割統治法

def func(i: int, w: int, arr: list[int]) -> bool:
    if i==0:
        return True if w==0 else False
    
    if func(i-1, w, arr):
        return True
    
    if func(i-1, w-arr[i-1], arr):
        return True
    
    return False


n = int(input('N = '))
w = int(input('W = '))
arr = [int(input(f'array[{x}] = ')) for x in range(n)]

result = 'Yes' if func(n, w, arr) else 'No'
print(result)