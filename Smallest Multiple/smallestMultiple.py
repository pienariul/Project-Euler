#Problem 5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def find_smallest_multiple(n):
    current_number = 1
    while True:
        divisible = True
        for i in range(1, n):
            if current_number % i != 0:
                divisible = False
                break
        if divisible:
            return current_number
        current_number += 1

smallest_multiple = find_smallest_multiple(10)
print(smallest_multiple)