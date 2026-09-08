from math import inf

tests = int(input())
for _ in range(tests):
    x, y = map(int, input().split())
    maxValue = -inf
    minChanges = inf

    