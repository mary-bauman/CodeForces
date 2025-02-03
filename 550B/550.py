from math import inf

n, l, r, minDiff = map(int, input().split())
difficulties = list(map(int, input().split()))
numOfCombos = 0

for mask in range(0, (1 << n)):
    sumOfSubset = 0
    smallest = inf
    biggest = -inf
    for i in range(n):
        if mask & (1<<i):
            sumOfSubset+=difficulties[i]
            smallest = min(smallest, difficulties[i])
            biggest = max(biggest, difficulties[i])
    if sumOfSubset >= l and sumOfSubset <= r and biggest-smallest >= minDiff:
        numOfCombos += 1

print(numOfCombos)
