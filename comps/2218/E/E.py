from math import inf


def operation(a, nLeft):
    print()
    print(f"a = {a}, nLeft = {nLeft}")
    if nLeft == 0: return max(a)
    
    bestArrLeft = -inf
    bestArr = []
    for i in range(nLeft+1):
        print(f"bestArrLeft = {bestArrLeft}, bestArr = {bestArr}")
        x = a[i]
        newA = []
        for j in range(nLeft+1):
            newA.append(a[j] ^ x)
        del newA[i]
        m = operation(newA, nLeft-1)
        if m > bestArrLeft:
            bestArrLeft = m
            bestArr = newA
    
            
    return bestArrLeft



tests = int(input())
for test in range(tests):
    n = int(input())
    a = list(map(int, input().split()))

    print(operation(a, n-1), "is the ans")
  


