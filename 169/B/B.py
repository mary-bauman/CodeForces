#credit to nolan
for _ in range(int(input())):
    aliceLeft, aliceRight = [int(x) for x in input().split()]
    bobLeft, bobRight = [int(x) for x in input().split()]

    ans = 0

    if aliceRight < bobLeft or bobRight < aliceLeft: # no overlap
        print(1)
        continue

    # literal edge cases
    if aliceLeft != bobLeft: ans += 1
    if aliceRight != bobRight: ans += 1

    left = max(aliceLeft, bobLeft)
    right = min(aliceRight, bobRight)

    ans += right - left
    print(ans)