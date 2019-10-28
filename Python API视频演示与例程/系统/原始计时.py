# 源于 https://gist.github.com/apalala/3fbbeb5305584d2abe05
from math import sin, cos, radians
import time
def bench():
    t1 = time.time()
    product = 1.0
    for counter in range(1, 1000, 1):
        for dex in list(range(1, 360, 1)):
            angle = radians(dex)
            product *= sin(angle)**2 + cos(angle)**2
    t2 = time.time() - t1
    print(t2)
    return product