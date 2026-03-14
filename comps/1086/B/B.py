tests = int(input())
for test in range(tests):
    #n,k=numPlayableCards,p,m
    numCards, k, winPosition, availEnergy = map(int, input().split())
    cardCosts = list(map(int, input().split()))
    ans = 0
    while availEnergy >= min(cardCosts[:k]):
        # print(f"cardCosts: {cardCosts}, availEnergy: {availEnergy}, winPosition: {winPosition}")
        while k < winPosition:
            i = cardCosts.index(min(cardCosts[:k]))
            cost = cardCosts[i]
            availEnergy -= cost
            cardCosts.remove(cost)
            cardCosts.append(cost)
            winPosition -= 1
        #now we can play winPisition
        cost = cardCosts[winPosition-1]
        if availEnergy < cost: availEnergy = -1
        else:
            cost = cardCosts[winPosition-1]
            availEnergy -= cost
            cardCosts.remove(cost)
            cardCosts.append(cost)
            winPosition = numCards
            ans += 1
    # print(f"Final cardCosts: {cardCosts}, availEnergy: {availEnergy}, winPosition: {winPosition}")
    print(ans)
    # print()