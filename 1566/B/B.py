#nolans code

for _ in range(int(input())):
    s = input()
    n = int(s, 2)

    cnt = 0
    cnt += (n & 1) == 0

    for mask in range(1, len(s)):
        d = (n>>mask) & 1
        if d == 0 and d != ((n>>(mask-1)) & 1):
            cnt += 1

    match cnt:
        case 0: print(0)
        case 1: print(1)
        case _: print(2)