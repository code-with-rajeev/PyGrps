from RTresult import RTResult
from BaseFunction import Temp,String,List,Number,BaseFunction
from Errors import RTError
from Context import Context
from GlobalSymbolTable import SymbolTable

def module(exec_ctx,pos,end):
    try:
        value = exec_ctx.symbol_table.get("value")
        return RTResult().success(Number(abs(value.value)))
    except Exception as a:
      return RTResult().failure(RTError(
        pos,end,
        "Expected int type object only :(",
        exec_ctx
      ))
    