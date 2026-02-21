testCases = int(input())
for _ in range(testCases):
    line = input().strip()
    if len(line) <= 10: print(line)
    else: print(line[0] + str(len(line)-2) + line[-1])