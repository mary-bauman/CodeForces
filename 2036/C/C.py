t = int(input())
for _ in range(t):
    s = list(input().strip())
    n = len(s)
    numQueries = int(input())
    if n<4:
        for _ in range(numQueries):
            input()
            print("NO")
        continue

    occurrences = {i for i in range(len(s) - 3) if s[i:i+4] == ['1', '1', '0', '0']}

    for _ in range(numQueries):
        i, val = input().split()
        i = int(i)-1
        s[i] = val
        small, big = max(0, i-3), min(n-3, i+1)
        for j in range(small,big):
            occurrences.discard(j)
            if s[j:j+4] == ['1', '1', '0', '0']: occurrences.add(j)
        print("YES" if occurrences else "NO")


        