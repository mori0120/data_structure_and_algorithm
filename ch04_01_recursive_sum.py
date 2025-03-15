# 再帰関数の例

def recursive_sum(n: int):
    if n==0:
        return 0
    return n + recursive_sum(n-1)

print(recursive_sum(int(input('Total num: '))))