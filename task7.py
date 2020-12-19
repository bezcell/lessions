def fact(n):
    facts = [item for item in range(1, n + 1)]
    start = 1
    for f in facts:
        start *= f
        yield start


for el in fact(10):
    print(el)
