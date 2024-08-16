tests = int(input())
for t in range(tests):
    items, k = map(int, input().split())
    costs = list(map(int, input().split()))
    costs.sort(reverse=True)
    alice, bob = 0, 0
    aliceTurn = True
    for i,cost in enumerate(costs):
        if aliceTurn: alice+=cost
        else:
            change = min((costs[i-1]-cost),k)
            bob+=(cost + change)
            k-=change         
        aliceTurn = not aliceTurn
    print(alice-bob)