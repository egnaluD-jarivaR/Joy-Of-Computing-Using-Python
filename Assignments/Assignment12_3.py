'''
    R
    |\
    |  \ 
    |    \X
  y |   /  \
    | /      \
    |__________P
    Q    x

Theorem: In a right angled triangle the mid point of the hypotenuse is equidistant from its vertices.
That is,
Px = QX = RX
Therefore QX = z = sqrt(x ** 2 + y ** 2) / 2
By Cosine Rule
cos(theta) = (z ** 2 + y ** 2 - z ** 2) / (2 * y * z)
Therefore, cos(theta) = y / sqrt(x ** 2 + y ** 2)
theta = acos(y / sqrt(x ** 2 + y ** 2))
'''


import math

def solve():
    x = int(input())
    y = int(input())
    denominator = math.sqrt(y * y + x * x)
    theta = round(math.acos(y / denominator) * (180 / math.pi))
    print(theta)
    return

solve()
