from collections import defaultdict, Counter

#gonna organize this whole thing by 0-4
#place = [[must be], [cannot be]]
zero = [[], []]
one = [[], []]
two = [[], []]
three = [[], []]
four = [[], []]
letters = defaultdict(list)

guesses, words = map(int, input().split())
for _ in range(guesses):
    guess, result = map(str, input().split())
    #lettersGuess[letter] = [cappedAmount]
    lettersGuess = dict()
    for i in range(5):
        r = result[i]
        c = guess[i]
        if r =="G":
            match i:
                case 0: zero[0].append(c)
                case 1: one[0].append(c)
                case 2: two[0].append(c)
                case 3: three[0].append(c)
                case 4: four[0].append(c)
            if c in lettersGuess:
                lettersGuess[c][0] += 1 
            else:
                lettersGuess[c] = [1,False] 
        elif r=="-":
            match i:
                case 0: zero[1].append(c)
                case 1: one[1].append(c)
                case 2: two[1].append(c)
                case 3: three[1].append(c)
                case 4: four[1].append(c)
            if c in lettersGuess:
                lettersGuess[c][1] = True
            else:
                lettersGuess[c] = [0,True]
        else: #r == "Y"
            match i:
                case 0: zero[1].append(c)
                case 1: one[1].append(c)
                case 2: two[1].append(c)
                case 3: three[1].append(c)
                case 4: four[1].append(c)
            if c in lettersGuess:
                lettersGuess[c][0] += 1
            else:
                lettersGuess[c] = [1,False]
    for c in lettersGuess:
        if lettersGuess[c][1]:
            letters[c] = [lettersGuess[c][0]]

# for c in letters:
#     print("c = ", c)
#     print("letters[c] = ", letters[c])
#     print()



def processWords(w):  
    #confirm greens
    if zero[0] and w[0] not in zero[0]: return
    if one[0] and w[1] not in one[0]: return
    if two[0] and w[2] not in two[0]: return
    if three[0] and w[3] not in three[0]: return
    if four[0] and w[4] not in four[0]: return

    #confirm yellows and -s  
    if w[0] in zero[1] or w[1] in one[1] or w[2] in two[1] or w[3] in three[1] or w[4] in four[1]:
        return
    count = Counter(w)
    #make sure the count works
    for c in count:
        if c in letters:
            if letters[c][0]:
                if count[c] > letters[c][0]:
                    return

    print(w)


for _ in range(words):
    processWords(input())
    
            
#wrong answer and idk why