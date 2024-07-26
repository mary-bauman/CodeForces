def printarr(arr):
    print(arr[0], end="")
    for x in arr[1:]:
        print(f" {x}", end="")
    print()

def solve():
    n, m = [int(x) for x in input().split()]

    a = []
    for i in range(n):
        a.append([int(x) for x in input().split()])

    if n * m == 1:
        print(-1)
        return

    if n > 1:
        for row in a[1:] + a[0:1]:
            printarr(row)
    else:
        printarr(a[0][1:] + a[0][0:1])

for _ in range(int(input())):
    solve()
