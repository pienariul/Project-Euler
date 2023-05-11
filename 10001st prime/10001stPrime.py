import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    
counterNumberPrime = 0
number = 0

while counterNumberPrime < 10001:
    if is_prime(number):
        counterNumberPrime+= 1
    number += 1

print(number-1)