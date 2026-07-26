def perfectExists(numberBalls, ballWeights):
    # print()
    # print("numberBalls: ", numberBalls)
    # print("ballWeights: ", ballWeights)
    if numberBalls == 1: return False

    minK = min(ballWeights)+1
    maxK = max(ballWeights)
    for k in range(minK,maxK):
        if k not in ballWeights:
            #plots = [] + ballWeights + []
            #we need plots to remain
            #plots = [] + weights in any order + []
            # print("k: ", k)
            plots = [0]*(numberBalls+2)
            for i, weight in enumerate(ballWeights):
                if weight > k:
                    plots[i+2] = weight
                elif weight < k:
                    plots[i] = weight
            #should only be two 0s in the correct spot
            # print("plots: ", plots)
            # print("plots.count(0): ", plots.count(0))
            if plots.count(0) == 2:
                if plots[0] == 0 and plots[-1] == 0:
                    # print("perfect exists for k: ", k)
                    return True
            #     else:
            #         print("0s in wrong spot for k: ", k)
            # print()

    return False



tests = int(input())
for test in range(tests):
    numberBalls = int(input())
    ballWeights = list(map(int, input().split()))

    if perfectExists(numberBalls, ballWeights):
        print("YES")
    else:
        print("NO")
