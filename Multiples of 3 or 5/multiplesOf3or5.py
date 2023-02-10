import math

def multipleOf3or5(n):
    sum = 0
    for i in range(n):
        if (i%3 == 0) | (i%5 == 0):
            sum = sum + i
    print(sum)

print(multipleOf3or5(1000))


