from collections import defaultdict

tests = int(input())
for test in range(tests):
    boardSize = int(input())
    board = []
    s = defaultdict(int)
    for t in range(boardSize):
        line = input().split()
        board.append(line)
        for c in line: s[c] += 1
    exists = True
    limit = boardSize

    # 1 2
    # 2 1

    # 1 1 2
    # 2 1 1
    # 1 2 1

    # 1 1 1 2
    # 1 1 2 1
    # 1 2 1 1
    # 2 1 1 1

    # if boardSize == 2: limit = 2
    # elif boardSize == 3: limit = 6
    # elif boardSize == 4: limit = 12


    limit = (boardSize-1)* boardSize

    for c in s:
        if s[c] > limit:
            exists = False
            break
    
    if exists: print("YES")
    else: print("NO")
