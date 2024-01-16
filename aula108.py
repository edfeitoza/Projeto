# count é um iterador sem fim
from itertools import count

c1 = count()
r1 = range(10)

# print(next(c1))
# print(next(c1))

print(20*'-')

print('Count')

for i in c1:
    if i > 10:
        break
    
    print(i)
    
print(20*'-')

print('Range')

for j in r1:
    j += 1
    print(j)

print(20*'-')