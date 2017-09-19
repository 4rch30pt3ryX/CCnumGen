# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 15:55:15 2017

@author: gemmml9
"""

def luhn(n):
    r = [int(ch) for ch in str(n)][::-1]
    return (sum(r[0::2]) + sum(sum(divmod(d*2,10)) 
        for d in r[1::2])) % 10 == 0
for n in (4556384752412104, 4486686131483035, 4716579041905282):
    print(n, luhn(n))
    
    


    
# CCnumGen
