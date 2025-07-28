from RTresult import RTResult
from BaseFunction import Temp,String,List,Number,BaseFunction
from Errors import RTError

def module(exec_ctx,pos,end):
    try:
        is_number = isinstance(exec_ctx.symbol_table.get("value"), BaseFunction)
        return RTResult().success(Number.true if is_number else Number.false)
    except Exception as a:
      return RTResult().failure(RTError(
        pos,end,
        "Expected fun type object only :(",
        exec_ctx
      ))
