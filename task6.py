from sys import argv
from itertools import count, cycle

# итератор
counter = count(int(argv[1]))
stop = 40
i = 0
for item in counter:
    print(item)
    if i == stop:
        break
    i += 1


# cycle
count_cycle = int(argv[1])
cycle_items = cycle([1, 2, 3, 4, 5])
i = 1
for item in cycle_items:
    print(item)
    if i == count_cycle:
        break
    i += 1
