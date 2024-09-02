t = int(input())
for test in range(t):
    LR = input().split()
    left = int(LR[0])
    right = int(LR[1])
    if left == right:
        print(1)
        continue
    count = 0
    prev = 0
    diff = 0
    upNext = left+diff
    while upNext < right-diff:
        count+=1
        diff+=1
        prev = upNext
        upNext+=diff
    print(count+1)  
        
