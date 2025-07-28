from RTresult import RTResult
from BaseFunction import Temp,String,List,Number,BaseFunction,Bool,None_
from Errors import RTError

def module(exec_ctx,pos,end):
    try:
        if isinstance(exec_ctx.symbol_table.get("value"), None_) or exec_ctx.symbol_table.get("value").value == "False":
            return RTResult().success(Bool.false)
        else:
            return RTResult().success(Bool.true)
    except Exception as a:
      print(a)
      return RTResult().failure(RTError(
        pos,end,
        "Expected iterable type object only :(",
        exec_ctx
      ))