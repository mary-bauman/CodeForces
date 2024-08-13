t = int(input())

for _ in range(t):
    n = int(input()) # length of arr
    a = [int(x) for x in input().split()]
    m = int(input()) # number of strings

    for _ in range(m):
        s = input()
        tbl = {}
        good = True

        if len(s) != n:
            print("NO")
            continue



        for i in range(n):
            if s[i] not in tbl:
                tbl[s[i]] = a[i]

            if a[i] != tbl[s[i]]:
                good = False
                break



        if good:
            print("YES")
        else:
            print("NO")
