from collections import defaultdict

numberOfTestCases = int(input())
for testCase in range(numberOfTestCases):
    print(" ")
    numberOfHouses,numberOfRoads = [int(x) for x in input().split()]
    
    connections = defaultdict(list)
    for road in range(numberOfRoads):
        roadPoint1, roadPoint2, c = input().split()
        if c == "1":
            connections[roadPoint1].append(roadPoint2)
            connections[roadPoint2].append(roadPoint1)
    print(connections)
    route = ""

    queue = [f"{x}" for x in range(1, numberOfHouses+1)]
    while queue:
        print(queue)
        cur = queue.pop(0)

        if len(cur) == numberOfHouses:
            print("len(cur) == numberOfHouses")
            if cur[0] in connections[cur[-1]]:
                print("break for route = ", cur)
                route = cur
                break
        
        ext = []
        for i in connections[cur[-1]]:
            if str(i) not in cur:
                ext.append(cur + str(i))

        print("ext:", ext)
        queue = queue + ext
    print(queue)
    print("route = ", route)
    if route:
        print("Yes")
        print(len(route))
        print(route)
    else: print("No")

