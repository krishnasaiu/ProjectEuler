'''
Created on Aug 6, 2015

@author: krishnasai
'''
def eratosthenes(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))
primes = list(eratosthenes(10000))
for _ in range(int(input())):
    print(primes[int(input())-1])
