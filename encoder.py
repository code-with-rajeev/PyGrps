# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 20:08:12 2020

@author: ACER
"""
def encoder(text):
    incode = ""
    for a in text :
        incode += chr(ord(a)+7000)#
    print(incode)
    return incode
def decoder(text):
    decode = ""
    for a in text :
        if ord(a) <= 7000:
            return("VALUE ERROR: already decoded")
        decode += chr(ord(a)-7000)
    print(decode)
    return decode
encode = encoder
decode = decoder
