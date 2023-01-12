import operator
import itertools

miesiace = [10, 8, 5, 7, 12, 10, 5, 8, 15, 3, 4, 2]

print(list(itertools.accumulate(miesiace, operator.add)))

a = range(3)
b = range(5)
c = [a, b]
print(list(itertools.chain(a, b)))
print(list(itertools.chain.from_iterable(c)))

print(list(itertools.compress(range(1000), [0, 1, 1, 1, 0, 1])))

primes = [0, 0, 1, 1, 0, 1, 0, 1]
numbers = ['zero', 'jeden', 'dwa', 'trzy', 'cztery', 'pięć']

print(list(itertools.compress(numbers, primes)))
