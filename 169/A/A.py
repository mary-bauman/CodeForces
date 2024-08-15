import math
tests = int(input())
for t in range(tests):
    good = True
    pointsLen = int(input())
    arr = input().split()
    arr = [int(i) for i in arr]
    arr.sort()
    better = []
    for i,a in enumerate(arr):
        m = math.inf
        be = []
        for b in arr[:i]:
            if abs(a-b) < m:
                m = abs(a-b)
                be = [a-m+1, a+m-1]
        for b in arr[i+1:]:
            if abs(a-b) < m:
                m = abs(a-b)
                be = [a-m+1, a+m-1]
        if m==1:
            good = False
            break
        newBe = []
        small = max(be[0], 1)
        big = min(be[1], 100)
        for i in range(small, big+1):
            newBe.append(i)
        better.append(newBe)

    workingOptions = False
    if good:
        options = better[0]
        for option in options:
            if option not in arr:
                optionWorks = True
                for b in better[1:]:
                    if option not in b:
                        optionWorks = False
                        break
                if optionWorks:
                    workingOptions = True
                    break

    if workingOptions: print("YES")
    else: print("NO")

    
