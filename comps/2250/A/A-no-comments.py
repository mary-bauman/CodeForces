def perfectExists(numberBalls, ballWeights):
    if numberBalls == 1: return False

    minK = min(ballWeights)+1
    maxK = max(ballWeights)
    for k in range(minK,maxK):
        if k not in ballWeights:
            plots = [0]*(numberBalls+2)
            for i, weight in enumerate(ballWeights):
                if weight > k:
                    plots[i+2] = weight
                elif weight < k:
                    plots[i] = weight
            
            if plots.count(0) == 2:
                if plots[0] == 0 and plots[-1] == 0:
                    return True

    return False



tests = int(input())
for test in range(tests):
    numberBalls = int(input())
    ballWeights = list(map(int, input().split()))

    if perfectExists(numberBalls, ballWeights):
        print("YES")
    else:
        print("NO")
