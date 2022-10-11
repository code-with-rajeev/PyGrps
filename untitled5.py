# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 15:18:45 2020

@author: ACER
"""
import random
import string
from os import urandom as _urandom
def getrandbits( k):
        k = k.bit_length()
        """getrandbits(k) -> x.  Generates an int with k random bits."""
        if k <= 0:
            raise ValueError('number of bits must be greater than zero')
        if k != int(k):
            raise TypeError('number of bits should be an integer')
        numbytes = (k + 7) // 8                       # bits / 8 and rounded up
        x = int.from_bytes(_urandom(numbytes), 'big')
        return x >> (numbytes * 8 - k)
a = 10 
b = 20
result = b+1


while True:
    if result > a and result < b:
         break   
    result = getrandbits(b)
    print(result)
    
    