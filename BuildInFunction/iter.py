# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 12:44:35 2020

@author: ACER
"""

from RTresult import RTResult
from BaseFunction import Temp,String,List,Number,BaseFunction,Bool,Iterable
from Errors import RTError

def module(exec_ctx,pos,end):
    try:
        value = exec_ctx.symbol_table.get("value")
        print(value)
        is_number = isinstance(value, Number)
        if not is_number:
            return RTResult().success(Iterable(value.value))
        else:
            return RTResult().failure(RTError(
                pos,end,
                f"{type(value).__name__} is not iterabale \n don't be sad:(",
                exec_ctx
            ))
    except Exception as a:
      return RTResult().failure(RTError(
        pos,end,
        f"{a} \n don't be sad:(",
        exec_ctx
      ))
        