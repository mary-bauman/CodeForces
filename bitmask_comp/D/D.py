for _ in range(int(input())):
    n = int(input())
    k = 1
    #its always the  closest power of 2 not going over minus 1
    #thank you nolan for the trick
    while k<<1 <= n: k <<= 1 
    print(k-1)
