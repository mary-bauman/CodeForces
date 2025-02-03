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
    #sum of the whole thing (besides start)
    wholeThing = ((arrayLen-1)*(arrayLen))//2
    b = wholeThing
    cur = 0

    if arrayLen > 200000000:
        #arrayLen = 100000000
        a = 2499999915742968
        b = wholeThing - a
        cur = 70623205
    elif arrayLen > 85000000:
        #arrayLen = 80000000
        a = 1599999923919261
        b = wholeThing - a
        cur = 56459163
    elif arrayLen > 10000000:
        #arrayLen = 5000000
        a = 6249998564811
        b = wholeThing - a
        cur = 370378
    elif arrayLen > 1500000:
        #arrayLen = 100000
        a = 2499916695
        b = wholeThing - a
        cur = 70710
    elif arrayLen > 50000:
        #arrayLen = 5000
        a = 6246345
        b = wholeThing - a
        cur = 3535
    elif arrayLen > 500:
        #arrayLen = 100 stuff
        a = 2415
        b = wholeThing - a
        cur = 70
    # if arrayLen > 18000000:
    #     a = 24999990723711
    #     b = 25000004276289
    #     cur = 7071067


    
    while a+cur < b-cur:
        a, b, cur = a+cur, b-cur, cur+1

    print("second a = ", a)
    print("second b = ", b)
    print("Cur: ", cur)
    print(min(abs(a-b), abs(a+cur-(b-cur))))
print("time: ", time()-t1)
