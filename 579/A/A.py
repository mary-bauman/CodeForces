# print(bin(int(input())).count('1'))
print(int(input()).bit_count())

# curr = int(input())
# total = 0
# while curr != 0:
#   if curr & 1: total += 1
#   curr >>= 1
# print(total)