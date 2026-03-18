tests = int(input())
for test in range(tests):
    numberOfTasks = int(input())
    tasks = []
    for _ in range(numberOfTasks):
        #each task is c,p
        #c is int, p is difficulty
        tasks.append(list(map(int, input().split())))
    maxPossiblePoints = 0.0
    initialStamina = 1
    


    print(maxPossiblePoints)