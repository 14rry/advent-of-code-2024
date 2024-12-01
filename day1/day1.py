import operator
from collections import Counter

with open('input.txt') as f:
    s = f.read().split()

    a = sorted([int(val) for val in s[::2]])
    b = sorted([int(val) for val in s[1::2]])

    d = list(map(operator.sub,a,b))
    d = [abs(val) for val in d]
    print(sum(d)) # part 1

    bc = Counter(b)
    counts = sum([bc[val]*val for val in a])
    print(counts) # part 2


    



