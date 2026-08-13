#example
#n = 10, k = 3
#a = [1,3,5,7,9,2,4,6,8,10]
#a[k-1] = 5
#ans = 5

n, k = map(int, input().split())
a = [i for i in range(1, n+1, 2)]+[i for i in range(2, n+1, 2)]
print(a[k-1])