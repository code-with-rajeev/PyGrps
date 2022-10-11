# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 19:56:59 2020

@author: ACER
"""

from RTresult import RTResult
from BaseFunction import Temp,String,List,Number,BaseFunction,Bool
from Errors import RTError

def module(exec_ctx,pos,end):
    print(exec_ctx.symbol_table.get("value").value)
    try:
        value = exec_ctx.symbol_table.get("value")
        is_number = isinstance(value,String)
        return RTResult().success(String(open(value.value))) if is_number else None
    except Exception as a:
      return RTResult().failure(RTError(
        pos,end,
        f"{a} \n don't be sad:(",
        exec_ctx
      ))