"""
Given a number, we have to return its factorial
For example: Factorial of 5 is : 5*4*3*2*1 = 120
we can solve it both iteratively and recursively
Lets solve it iteratively first

There are 3 steps to recursion:
1. Identify the base case
2. Identify the recursive case
3. Get closer and closer and return when needed. Usually you have 2 returns
"""


# using iterative method
def calculate_factorial_iteratively(num):
    factorial = 1

    # using while loop
    # while num != 0:
    #     factorial = factorial * num
    #     num -= 1
    # print(factorial)

    # using for loop
    for i in range(1, num + 1):
        factorial *= i
    print(factorial)


def calculate_factorial_recursively(num):
    if num <= 1:
        return 1
    else:
        return num * calculate_factorial_recursively(num - 1)


calculate_factorial_iteratively(5)
print(calculate_factorial_recursively(5))
