tests = int(input())
for test in range(tests):
    n = int(input())
    a = list(map(int, input().split()))
    #a only contains 0s and 1s
    #bessie using max to make 0 next to 1 into 1
    #elsie using min to make 1 next to 0 into 0
    #neither cares about 00 or 11

    bTurn = True
    while len(a)>1:
        # print(a)
        #find first 0 next to 1
        #regardless of who's turn it is
        newA = []
        for i in range(len(a)-1):
            if a[i] != a[i+1]:
                if bTurn:
                    newA.append(1)
                    newA += a[i+2:]
                else:
                    newA.append(0)
                    newA += a[i+2:]
                bTurn = not bTurn
                break
            else:
                newA.append(a[i])
        a = newA.copy()



    # print(a)
    if a == [1]: print("Bessie")
    else: print("Elsie")