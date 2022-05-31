def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


def list_squares(list1):
    for i in list1:
        yield i**2


def evaluate_sum(x):
    ans = 0
    print("N:", x)
    fiblist = list(fibonacci(x))
    print("First", x, "Fibonacci numbers:", fiblist)
    sqlist = list(list_squares(fiblist))
    print("Their Squares:", sqlist)
    print("The sum of the squares of the first N Fibonacci numbers:")
    for i in sqlist:
        ans += i
    return ans


print(evaluate_sum(10))
