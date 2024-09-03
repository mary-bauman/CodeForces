testCases = int(input())
for t in range(testCases):
    inp = input().split()
    a = int(inp[0])
    b = int(inp[1])
    minC = (b-a)
    for c in range(a, b):
        minC = min(minC, abs(c-a)+abs(c-b))
    print(minC)

    
