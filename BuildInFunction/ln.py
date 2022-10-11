# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 16:32:49 2020

@author: ACER
"""
from RTresult import RTResult
from BaseFunction import Temp,String,List,Number,BaseFunction
from Errors import RTError

def module(exec_ctx,pos,end):
    list_ = exec_ctx.symbol_table.get("list")
    
    if isinstance(list_, Temp):
      list_ = list_.__dict__['value'].__dict__
      return RTResult().success(Number(len(list_['value'])))
    elif isinstance(list_ , List):
      return RTResult().success(Number(len(list_.elements)))
    elif isinstance(list_ , String):
      return RTResult().success(Number(len(list_.value)))
    return RTResult().failure(RTError(
        pos,end,
        "Argument must be str, list or tuple",
        exec_ctx
    ))
