from time import time
startTime = time()

tests = int(input())

for test in range(tests):
    numberOfTasks = int(input())
    tasks = [list(map(float, input().split())) for _ in range(numberOfTasks)]
    memo = {}
    def makeChoice(task, stamina):
        stamina_rounded = round(stamina, 6)
        state = (task, stamina_rounded)
        if state in memo:
            return memo[state]

        if task >= numberOfTasks:
            return 0

        stamina2 = stamina * (1-(tasks[task][1]/100))
        points_from_this_task = stamina * tasks[task][0]

        if stamina2 < stamina:
            doNothing = makeChoice(task + 1, stamina)
            doTask = points_from_this_task + makeChoice(task + 1, stamina2)
            result = max(doNothing, doTask)
        else:
            result = points_from_this_task + makeChoice(task + 1, stamina2)

        memo[state] = result
        return result

    maxPossiblePoints = makeChoice(0, 1)
    print(maxPossiblePoints)
print("Time taken: ", time() - startTime)