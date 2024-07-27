from collections import defaultdict

numberOfTestCases = int(input())
for testCase in range(numberOfTestCases):
    print(" ")
    numberOfHouses,numberOfRoads = [int(x) for x in input().split()]
    npcRoad = []
    normRoad = []

    for _ in range(numberOfRoads):
        p1, p2, npc = input().split()
        if npc == "1":
            npcRoad.append(f"{p1}{p2}")
        else:
            normRoad.append(f"{p1}{p2}")
    
    print("npc",npcRoad)
    print("norm",normRoad)
    print("NPCs",len(npcRoad))
    
    queue = [f"0{x}" for x in range(1,numberOfHouses+1)]
    visited = defaultdict(list)
    route = ""

    def getRoute():
        global queue
        global visited
        global route
        cur = queue.pop(0)

        if len(set(cur[1:])) == numberOfHouses:
            print("full house:", cur)
            if int(cur[0]) == len(npcRoad)-1:
                for road in npcRoad:
                    print(f"for npc road {road} in {npcRoad}")
                    print(road not in visited)
                    print((cur[-1] in road))
                    print((cur[1] in road))
                    if (road not in visited) and (cur[-1] in road) and (cur[1] in road):
                        return cur[1:] + cur[1]


            elif int(cur[0]) == len(npcRoad):
                for road in normRoad:
                    print(f"for norm road {road} in {normRoad}")
                    print(road not in visited)
                    print((cur[-1] in road))
                    print((cur[1] in road))
                    if road not in visited and cur[-1] in road and cur[1] in road:
                        return cur[1:] + cur[1]
            
            
        ext = []
        for road in npcRoad:
            if road not in visited[cur] and cur[-1] in road:
                new = str(int(cur[0])+1) + cur[1:] + road.replace(cur[-1], "")
                ext.append(new)
                visited[new] = visited[cur] + [road]
            
        for road in normRoad:
            if road not in visited[cur] and cur[-1] in road:
                new = cur + road.replace(cur[-1], "")
                ext.append(new)
                visited[new] = visited[cur] + [road]
        
        queue = queue + ext

    while queue:
        route = getRoute()
        if route:
            break
        

        
    print("route = ", route)
    if route:
        print("Yes")
        print(len(route))
        print(route)
    else: print("No")

