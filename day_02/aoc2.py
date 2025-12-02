import math

items = [tuple(map(int, x.split("-"))) for x in open("input").read().split(",")]

## Part 1
count = 0

for (a,b) in items:
    for i in range(b-a + 1):
        x1 = a + i
        x = str(x1)
        l = len(x)
        if l % 2 == 0:
            half = int(l / 2)
            f = x[half:]
            l = x[:half]
            if f == l:
                count += x1

print(count)

## Part 2
count = 0

def is_valid(x):
    s = str(x)
    l = len(s)
    for splits in range(1, l):
        if math.floor(l / splits) != l / splits:
            continue

        r = int(l / splits)
        
        f = s[:splits]
        found = True
        for a in range(r):
            subset = s[a*splits:a*splits + splits]
            if subset != f:
                found = False
                break
        if found:
            return x

    return 0
    

for (a,b) in items:
    for i in range(b-a + 1):
        x1 = a + i
        count += is_valid(x1)

print(count)