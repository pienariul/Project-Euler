import math
import array
import numpy as np

#Problem 4
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 
#                                                  9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrom(n):
    reverse = 0
    number = n
    while n != 0:
        reverse = reverse * 10 + (n % 10)
        n = int(n / 10)
    
    if number == reverse:
        return True
    else:
        return False

def maxThreeDigitsPalindromNumber():
    arr = []
    for i in range(100, 999):
        for j in range(100, 999):
            product = i * j
            if isPalindrom(product):
                arr.append(product)
    return np.max(arr)
    

print(maxThreeDigitsPalindromNumber())