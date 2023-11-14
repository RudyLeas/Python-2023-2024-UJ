def fibonacci(n):
    if n < 0:
        return "Number should be greater than 0."
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return a+b

# example use:
n = 4

print(fibonacci(n))
