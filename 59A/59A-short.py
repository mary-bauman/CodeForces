w=input(); print(w.upper() if sum(1 for c in w if c.isupper())*2>len(w) else w.lower())
