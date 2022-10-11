# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 13:42:33 2020

@author: ACER
"""
from RTresult import RTResult
from BaseFunction import Temp,String,List,Number,BaseFunction,Bool,Class
from Errors import RTError

def module(exec_ctx,pos,end):
    try:
        value1 = exec_ctx.symbol_table.get("start")
        is_number1 = isinstance(value1, Number)
        try:
            value2 = exec_ctx.symbol_table.get("stop")
        except Exception as a:
            print(a)
        is_number1 = isinstance(value2, Number)
        print(value1,value2)

        return RTResult().success(Class(range(value1.value,value2.value)))
    
    except Exception as a:
      return RTResult().failure(RTError(
        pos,end,
        f"{a} \n don't be sad:(",
        exec_ctx
      ))