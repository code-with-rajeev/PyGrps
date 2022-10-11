# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:29:34 2020

@author: ACER
"""


from RTresult import RTResult
from BaseFunction import Temp,String,List,Number,BaseFunction
from Errors import RTError

def module(ctx ,pos,end):
    try:
        is_number = isinstance(ctx.symbol_table.get("value"), Number)
        return RTResult().success(Number.true if is_number else Number.false)
    except Exception as a:
      return RTResult().failure(RTError(
        pos,end,
        "Expected int type object only :(",
        exec_ctx
      ))