testCases = int(input())
for testCase in range(testCases):
    inp = input().split()
    ones = int(inp[0])
    twos = (int(inp[1])%2)*2
    if ones>=twos:
        twos = ones-twos
        print("YES") if twos%2==0 else print("NO")
    else:
        print("NO")
    