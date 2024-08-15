for _ in range(int(input())): # for each testcase
    n = int(input()) # length of arr
    a = [int(x) for x in input().split()]

    for _ in range(int(input())): # for each string
        s = input()
        stbl = {}
        atbl = {}
        good = True

        if len(s) != n:
            print("NO")
            continue

        for i in range(n):
            if s[i] not in stbl:
                stbl[s[i]] = a[i]

            if a[i] not in atbl:
                atbl[a[i]] = s[i]

            if a[i] != stbl[s[i]]:
                good = False
                break

            if s[i] != atbl[a[i]]:
                good = False
                break

        if good:
            print("YES")
        else:
            print("NO")
