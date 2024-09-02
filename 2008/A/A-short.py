for testCase in range(int(input())):
    ones, twos = [int(x) for x in input().split()]
    print("NO") if (ones<twos or (ones-twos)%2!=0) else print("YES")