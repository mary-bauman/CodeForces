from collections import defaultdict
tests = int(input())
for t in range(tests):
    line = input().split()
    numShelves = int(line[0])
    numBottles = int(line[1])
    bottles = defaultdict(list)
    for i in range(numBottles):
        line = input().split()
        brand = int(line[0])
        cost = int(line[1])
        bottles[brand].append(cost)

    shelves = []
    for brand in bottles:
        shelves.append(sum(bottles[brand]))
    shelves.sort(reverse=True)

    if len(shelves)<numShelves: print(sum(shelves))
    else: print(sum(shelves[:numShelves]))