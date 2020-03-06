def recur_fibonacci(n):
    """
    Set a fibonacci sequence using recursion method
    """
    
    if n>= 0 and n <= 1:
        return n
    else:
        return (recur_fibonacci(n-1) + recur_fibonacci(n-2))

n_term = int(input('Enter the integer number between 0 and 30: '))
if n_term < 0:
    print('Please enter a positive integer')
elif n_term > 30 :
    print('The number is too large')
else:
    print('The fibonacci of', n_term, 'is', recur_fibonacci(n_term))