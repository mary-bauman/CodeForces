word = input()
if sum(1 for c in word if c.isupper()) > (len(word)//2): print(word.upper())
else: print(word.lower())
