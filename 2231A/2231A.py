with open('in.txt', 'r') as f:
    numTestCases = int(f.readline())
    for _ in range(numTestCases):
        n = int(f.readline())
        if n == 1: print(1)
        elif n == 2: print("1 2")
        else:
            curArray = [1,2]
            totals = [1,2,3]
            cur = 4
            while len(curArray) < n:
                #add to cur
                while cur in totals: cur+=1
                totals.append(cur)
                totals.append(curArray[-1]+cur)
                curArray.append(cur)
                cur += 1
     
            print(curArray)
        
        