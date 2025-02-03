from math import inf
tests = int(input())
for t in range(tests):
    inp = input().split()
    arrayLen = int(inp[0])
    start = int(inp[1])
    minX = inf
    #arr is slow so i gotta make that fast
    #but for now im rolling with slow input
    #so basically trying to find the spot in the arr
    #right before and after a<b
    #and test those vals
    arr = [start + i for i in range(arrayLen)]
    print(arr)
    for i in range(arrayLen):
        a = sum(arr[:i])
        b = sum(arr[i:])
        diff = abs(a-b)
        # print("\na: ", a)
        # print("b: ", b)
        # print("diff = ", diff)
        minX = min(minX, diff)

    print(minX)