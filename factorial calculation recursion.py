def fibo(n):
    if n == 0 or n == 1:
        return n
    return n * fibo(n - 1)


print(fibo(5))
