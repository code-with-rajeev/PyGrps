# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 13:25:02 2020      #lAST MODIFIED 19 jan 723 LINES 24.7KB

@author: ACER
"""
from Context import Context
from GlobalSymbolTable import SymbolTable
from RTresult import RTResult
from Errors import *
global_symbol_table = SymbolTable()

class Value:
    def __init__(self):
        self.set_pos()
        self.set_context()

    def set_pos(self, pos_start=None, pos_end=None):
        self.pos_start = pos_start
        self.pos_end = pos_end
        return self

    def set_context(self, context=None):
        self.context = context
        return self

    def added_to(self, other):
        return None, self.illegal_operation(other)

    def subbed_by(self, other):
        return None, self.illegal_operation(other)

    def multed_by(self, other):
        return None, self.illegal_operation(other)

    def dived_by(self, other):
        return None, self.illegal_operation(other)

    def powed_by(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_eq(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_ne(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_lt(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_gt(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_lte(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_gte(self, other):
        return None, self.illegal_operation(other)

    def anded_by(self, other):
        return None, self.illegal_operation(other)

    def ored_by(self, other):
        return None, self.illegal_operation(other)

    def notted(self):
        return None, self.illegal_operation()

    def execute(self, args):
        return RTResult().failure(self.illegal_operation())

    def copy(self):
        raise Exception('No copy method defined')

    def is_true(self):
        return False
    def __all__(self):
        __all__ = self.__dict__
        for name,value in self.__class__.__dict__.items():
            __all__[name] = value
        return Number(__all__), None
    def illegal_operation(self, other=None):
        if not other: other = self
        return RTError(
            self.pos_start, other.pos_end,
            'Illegal operation',
            self.context
        )
class Module(Value):
    def __init__(self, value):

        super().__init__()
        self.value = value
        
    def copy(self,z = None):
        copy = Module(self.value)
        if z:
            copy = z
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def is_true(self):
        return self.value != 0
    
    def __repr__(self):
        return str(self.value)
class None_(Value):
    def __init__(self, value):

        super().__init__()
        self.value = value
        
    def copy(self):
        copy = None_(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy
    def type_(self):
        return Class(None).set_context(self.context), None
    def is_true(self):
        return self.value != 0
    def get_comparison_eq(self, other):
            return Bool(str(self.value == other.value)).set_context(self.context), None
    def __repr__(self):
        return str(self.value)
class Iterable(Value):
    def __init__(self, value):

        super().__init__()
        self.value = value
        
    def copy(self):
        copy = Iterable(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def is_true(self):
        return self.value != 0
    
    def __repr__(self):
        return f"Built-in {type(self.value).__name__} -Iterable object {self.value}"

class Bool(Value):
    def __init__(self, value):

        super().__init__()
        self.value = value
    def get_comparison_eq(self, other):
            return Bool(str(self.value == other.value)).set_context(self.context), None
    def copy(self):
        copy = Bool(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy
    def anded_by(self,other):
        if isinstance(other, Bool):
            print("treat",self.value,other.value,str(self.value and other.value))
            return Bool(str(self.value == "True" and other.value == "True")).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)
    def notted(self):
        print()
        if isinstance(self, Bool):
            return Bool(str(True if self.value == "False" else False)).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)
    def is_true(self):
        return True if self.value == "True" else False
    def type_(self):
        return Class(bool).set_context(self.context), None
    def __repr__(self):
        return str(self.value)
class Number(Value):
    def __init__(self, value):

        super().__init__()
        self.value = value

    def added_to(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def subbed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def multed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value).set_context(self.context), None
        if isinstance(other, String):
            return String(self.value * other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)
    def right_shift(self, other):
        if isinstance(other, Number):
            return Number(self.value >> other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)
    def left_shift(self, other):
        if isinstance(other, Number):
            return Number(self.value << other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def dived_by(self, other):
        if isinstance(other, Number):
            if other.value == 0:
                return None, RTError(
                    other.pos_start, other.pos_end,
                    'Division by zero',
                    self.context
                )

            return Number(self.value / other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)
    def rdived_by(self, other):
        if isinstance(other, Number):
            if other.value == 0:
                return None, RTError(
                    other.pos_start, other.pos_end,
                    'Division by zero',
                    self.context
                )

            return Number(self.value // other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)
    def powed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value ** other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_eq(self, other):
            return Bool(str(self.value == other.value)).set_context(self.context), None

    def get_comparison_ne(self, other):
            return Bool(str(self.value != other.value)).set_context(self.context), None
    def get_unpack(self, other):
            self.list = []
            if type(self.value) == int or type(self.value) == str:
                self.value = [self.value]
            self.value.append(other.value)
            return Number(self.value).set_context(self.context), None
    def makeequal(self,other):
        return Number([self.value,other.value]).set_context(self.context), None
    def get_comparison_lt(self, other):
        print(self.value,other.value)
        if isinstance(other, Number):
            
            return Bool(str(self.value < other.value)).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_gt(self, other):
        if isinstance(other, Number): 
            print("true",str(self.value > other.value))
            return Bool(str(self.value > other.value)).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_lte(self, other):
        if isinstance(other, Number):
            return Bool(str(self.value <= other.value)).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_gte(self, other):
        if isinstance(other, Number):
            return Bool(str(self.value >= other.value)).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def anded_by(self, other):
            return Number(int(self.value and other.value)).set_context(self.context), None
    def ored_by(self, other):
            return Number(int(self.value or other.value)).set_context(self.context), None

    def type_(self):
        return Class(int).set_context(self.context), None
    def copy(self, z = None):
        copy = Number(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def is_true(self):
        return self.value != 0
    
    def __repr__(self):
        return str(self.value)
    
class List(Value):
  def __init__(self, elements):
    super().__init__()
    self.elements = elements
    self.value = elements
  def type_(self):
      return Class(list).set_context(self.context), None
  def added_to(self, other):
    new_list = self.copy()
    try:
        new_list = new_list.elements+ other.elements
    except Exception as a:
        return None,  InvalidSyntaxError(
          self.pos_start, self.pos_end,
          f"Can't use operant type \"+\" to numeric or string \n Please use valid operant in Grapes" 
        )
    return List(new_list).set_context(self.context), None
  def slice(self,st,sp,sk):
      st = st.value if st else st
      sp = sp.value if sp else sp
      sk = sk.value if sk else sk
      new_list = self.elements[st:sp:sk]
      return List(new_list).set_context(self.context), None

  def append(self,other):
      new_list = self.value
      print(type(other))
      new_list.append(other.value)
      return List(new_list).set_context(self.context), None
  def pop(self):
      new_list = self.value
      removed  = new_list.pop()
      return removed.set_context(self.context), None
  def get_comparison_eq(self, other):
      return List.equal(self,other)
  def equal(first ,other):       

       if len(first.value) == len(other.value):
           for i in range(len(first.value)):
               if type(first.value[i]) == List:
                   return List.equal(first.value[i],other.value[i])
               elif first.value[i].value != other.value[i].value :
                   return Bool(str(False)).set_context(first.context), None
           return Bool(str(True)).set_context(first.context), None
       return Bool(str(False)).set_context(first.context), None

       
  def multed_by(self, other):
    if isinstance(other,Number):
      new_list = self.copy()
      new_list.elements.extend(other.elements)
      return new_list, None
    else:
      return None, Value.illegal_operation(self, other)
  def copy(self):
    copy = List(self.elements)
    copy.set_pos(self.pos_start, self.pos_end)
    copy.set_context(self.context)
    return copy
  def __str__(self):
     try:
        return ", ".join([str(x) for x in self.elements])
     except Exception as a:
         return str(self.elements)

  def __repr__(self):
    return f'[{", ".join([repr(x) for x in self.elements])}]'
class Temp(Value):
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.tempdata = []
    def makeequal(self,other):
        lhs = self.value.__dict__['value']
        if type(other.value) == int or type(other.value) == str:
            return None,Value_Error(other.__dict__['pos_start'], other.__dict__['pos_end'],"not enough value to pack")
        else:
            rhs = other.value.__dict__['value']
        if len(lhs) != 1 and len(lhs) > len(rhs):
            return None,InvalidSyntaxError(lhs[0].pos_start, lhs[0].pos_end,"not enough value to pack")
        else:
            for i in range(len(lhs)):
                if type(lhs[i]).__name__ != "VarAccessNode":
                    name = type(lhs[i]).__name__
                    return None, Value_Error(lhs[i].pos_start, lhs[i].pos_end,f"Can't assign non literal type {type(lhs[i]).__name__[:len(name)-4:]}")
                value = self.context.symbol_table.set(lhs[i].__dict__['var_name_tok'].__dict__['value'],rhs[i])
            return Temp(value).set_context(self.context), None

    def arrange(self,data,mode,interpreter):
        context = Context('<program>')
        context.symbol_table = global_symbol_table
        list = ()
        for i in range(len(data.node)):
            if type(data.node[i]).__name__ == "Temp":
                new = self.arrange(data.node[i])
                for j in range(len(new)):
                    list+=(new[j],)
            else:
                if mode:
                    result = Identifier(data.node[i])
                else:
                    result = interpreter.visit(data.node[i], context)
                list+=(result.value,)
        return Temp(list)
    def copy(self):
        copy = Temp(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy
    def __repr__(self):
        return f'{self.value}'
class Identifier(Value):
    def __init__(self, value):
        super().__init__()
        self.value = value
    def makeequal(self,other):
        res = RTResult()
        value = self.context.symbol_table.set(self.value,other)
        return Identifier(self.value).set_context(self.context), None
    def arrange(self,data):
        pass
    def copy(self):
        copy = Temp(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy
    def __repr__(self):
        return f'{self.value}'
class ContainerType(Value):
    def __init__(self, value):
        super().__init__()
        self.value = value
    def arrange(self):
        pass
    def copy(self):
        copy = ContainerType(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy
    def __repr__(self):
        return f'{self.value}'
class Attribute(Value):
    def __init__(self, value,parent = None,chain = None,exter = None):
        super().__init__()
        self.exter = exter
        self.parent= parent
        self.chain = chain
        self.value = value
        self.repr = str(self.value)

    def visit_CallNode(self,other):
        pass
    def visit_VarAccessNode(self,data):
        pass
    def set_grps_mod(val,name):
        mod = Module(name).set_context(val.context)
        val = val.value
        for value in val:
            mod.context.symbol_table.set(name,value)
        return mod
        
        
    def getattr1_(self,parent,chain,i,node,context,exter= None):
        print(88)
        res = RTResult()
        error = None
        z = None
        chain_args = None
        class_ = Class(None)
        parent_args = None
        type_ = None
        if exter:### for var only
            x = getattr(exter,chain.var_name_tok.value)
            x = Number(x)
            c = RTResult().success(x.set_context(context).set_pos(node.pos_start, node.pos_end)),None
            return c
        if type(parent).__name__ == "ClassType":
            self.parent_name = parent.tok.value
        elif type(parent).__name__ == "CallNode":
            self.parent_name = parent.node_to_call.var_name_tok.value
        elif type(parent).__name__ == "StringNode":   #when parent is string directly
            self.parent_name = parent.tok    
        else:
            print("UNDER DEVELOPMENT!")
        parent_value = i.visit(parent,context).value
        chain_name = chain.node_to_call.var_name_tok.value if type(chain).__name__ == "CallNode" else chain.var_name_tok.value
        try:
            z = getattr(self,f'{type(parent_value).__name__}_attr')(parent_value,chain_name)
        except Exception as a:
            if type(parent_value).__name__ == "Function":
                return None, RTResult().failure(Attribute_Error(parent.pos_start,chain.pos_end,a))# if GRPS FUNC
            
        try:
            z = z.copy(parent_value)
        except Exception as a:
            pass
        py_val = []
        if not z:
            try:
                z = parent_value.value
            except Exception as a:
                print("Sorry ! yet under development")
               # return None, RTResult().failure(Attribute_Error(parent.pos_start,chain.pos_end,a))
        if type(chain).__name__ == "CallNode":
            chain_args = chain.arg_nodes
            for j in range(len(chain_args)):
                if type(z).__name__ in ["builtin_function_or_method","function"]:
                    
                    x = i.visit(chain_args[j],context)
                    
                    value = x.value
                    error = x.error#if argument is define
                    if error:
                        return None,RTResult().failure(error)
                    value = value.value  
                    py_val.append(value)
                elif type(z).__name__ in ["type"]:
                    
                    x = i.visit(chain_args[j],context).value.value
                    py_val.append(x)
                else:
                    x = i.visit(chain_args[j],context).value
                #   x = i.visit(chain_args[j],context).value when args
                    py_val.append(x)
            if type(z).__name__ in ["builtin_function_or_method","function"]:
                try:
                    value = z(*py_val) # two case -arg is  grps or -arg is pyhton
                except Exception as a:
                    
                    value = z()(*py_val)
            elif type(z).__name__ == "method":
                try:
                    value = z(*py_val)#when bound method is of GRPS
                    value,error = value
                except Exception as a:
                    value = z(*py_val)#when bound method is of py
                if error :
                    return None,RTResult().failure(error)
            elif type(z).__name__ == "type":
                value = z(*py_val)    #when parent is a python class and args is GrPS
            else:
                try:
                    value = z.execute(*py_val).value if py_val else z.execute([]).value.value
                    error = z.execute(*py_val).error if py_val else z.execute([]).error
                except Exception as a:
                    try:
                        value = value.execute(*py_val) if py_val else value.execute([])
                        value = value.value.value
                    except Exception as a:
                        value = z
        else:
            value = z
        
        value = Class.set_class(value)
        return RTResult().success(
            value.set_context(context).set_pos(node.pos_start, node.pos_end)
        ),error
    
    def Class__attr(self,p,c):
        setattr(p,"name",f"{p.name}.{c}")
        try:
            setattr(p,"repr",f"bound method {p.name} of {self.parent_name}")
        except Exception as a:
            setattr(p,"repr",f"formatted method {p.name} of {c}")
        return getattr(p,c)
    def Class_attr(self,p,c): 
        x = getattr(p.value,c)
        return x
    def Module_attr(self,p,c):
        x = getattr(p.value,c)
        return x
    def Number_attr(self,p,c):
        try:
            return getattr(p.value,c)
        except Exception as a:
            return getattr(p,c)
    def String_attr(self,p,c):
        try:
            return getattr(p.value,c)
        except Exception as a:
            return getattr(p,c)
    def Function_attr(self,p,c):
        try:
            return getattr(p.value,c)
        except Exception as a:
            return getattr(p,c)
        
    def List_attr(self,p,c):
        try:
            return getattr(p.element,c)
        except Exception as a:
            return getattr(p,c)
    def type_(self):
        return Attribute(self.value).set_context(self.context), None
    def setattr_(self,parent,chain,i,node,context,exter):
        p_res = i.visit(parent,context).value if not exter  else exter
        c_res = chain.var_name_tok.value
        if exter:
            return exter
        return Attribute([p_res,c_res,context,exter])
    def copy(self):
        copy = Temp(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy
    def __repr__(self):
        return f"{self.value}"
    def makeequal(self,other):
        p = self.value.value[0]
        c = self.value.value[1]
        con = self.value.value[2]
        
        if not self.exter:
             # bcz only Number or str has attribute value
            setattr(p,c,other) if type(other).__name__ in ["Function"] else setattr(p,c,other.value)
        else:
            setattr(self.exter,self.chain.var_name_tok.value,other.value)
            self.context.symbol_table.set(f"{self.parent}",self.exter)
       # self.context.symbol_table.set(f"{self.exter.name}",self.value.value)
        return Number.null, None
        
class String(Value):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def added_to(self, other):
        if isinstance(other, String):
            return String(self.value + other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def multed_by(self, other):
        if isinstance(other, Number):
            return String(self.value * other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)
    def get_comparison_eq(self, other):
            return Bool(str(self.value == other.value)).set_context(self.context), None

    def get_comparison_ne(self, other):
            return Bool(str(self.value != other.value)).set_context(self.context), None
    def get_comparison_lt(self, other):
        if isinstance(other, String):
            return Bool(str(self.value < other.value)).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_gt(self, other):
        if isinstance(other, String): 
            return Bool(str(self.value > other.value)).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_lte(self, other):
        if isinstance(other, String):
            return Bool(str(self.value <= other.value)).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_gte(self, other):
        if isinstance(other, String):
            return Bool(str(self.value >= other.value)).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_unpack(self, other):
            self.list = []
            if type(self.value) == int or type(self.value) == str:
                self.value = [self.value]
            self.value.append(other.value)
            return Number(self.value).set_context(self.context), None
    def is_true(self):
        return len(self.value) > 0
    def type_(self):
        return Class(str).set_context(self.context), None
    def find_as(self):
        if isinstance(other, String):
            return String(self.value + other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)
    def copy(self):
        copy = String(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def __repr__(self):
        return f'{self.value}'

class Class(Value):
    def __init__(self, value):

        super().__init__()
        
        self.value = value
        
    def copy(self):
        copy = Class(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy
    def type_(self):
        return Class(type(self.value)).set_context(self.context), None
    def is_true(self):
        return self.value != 0
    def set_class(value):
        try:
            if type(value.value) in [int,str,list,bytes,str]:
                value = value.value# only if return value is GRPS OBJ
        except Exception as a:
            print(a)
        if type(value) == int:
            return Number(value)
        elif type(value) == str:
            return String(value)
        elif type(value) == list:
            return List(value)
        elif type(value) == bytes:
            return Number(value)
        else:
            return Class(value)
            #return Class(value) #Treat both py and grps obj same so it raises an error

 
    def get_comparison_eq(self, other):
        #if isinstance(other, Class):  bcz function has no attr value
            """
            try:
                return Number(int(self.value.value == other.value)).set_context(self.context), None
            except Exception as a:
                return Number(int(self.value == other.value.value)).set_context(self.context), None
        else:
            try:
                return Number(int("None" ==other.value)).set_context(self.context), None
            except Exception  as a:
                pass
            """
            return Bool(str(self.value == other.value)).set_context(self.context), None
        #return None, Value.illegal_operation(self, other)
    def __repr__(self):
        return f"GRPS OBJ {str(self.value)}"
class BaseModule(Value):
  def __init__(self, name):
    super().__init__()
    self.name = name or "<anonymous>"

  def generate_new_context(self):
    if not self.context:
        self.context = Context('<program>')
        self.context.symbol_table = global_symbol_table
    new_context = Context(self.name, self.context, self.pos_start)
    new_context.symbol_table = SymbolTable(new_context.parent.symbol_table)
    return new_context

class BaseFunction(Value):
  def __init__(self, name):
    super().__init__()
    self.name = name or "<anonymous>"

  def generate_new_context(self):
    if not self.context:
        self.context = Context('<program>')
        self.context.symbol_table = global_symbol_table
    new_context = Context(self.name, self.context, self.pos_start)
    new_context.symbol_table = SymbolTable(new_context.parent.symbol_table)
    return new_context
 
  def check_args(self, arg_names, args):
    res = RTResult()
    if len(args) > len(arg_names):
      return res.failure(RTError(
        self.pos_start, self.pos_end,
        f"{len(args) - len(arg_names)} too many args passed into {self}",
        self.context
      ))
    
    if len(args) < len(arg_names):
      return res.failure(RTError(
        self.pos_start, self.pos_end,
        f"{len(arg_names) - len(args)} too few args passed into {self}",
        self.context
      ))

    return res.success(None)

  def populate_args(self, arg_names, args, exec_ctx):
    for i in range(len(args)):
      arg_name = arg_names[i]
      arg_value = args[i]
      arg_value.set_context(exec_ctx)
      exec_ctx.symbol_table.set(arg_name, arg_value)

  def check_and_handle_args(self, arg_names, args, exec_ctx):
    res = RTResult()
    res.register(self.check_args(arg_names, args))
    if res.should_return(): return res
    self.populate_args(arg_names, args, exec_ctx)
    return res.success(None)

Number.null = Number(0)
Number.false = Number(0)
Number.true = Number(1)
Bool.true = Bool("True")
Bool.false = Bool("False")
None_.null = None_("None")

"""
        lhs = self.value.__dict__['value']
        if type(other.value) == int or type(other.value) == str:
            return None,Value_Error(other.__dict__['pos_start'], other.__dict__['pos_end'],"not enough value to pack")
        else:
            rhs = other.value.__dict__['value']
        if len(lhs) != 1 and len(lhs) > len(rhs):
            return None,InvalidSyntaxError(lhs[0].pos_start, lhs[0].pos_end,"not enough value to pack")
        else:
            for i in range(len(lhs)):
                if type(lhs[i]).__name__ != "VarAccessNode":
                    name = type(lhs[i]).__name__
                    return None, Value_Error(lhs[i].pos_start, lhs[i].pos_end,f"Can't assign non literal type {type(lhs[i]).__name__[:len(name)-4:]}")
                value = self.context.symbol_table.set(lhs[i].__dict__['var_name_tok'].__dict__['value'],rhs[i])
            return Temp(value).set_context(self.context), None

"""