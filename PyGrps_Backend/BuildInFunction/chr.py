from RTresult import RTResult
from BaseFunction import Temp,String,List,Number,BaseFunction,Bool
from Errors import RTError

def module(exec_ctx,pos,end):
    try:
        value = exec_ctx.symbol_table.get("value")
        is_number = isinstance(value, Number)
        return RTResult().success(Number(chr(value.value)))
    except Exception as a:
      return RTResult().failure(RTError(
        pos,end,
        f"{a} \n don't be sad:(",
        exec_ctx
      ))