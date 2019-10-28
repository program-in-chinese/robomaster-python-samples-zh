# 源于 https://gist.github.com/apalala/3fbbeb5305584d2abe05
from math import sin, cos, radians
import time
def bench():
    t1 = time.time()
    product = 1.0
    for counter in range(1, 1001):
        product *= calculate()
    t2 = time.time() - t1
    print(t2)
    return product

def calculate():
    product = 1.0
    for dex in range(1, 360):
        angle = radians(dex)
        product *= sin(angle)**2 + cos(angle)**2
    return product