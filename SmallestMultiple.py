'''
Created on Aug 6, 2015

@author: krishnasai
'''
import functools
def gcd(a, b): return a if b == 0 else gcd(b, a%b)
def lcm(a, b): return a / gcd(a, b) * b
for _ in range(int(input())):
    N = int(input())
    print(functools.reduce(lambda x,y: lcm(x, y), range(1, N+1)))
