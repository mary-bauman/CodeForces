from time import time
t1 = time()

def seatsGood(numPeople, seats):
    # seats = list(map(int, seats))
    #not faster than int(x) for x in seats
    seats = [int(x) for x in seats]
    cur = [seats[0]]
    seats = seats[1:]
    #switching to seats.pop(0) is slower? idk why
    # cur = [seats.pop(0)]    
    for seat in seats:
        if seat-1 in cur or seat+1 in cur:
            cur.append(seat)
        else: return False
    
    if min(cur)<1 or max(cur)>numPeople: return False
    return True

tests = int(input())
for test in range(tests):
    if seatsGood(int(input()), input().split()): print("YES")
    else: print("NO")
t2 = (time()-t1) * 1000
print(f"time = {t2} s")
#time = 0.10180473327636719 s
#time = 0.2760887145996094 s
#time = 0.1621246337890625 s

