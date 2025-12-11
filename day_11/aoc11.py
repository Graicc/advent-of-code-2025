from functools import cache

lines = [line.split(":") for line in open("input").readlines()]
graph = dict([(l, r.split()) for (l, r) in lines])


## Part 1
@cache
def num_ways(curr: str) -> int:
    return 1 if curr == "out" else sum(map(num_ways, graph[curr]))


print(num_ways("you"))


## Part 2
@cache
def num_ways_2(curr: str, seen_dac: bool, seen_fft: bool) -> int:
    if curr == "out":
        return 1 if seen_dac and seen_fft else 0
    elif curr == "dac":
        seen_dac = True
    elif curr == "fft":
        seen_fft = True

    return sum([num_ways_2(x, seen_dac, seen_fft) for x in graph[curr]])


print(num_ways_2("svr", False, False))
