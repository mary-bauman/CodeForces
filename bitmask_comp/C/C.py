for _ in range(int(input())):
    zero = 0 
    z = False
    for c in str(input()):
        if c == '1':
            if z:
                zero += 1
                z = False
        else: z = True
    if z: zero += 1
    print(min(zero, 2))

