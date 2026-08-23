tests = int(input())
for test in range(tests):
    n, m = map(int, input().split())
    words, abbrev = set(), set()
    for _ in range(n): words.add(input()[0].upper())
    for _ in range(m): abbrev.add(input())

    def checkAbbrev():
        for a in abbrev:
            for char in a:
                if char not in words: return False
        return True

    if checkAbbrev(): print("YES")
    else: print("NO")

            