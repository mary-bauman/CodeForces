from collections import defaultdict

numberOfTestCases = int(input())
for testCase in range(numberOfTestCases):
    numberOfHouses, numberOfRoads = [int(x) for x in input().split()]
    npcRoad = defaultdict(int)
    normRoad = defaultdict(int)
    numberOfNPCs = sum(npcRoad.values())

    for _ in range(numberOfRoads):
        p1, p2, npc = input().split()
        if npc == "1":
            npcRoad[f"{p1}{p2}"] += 1
        else:
            normRoad[f"{p1}{p2}"] += 1
    
    queue = [f"0{x}" for x in range(1,numberOfHouses+1)]
    visited = defaultdict(lambda: defaultdict(int))

    def getRoute():
        global queue
        global visited

        cur = queue.pop(0)

        if len(set(cur[1:])) == numberOfHouses:
            if int(cur[0]) == numberOfNPCs-1:
                for road in npcRoad:
                    if (visited[cur][road] - normRoad[road] < npcRoad[road]) and (cur[-1] in road) and (cur[1] in road):
                        return cur[1:] + cur[1]

            elif int(cur[0]) == numberOfNPCs:
                for road in normRoad:
                    if (visited[cur][road] - npcRoad[road] < normRoad[road]) and cur[-1] in road and cur[1] in road:
                        return cur[1:] + cur[1]
            
        ext = []
        for road in npcRoad:
            if (visited[cur][road] - normRoad[road] < npcRoad[road]) and cur[-1] in road:
                new = str(int(cur[0])+1) + cur[1:] + road.replace(cur[-1], "")
                ext.append(new)
                visited[new] = visited[cur]
                visited[new][road] += 1
            
        for road in normRoad:
            if (visited[cur][road] - npcRoad[road] < normRoad[road]) and cur[-1] in road:
                new = cur + road.replace(cur[-1], "")
                ext.append(new)
                visited[new] = visited[cur]
                visited[new][road] += 1
        
        queue = queue + ext

    route = ""
    while queue:
        route = getRoute()
        if route:
            break
    
    if route:
        print("YES")
        print(len(route)-1)
        ans = route[0]
        for house in route[1:]:
            ans += f" {house}"
        print(ans)
    else: print("NO")

