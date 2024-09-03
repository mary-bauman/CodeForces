from collections import defaultdict
tests = int(input())
for t in range(tests):
    rowCount = int(input())
    locations = defaultdict(int)
    for r in range(rowCount):
        s = input()
        i = s.index('#')+1
        locations[r] = i
    ans = ""
    for i in range(rowCount-1, -1, -1):
        ans+=str(locations[i]) + " "
    print(ans[:-1])