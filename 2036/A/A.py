tests = int(input())
for t in range(tests):
    numNotes = int(input())
    notes = input().split()
    perfect = True
    for i in range(1,numNotes):
        diff = abs(int(notes[i]) - int(notes[i-1]))
        if not (diff==5 or diff==7):
            perfect = False
            break



    if perfect: print ("YES")
    else: print("NO")