#Problem 6
#The sum of the squares of the first ten natural numbers is,
#              1**2 + 2**2 + ... + 10**2 = 385
#The square of the sum of the first ten natural numbers is,
#              (1 + 2 + ... + 10)**2 = 55**2 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
#               3025 - 385 = 2640
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def number_square_sum(n):
    return sum(i*i for i in range(n+1))

def square_sum_numbers(n):
    sum_n = (n * (n + 1)) // 2
    square_sum = sum_n**2
    return square_sum

result = square_sum_numbers(100) - number_square_sum(100)
print(result)