# Gererator expression, iterables e iterators em Python

# iterable = deter valor em sequencia
# iterator = entregar um valor por vez

from email import generator


iterable = ['Python','Progrmação','__inter__']
iterator = iter(iterable) #tem __item__ e __next__
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
for inte in iterator:
    print(inte)

generator = [
    n for n in range(10)
]
print(generator)

generator = (n for n in range (10))
for n in generator:
    print(n)