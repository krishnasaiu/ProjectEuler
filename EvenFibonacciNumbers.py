'''
Created on Aug 5, 2015

@author: krishnasai
'''
for _ in range(int(input())):
    fib = []
    fib.append(1)
    fib.append(1)
    N = int(input())
    [fib.append(fib[i-1] + fib[i-2]) for i in range(2, N)] 
    print(sum([n for n in fib if n%2 == 0 and n<N]))
