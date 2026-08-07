import math

def answer(n, m, a):
    if a==1: return n*m
    if a>=n and a>=m: return 1
    if a>=n: #a<m
        return math.ceil(m/a)
    if a>=m: #a<n
        return math.ceil(n/a)
    # a<n and a<m
    return math.ceil(n/a)*math.ceil(m/a)




n, m, a = map(int, input().split())
print(answer(n, m, a))