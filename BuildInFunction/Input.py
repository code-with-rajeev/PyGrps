# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 08:46:24 2020

@author: ACER
"""


from RTresult import RTResult
from BaseFunction import Temp,String,List,Number,BaseFunction
from Errors import RTError
from Context import Context
from GlobalSymbolTable import SymbolTable

def module():
    text = input()
    return RTResult().success(String(text))
