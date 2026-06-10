def solve(s, cur, left): #brute force backtracking for n<10^5
    # print(f"sum = {s}, cur = {cur}, left = {a}")

    if not left: return (s, cur, left)

    if cur and len(cur)%3==0:
        prev = sorted(cur[-3:])
        s += int(prev[1])

    if len(left)==3:
        s += sorted(left)[1]
        cur += " " + " ".join(str(i) for i in left)
        return (s, cur, [])

    newS = s
    newCur = cur
    newLeft = left

    for i in left:
        cur2 = cur + " " + str(i)
        left2 = left.copy()
        left2.remove(i)
        s2, cur2, left2 = solve(s, cur2, left2)
        if s2 > newS:
            newS = s2
            newCur = cur2
            newLeft = left2.copy()


    return solve(newS, newCur, newLeft)



tests = int(input())
for test in range(tests):
    n = int(input())
    # print()
    # print(n)
    a = list(range(1, 3*n + 1))
    s, cur, a = (solve(0, "", a))
    print(cur[1:])
    