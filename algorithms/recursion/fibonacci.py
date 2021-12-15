"""
    Fibonacci numbers, commonly denoted as F(n) form the Fibonacci sequence where each number is a sum of its
    two preceding numbers starting from 0 and 1.
    F(0) = 0, F(1) = 1
    F(n) = F(n-1) + F(n-2), for n > 1

    Example: Input : n=2
    F(2) = F(2-1) + F(2-2) =  F(1) + F(0) = 1 + 0 = 1
    Given a number N, return the index value of the fibonacci sequence
    Sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
    Fibo

"""
from itertools import repeat


def fibonacciIterative2(index):
    a, b = 0, 1
    for _ in repeat(None, index):
        a, b = b, a + b
    return a


# Time complexity: O(n)
def fibonacciIterative(index):
    first_number = 0
    second_number = 1
    if index == 0:
        return first_number
    if index == 1:
        return second_number

    fib_seq = [first_number, second_number]
    third_number = 0
    for i in range(2, index + 1):
        third_number = first_number + second_number
        first_number = second_number
        second_number = third_number
        fib_seq.append(third_number)

    print(fib_seq)
    return third_number


# Time complexity: O(2^n)
def fibonacciRecursive(index):
    if index < 2:
        return index
    else:
        return fibonacciRecursive(index - 2) + fibonacciRecursive(index - 1)


print(fibonacciIterative2(0))
print(fibonacciIterative2(5))
print(fibonacciIterative2(9))
print(fibonacciIterative2(4))
print("******************")
print(fibonacciIterative(5))
print(fibonacciIterative(9))
print(fibonacciIterative(4))
print("******************")
print(fibonacciRecursive(5))
print(fibonacciRecursive(9))
print(fibonacciRecursive(4))
