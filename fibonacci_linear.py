def fibonacci_l(n):
    """
    Set a fibonacci sequence using recursion method
    """
    a = 0
    b = 1
    if n < 0:
        print('Please enter a positive integer')
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return a + b


print(fibonacci_l(9))

