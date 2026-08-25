def sequenceToSingleDigit(s, c):
    if len(s)==1: return s == c
    for i in range(len(s)-1):
        #reduce the two digits
        newS = s[:i]+str((int(s[i])+int(s[i+1]))%10)+s[i+2:]
        if sequenceToSingleDigit(newS, c): return True
    return False


def run(a, b):
    if a == b: return "YES"
    if len(a)==1:
        #try to bring b down to the single digit a[0]
        if sequenceToSingleDigit(b, a[0]): return "YES"
    if len(b)==1:
        #try to bring a down to the single digit b[0]
        if sequenceToSingleDigit(a, b[0]): return "YES"


    #switch any two digits in a. b stays the same
    


    #switch any two digits in b. a stays the same


    #nothing worked
    return "NO"

        




tests = int(input())
for _ in range(tests):
    print(run(input(),input()))

   
