import math

def answer(n, m, a):
    if a>=n and a>=m: return 1
    if a>=n: #a<m
        return math.ceil(a/m)
    if a>=m: #a<n
        return math.ceil(a/n)
    # a<n and a<m
    return math.ceil(n/a)*math.ceil(m/a)




n, m, a = map(int, input().split())
print(answer(n, m, a))