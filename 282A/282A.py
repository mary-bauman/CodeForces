tests = int(input())
x = 0
for test in range(tests):
    op = str(input())
    if "+" in op: x+=1
    else: x-=1
print(x)

    