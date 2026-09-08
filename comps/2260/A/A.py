def calc(probs):
    if probs.count(0)<2: return(-1)
    return (probs[0]+probs[-1])


tests = int(input())
for test in range(tests):
    n = int(input())
    probs = list(map(int, input().split()))
    print(calc(probs))