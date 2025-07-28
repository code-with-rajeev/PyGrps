from RTresult import RTResult
from BaseFunction import Temp,String,List,Number,BaseFunction,Bool
from Errors import RTError

def module(exec_ctx,pos,end):
    try:
        is_number = isinstance(exec_ctx.symbol_table.get("value"),Bool)
        return RTResult().success(Bool.false if not is_number else Bool.true)
    except Exception as a:
      print(a)
      return RTResult().failure(RTError(
        pos,end,
        "Expected Bool type object only :(",
        exec_ctx
      ))