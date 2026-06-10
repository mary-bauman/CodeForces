tests = int(input())
for test in range(tests):
    line = list(map(int, input().split()))
    m = line.index(max(line))
    line = [x*(-1) for x in line]
    line[m] = line[m]*(-1)
    print(sum(line))