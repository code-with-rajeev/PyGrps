# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 19:17:14 2020

@author: ACER
"""


x = "i am fine bro. Nice to meet you can we meet again"
def encoder(x):
    text = ""
    for a in x :
        num = ord(a)
        if num %2 == 0:
            text += chr(5100+(num))
        else:
            text += chr(5100+(num))
    return text
print(encoder(x))
