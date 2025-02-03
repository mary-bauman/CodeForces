n = int(input())
degrees = [int(input()) for _ in range(n)]
possible = "No"
for mask in range((1 << n)):
    sumOfSubset = 0
    for i in range(n):
        if mask & (1<<i): sumOfSubset += degrees[i]
        else: sumOfSubset -= degrees[i]
    if sumOfSubset%360 == 0:
        possible = "Yes"
        break
print(possible) 