tests = int(input())
for t in range(tests):
    # print("\n")
    arr = input().split()
    items = int(arr[0])
    k = int(arr[1])
    costs = input().split()
    costs = [int(c) for c in costs]
    costs.sort(reverse=True)
    # print("items = ", items)
    # print("k = ", k)
    # print("costs = ", costs)
    bob = 0
    alice = 0
    #score will be alice-bob
    #both trying to have big scores

    aliceTurn = True
    for i,cost in enumerate(costs):
        if aliceTurn:
            alice+=cost
        else:
            bob+=cost
            # print("\nelse")
            # print("bob = ", bob)
            # print("k = ", k)
            # print("i = ", i)
            if k!=0:
                diff = costs[i-1]-cost
                change = min(diff,k)
                bob+=change
                k-=change
        aliceTurn = not aliceTurn
    print(alice-bob)
    # print("costs = ", costs)
    # print("bob = ", bob)
    # print("alice = ", alice)