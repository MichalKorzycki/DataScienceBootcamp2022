print("Importing "+__name__)

my_variable = 7

def fib(n):   # return Fibonacci series up to n
    result = []
    c = 0
    a, b = 0, 1
    while c < n:
        result.append(a)
        a, b = b, a+b
        c+=1
    return result
