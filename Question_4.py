def fib_seq(n):
    if n <= 1:
        return n
    else:
        return fib_seq(n-1)+fib_seq(n-2)