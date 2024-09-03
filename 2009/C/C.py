tests = int(input())
for t in range(tests):
    inp = input().split()
    goalX = int(inp[0])
    goalY = int(inp[1])
    dist = int(inp[2])
    Xmoves = 0
    Ymoves = 0

    if goalX !=0:
        Xmoves += goalX//dist
        if goalX%dist != 0:
            Xmoves += 1
    if goalY !=0:
        Ymoves += goalY//dist
        if goalY%dist != 0:
            Ymoves += 1
    
    #accounts for alternating
    if Ymoves > Xmoves:
        print(Ymoves*2)
    elif Xmoves == Ymoves:
        print(Ymoves*2)
    else:
        print((Xmoves*2-1))