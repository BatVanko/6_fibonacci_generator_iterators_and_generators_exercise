def fibonacci():
    first =  0
    second = 1
    yield first
    yield second
    while True:
        result = first + second
        yield result
        first = second
        second = result
generator = fibonacci()
for i in range(5):
    print(next(generator))



