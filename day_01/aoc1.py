import math

lines = open("input").readlines()

### Part 1
pos = 50
count = 0

for line in lines:
    num = int(line[1:])
    if line[0] == "L":
        pos -= num
    else:
        pos += num

    pos = pos % 100

    if pos == 0:
        count += 1

print(count)

### Part 2
pos = 50
count = 0

for line in lines:
    orig = pos

    num = int(line[1:])
    cycles = math.floor(num / 100)
    count += cycles
    num = num % 100

    if line[0] == "L":
        while num > 0:
            pos -= 1
            num -= 1
            pos = pos % 100
            if pos == 0:
                count += 1
    else:
        while num > 0:
            pos += 1
            num -= 1
            pos = pos % 100
            if pos == 0:
                count += 1

    # if start == 0:
    #     count += 1

print(count)
