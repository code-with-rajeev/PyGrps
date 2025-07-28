from RTresult import RTResult
from BaseFunction import Temp,String,List,Number,BaseFunction,Bool
from Errors import RTError

def module(exec_ctx,pos,end):
    try:
        value = exec_ctx.symbol_table.get("value")
        is_number = isinstance(value, String)
        return RTResult().success(Number(ord(value.value)))
    except Exception as a:
      print(a)
      error = ""
      if isinstance(exec_ctx.symbol_table.get("value"), String):
          error = f"of length {len(value.value)} "
      return RTResult().failure(RTError(
        pos,end,
        f"Expected string of len 1, but a {type(value).__name__} {error} found  \n don't be sad:(",
        exec_ctx
      ))