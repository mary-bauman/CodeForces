tests = int(input())
for test in range(tests):
    numberOfTasks = int(input())
    tasks = []
    for _ in range(numberOfTasks):
        #each task is c,p
        #c is int, p is difficulty
        tasks.append(list(map(float, input().split())))
    # print("tasks: ", tasks)

    def makeChoice(task, stamina, points):
        if task >= numberOfTasks: 
            # print(f"at {points} points: no more tasks")
            return points
        
        c, difficulty = tasks[task]

        # print(f"c: {c}, difficulty: {difficulty}, stamina: {stamina}, points: {points}")

        
        # print("about to doNothing")
        doNothing = float(makeChoice(task + 1, stamina, points))

        #do task
        points += stamina * c
        stamina *= (1-(difficulty/100))
        # print("about to do task")
        doTask = float(makeChoice(task + 1, stamina, points))

        return max(doNothing, doTask)

    maxPossiblePoints = makeChoice(0, 1, 0)
    print(maxPossiblePoints)