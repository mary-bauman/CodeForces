with open('in.txt', 'r') as f:
    numTestCases = int(f.readline())
    for _ in range(numTestCases):
        n = int(f.readline())
        if n == 1: print(1)
        elif n == 2:
            options = [1,2,3,4]
            #any 2 would work
            print("1 2")
        elif n == 3:
            options = [1,2,3,4,5,6]
            #still so many options
            #the lower outside + inside cannot = the other outside

            
            
        else:
            a = [0] * n
            options = []
            for i in range(1,2*n+1):
                options.append(i)
        
        