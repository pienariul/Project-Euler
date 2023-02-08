import math
import numpy as np


first = 1
second = 2

sum = 0

while sum<40000:
    sum = first + second
    first = second
    second = sum
    print(sum)

print(type('s'))