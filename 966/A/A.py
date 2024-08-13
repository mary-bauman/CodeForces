tests = int(input())
for test in range(tests):
    t = str(input())
    good = True
    if len(t)<3: good = False
    else:
        if t[:2] != "10": good = False
        if t[2] == "0": good = False
        if int(t[2:])<2: good = False
        
    if good: print("YES")
    else: print("NO")
