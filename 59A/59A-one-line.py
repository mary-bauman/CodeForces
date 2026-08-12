word = input()
upperSum = sum(1 for c in word if c.isupper())
lowerSum = sum(1 for c in word if c.islower())
if upperSum > lowerSum:
    print(word.upper())
else:
    print(word.lower())
