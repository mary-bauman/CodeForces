# tests = int(input())
# for test in range(tests):
#     b, a, k = map(int, input().split())
#     total = 0
#     diff = a - b
#     for month in range(k):
#         total += (diff % (b + month))

#     print(total)



# tests = int(input())
# for test in range(tests):
#     b, a, k = map(int, input().split())
#     diff = a - b
#     total = sum(diff % (b + i) for i in range(k))
#     print(total)






#had to use ai to understand the math optimization so I didn't submit this one 
#but it works

# tests = int(input())

# for _ in range(tests):
#     b, a, k = map(int, input().split())

#     diff = a - b
#     end = b + k - 1
#     total = 0
#     x = b

#     while x <= end:
#         # Once x > diff, diff % x == diff
#         if x > diff:
#             total += diff * (end - x + 1)
#             break

#         q = diff // x
#         r = min(end, diff // q)

#         # Sum diff - q*x for x in [x, r]
#         count = r - x + 1
#         sum_x = (x + r) * count // 2

#         total += diff * count - q * sum_x
#         x = r + 1

#     print(total)