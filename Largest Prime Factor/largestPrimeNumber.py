import math

#Problem 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?


def largestPrimeFactor(number):
    startPrimeFactor = 2
    while startPrimeFactor*startPrimeFactor < number:
        while number % startPrimeFactor == 0:
            number = number / startPrimeFactor
        startPrimeFactor = startPrimeFactor + 1

    return number

print(largestPrimeFactor(600851475143))
