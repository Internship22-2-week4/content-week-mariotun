def cuenta_regresiva(n):
    while n > 0:
        print(n)
        n -= 1


def cuenta_regresiva_2(n):
    while n < 10:
        print(n)
        n += 1


def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b


cuenta_regresiva(5)
print('-'*30)
cuenta_regresiva(-1)
print('-'*30)
cuenta_regresiva_2(1)
print('-'*30)
fib1 = fibonacci(20)
fib_nums = [num for num in fib1]
print(fib_nums)