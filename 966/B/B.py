def seatsGood(numPeople, seats):
    seats = [int(x) for x in seats]
    cur = [seats[0]]
    seats = seats[1:]  
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

