import random
from cache import all_
from RTresult import RTResult
from BaseFunction import Temp,String,List,Number,BaseFunction
from Errors import Value_Error
from Context import Context
from GlobalSymbolTable import SymbolTable

def module(exec_ctx,pos,end):
    print(type(exec_ctx.symbol_table.get("value")))
    try:        
        value = exec_ctx.symbol_table.get("value")
        if value != None:
            if value.value in all_().keys():
                 value = all_()[value.value]
            else:
                 print(type(value.value))
                 return RTResult().failure(Value_Error(
                     pos,end,
                     f"__all__ have no value like {value.value} :("
                 ))
        else:
            value = "\n ______________________________\n| \n"
            for i in all_():
                value += f"| {i}  : {all_()[i]}\n"
            value += "|______________________________\n"
            print(value)
            value = all_()
        return RTResult().success(Number(value))
    except Exception as a:
      return RTResult().failure(Value_Error(
        pos,end,
        "Expected string type object only :("
      ))