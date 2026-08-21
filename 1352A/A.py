tests = int(input())
for _ in range(tests):
    i = int(input())
    a = []
    offset = 1
    while i>0:
        if i%10 != 0:
            a.append((i%10) * offset)
        i = i//10
        offset *= 10
    print(len(a))
    print(*a)
        



