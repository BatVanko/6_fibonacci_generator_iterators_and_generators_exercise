# 6_fibonacci_generator_iterators_and_generators_exercise

Create a generator function called fibonacci() that generates the Fibonacci numbers infinitely. The first two numbers in the sequence are always 0 and 1. Each following Fibonacci number is created by the sum of the current number with the previous one.


Test Code
generator = fibonacci()
for i in range(5):
    print(next(generator))


Output

0
1
1
2
3
