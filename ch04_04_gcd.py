def gcd(m: int, n: int) -> int:
    if n==0:
        return m
    return gcd(n, m%n)

m = int(input('m = '))
n = int(input('n = '))
print(gcd(m, n))