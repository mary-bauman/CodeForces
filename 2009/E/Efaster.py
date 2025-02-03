from math import inf
from math import factorial
from time import time
t1 = time()
tests = int(input())
for t in range(tests):
    inp = input().split()
    arrayLen = int(inp[0])
    minX = inf
    a = 0
    wholeThing = ((arrayLen-1)*(arrayLen))//2
    b = wholeThing
    cur = 0
    
    while a+cur < b-cur:
        a, b, cur = a+cur, b-cur, cur+1

    print("second a = ", a)
    print("second b = ", b)
    print("Cur: ", cur)
    print(min(abs(a-b), abs(a+cur-(b-cur))))
print("time: ", time()-t1)
