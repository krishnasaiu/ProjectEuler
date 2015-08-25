'''
Created on Aug 6, 2015

@author: krishnasai
'''
for _ in range(int(input())):
    nk = list(map(int, input().split()))
    n = input()
    result = 0
    for i in range(nk[0]-nk[1]+1):
        mul = 1
        for j in range(nk[1]):
            mul *= int(n[i+j])
        if mul > result:
            result = mul
    print(result)    