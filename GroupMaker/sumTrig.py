# Chris Allulis
# What does this progam do?

import math

sumSin = 0.00
sumCos = 0.00

for deg in range(1,360):
    rad = math.radians(deg)
    sumSin += math.sin(rad)
    sumCos += math.cos(rad)

"""
sumSin = math.degrees(sumSin)
sumCos = math.degrees(sumCos)
"""

print sumSin
print sumCos