# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a<b<c, for which,

#                           a^2 + b^2 = c^2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000
# Find the product a*b*c


import math

for a in range(1,500):
    for b in range (1,500):
        c = int(math.sqrt(a*a + b*b))
        if a*a + b*b == c*c:
            if a+b+c == 1000:
                if a<b & b<c :
                    print("The numbers are :", a, b, c)
                    print("The product is :", a*b*c)