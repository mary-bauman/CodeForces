tests = int(input())
for test in range(tests):
    n, m = map(int, input().split())
    numOrdinaryWords = n
    numAbbrev = m
    words = []
    abbrev = []
    for _ in range(n): words.append(input())
    for _ in range(m): abbrev.append(input())