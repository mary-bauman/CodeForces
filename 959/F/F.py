numberOfTestCases = int(input())
for testCase in range(numberOfTestCases):
    print(" ")
    housesRoads = input().split()
    numberOfHouses = int(housesRoads[0])
    numberOfRoads = int(housesRoads[1])
    arr = []
    for road in range(numberOfRoads):
        arr.append(input().split())
    print(arr)
