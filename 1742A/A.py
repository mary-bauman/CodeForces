tests = int(input())
for test in range(tests):
    a = [int(i) for i in input().split()]
    a.sort()
    if (a[0] + a[1] == a[2]):
        print("YES")
    else:
        print("NO")
