# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 02:42:14 2020

@author: ACER
"""



from RTresult import RTResult
from BaseFunction import Temp,String,List,Number,BaseFunction,Bool,Class
from Errors import RTError

def module(exec_ctx,pos,end):
    print(23,exec_ctx.symbol_table.get("value").type_())
    try:
        return RTResult().success(exec_ctx.symbol_table.get("value").type_()[0])
    except Exception as a:
      return RTResult().failure(RTError(
        pos,end,
        f"{a} \n don't be sad:(",
        exec_ctx
      ))