'''
Created on Aug 6, 2015

@author: krishnasai
'''
for _ in range(int(input())):
    N = int(input())
    temp = N*(N+1)/2
    print(temp**2 - temp*(2*N+1)/3)