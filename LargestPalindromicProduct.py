'''
Created on Aug 6, 2015

@author: krishnasai
'''
def isPalindrome(N):
    return str(N) == str(N)[::-1]
palins = []
for i in range(100, 999):
    for j in range(i, 999):
        m = i * j
        if(isPalindrome(m)):
            palins.append(m)
for _ in range(int(input())):
    N = int(input())
    print(max([i for i in palins if i < N]))