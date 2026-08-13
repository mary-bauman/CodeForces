#example
#n = 10, k = 3
#a = [1,3,5,7,9,2,4,6,8,10]
#a[k-1] = 5
#ans = 5
#a[n//2] = a[5] = 2
#a[5] = 2
#if k = 6 then a[5]=2 ans = 2
#if k = 7 then ans = 4
#k = 8 then ans = 6
#k = 9 then ans = 8
#k = 10 then ans = 10
#k is always <= n

#7 7
#a = [1,3,5,7,2,4,6]
#7 1 = 1
#7 2 = 3
#7 3 = 5
#7 4 = 7
#7 5 = 2
#7 6 = 4
#7 7 = 6




n, k = map(int, input().split())

if n % 2 == 0:
    if k < n // 2:
        print((k * 2) - 1)
    else:
        print((k-(n//2))*2)
else:
    if k <= n // 2 + 1:
        print((k * 2) - 1)
    else:
        print((k-(n//2 + 1))*2)