#24.5 kb base func 723 lines  24.2 kb 723 }} 682 23.1    691   23.4 {}
#1612  63.2  1590 66  {}
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 17:08:59 2020

@author: ACER
"""

from tokens import *
from BaseFunction import *
from Errors import *
from Lexer import Lexer
from RTresult import RTResult
from _In_Built_Function import BuildInFunction_grps as In_Built
import time


__all__ = ['NumberNode','StringNode','VarAccessNode','VarAssignNode','UnaryOpNode','UnPack',
           'Templist','IfNode','all_','FuncDefNode','CallNode','ReturnNode','ListNode','ParseResult']
to_print = []

class BaseNode:
    def __init__(self, tok):
        self.tok,self.pos_start,self.pos_end = tok,tok.pos_start,tok.pos_end  
class NumberNode:
    def __init__(self, tok):
        BaseNode.__init__(self,tok)
    def __repr__(self): return f'{self.tok}'
class ImportNode:
    def __init__(self, mod, get):
        self.mod,self.get,self.pos_start,self.pos_end = mod,get,mod.pos_start,mod.pos_end
    def __repr__(self): return f'{self.mod}'
class BoolType:
    def __init__(self, tok):
        BaseNode.__init__(self,tok)
    def __repr__(self): return f'{self.tok}'
class ClassType:
    def __init__(self, tok):
        BaseNode.__init__(self,tok)
    def __repr__(self): return f'{self.tok}'
class NoneType:
    def __init__(self, tok):
        BaseNode.__init__(self,tok)
    def __repr__(self): return f'{self.tok}'
class Pass_Node:
    def __init__(self, tok):
        BaseNode.__init__(self,tok)
    def __repr__(self): return f'{self.tok}'
class StringNode:
    def __init__(self, tok):
        BaseNode.__init__(self,tok)
    def __repr__(self): return f'{self.tok}'
class VarAccessNode:
    def __init__(self, var_name_tok):
        self.var_name_tok,self.pos_start,self.pos_end = var_name_tok,var_name_tok.pos_start,var_name_tok.pos_end
class VarAssignNode:
    def __init__(self, var_name_tok, value_node):
        self.var_name_tok,self.pos_start,self.pos_end = var_name_tok,var_name_tok.pos_start, var_name_tok.pos_end
        self.value_node = value_node
class BinOpNode:
    def __init__(self, left_node, op_tok, right_node):
        self.left_node,self.op_tok,self.right_node = left_node,op_tok,right_node
        self.pos_start,self.pos_end=left_node.pos_start,right_node.pos_end
    def __repr__(self): return f'({self.left_node}, {self.op_tok}, {self.right_node})'
class UnaryOpNode:
    def __init__(self, op_tok, node):
        self.op_tok,self.node,self.pos_start,self.pos_end = op_tok,node,op_tok.pos_start,node.pos_end
    def __repr__(self): return f'({self.op_tok}, {self.node})'
class SliceNode:
    def __init__(self,parent,start,stop,skip):
        self.parent,self.pos_start,self.pos_end,self.start,self.stop,self.skip = parent,parent.pos_start,parent.pos_end,start,stop,skip
class AttributeNode:
    def __init__(self, chain, parent, type_ = None):
        self.chain,self.parent = chain,parent
        self.type_ = type_
        self.pos_start,self.pos_end = self.parent.pos_start,chain.pos_end
    def __repr__(self): return f'({self.parent}, {self.chain})'
class UnPack:
    def __init__(self, op_tok, node):
        self.op_tok,self.node,self.pos_start,self.pos_end = op_tok,node,op_tok.pos_start,node.pos_end
class Templist:
    def __init__(self,node= ()):
        self.node,self.pos_start,self.pos_end = node,None,None
    def add(self,node): 
        self.pos_start,self.pos_end = node.pos_start, node.pos_end
        self.node += node,
        return self
    def fresh(self): self.node = ()
    def copy(self): return Templist(self.node)
class IfNode:
  def __init__(self, cases, else_case):
    self.cases = cases
    self.else_case = else_case
    self.pos_start = self.cases[0][0].pos_start
    self.pos_end = (self.else_case or self.cases[len(self.cases) - 1])[0].pos_end
class WhileNode:
  def __init__(self, condition_node, body_node, should_return_null):
    self.condition_node = condition_node
    self.body_node = body_node
    self.should_return_null = should_return_null

    self.pos_start = self.condition_node.pos_start
    self.pos_end = self.body_node.pos_end
class FuncDefNode:
  def __init__(self, var_name_tok, arg_name_toks, body_node, should_auto_return):
    self.var_name_tok,self.arg_name_toks,self.body_node = var_name_tok,arg_name_toks,body_node
    self.should_auto_return = should_auto_return
    if self.var_name_tok:
      self.pos_start = self.var_name_tok.pos_start
    elif len(self.arg_name_toks) > 0:
      self.pos_start = self.arg_name_toks[0].pos_start
    else:
      self.pos_start = self.body_node.pos_start
    self.pos_end = self.body_node.pos_end
class ClassNode:
  def __init__(self, var_name_tok, arg_name_toks, body_node):
    self.var_name_tok,self.arg_name_toks,self.body_node = var_name_tok,arg_name_toks,body_node
class Container:
    def __init__(self,type_, node,start,end):
        self.type = None if not type_ else type_
        self.node = None if not node else node
        self.pos_start,self.pos_end = start,end
class CallNode:
    def __init__(self, node_to_call, arg_nodes):
        self.node_to_call = node_to_call
        self.arg_nodes = arg_nodes
        self.pos_start = self.node_to_call.pos_start
        self.pos_end = self.arg_nodes[len(self.arg_nodes) - 1].pos_end if len(self.arg_nodes) > 0 else self.node_to_call.pos_end
class ReturnNode:
  def __init__(self, node_to_return, pos_start, pos_end):
    self.node_to_return = node_to_return
    self.pos_start,self.pos_end = pos_start,pos_end
class ListNode:
  def __init__(self, element_nodes, pos_start, pos_end):
    self.element_nodes = element_nodes
    self.pos_start,self.pos_end = pos_start,pos_end
class ForNode:
  def __init__(self, var, parent, body):
    self.var = var
    self.parent,self.body = parent,body
class ParseResult:
    def __init__(self):
        self.error,self.node = None,None
        self.last_registered_advance_count = 0
        self.advance_count = 0
    def try_register(self, res):
        if res.error:
            self.to_reverse_count = res.advance_count
            return None
        return self.register(res)
    def register_advancement(self):
        self.last_registered_advance_count = 1
        self.advance_count += 1
    def register(self, res):
        if isinstance(res, ParseResult):
            if res.error:    self.error = res.error
            return res.node
        return res
    def success(self, node):
        self.node = node
        return self
    def failure(self, error):
        if not self.error or self.last_registered_advance_count == 0:
            self.error = error
        return self

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.prev,self.not_temp_node,self.list_node,self.Return_node = None,False,False,False
        self.tok_idx = -1
        self.advance()
        self.templist = Templist()
    def reverse(self, amount=1):
        self.tok_idx -= amount
        self.advance()
        return self.current_tok
    def advance(self, ):
        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]
        return self.current_tok
    def refresh(self):
        self.not_temp_node,self.list_node,self.Return_node = False,False,False
    def update(self,res):
        self.advance()
        res.register_advancement()
    def parse(self):
        res = ParseResult()
        if not self.current_tok.type == TT_EOF:
            res = self.statements()
            if not res.error and self.current_tok.type != TT_EOF:
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    "Expected '+', '-', '*', '/', '^', '==', '!=', '<', '>', <=', '>=', 'AND' or 'OR'"
                ))
        return res
    def statements(self):
        res = ParseResult()
        statements = []
        pos_start = self.current_tok.pos_start.copy()
        while self.current_tok.type == TT_NEWLINE:
            self.update(res)
        statement = res.register(self.statement())     
        if res.error: return res
        statements.append(statement)
        more_statements = True
        while True:
            newline_count = 0
            while self.current_tok.type == TT_NEWLINE :
                    self.update(res)
                    newline_count+=1
            if newline_count == 0:
                more_statements = False
            if not more_statements: break
            statement = res.try_register(self.statement()) # actually it is res.try register
            if res.error: return res
            if not statement:
                more_statements = False
                continue
            statements.append(statement)
        return res.success(ListNode(
            statements,
            pos_start,
            self.current_tok.pos_end.copy()
        ))
    def fun_stat(self):
        res = ParseResult()
        statements = []
        pos_start = self.current_tok.pos_start.copy()
        while self.current_tok.type != TT_DS:
            while self.current_tok.type == TT_NEWLINE:
                self.update(res)
            statement = res.register(self.statement())
            if res.error: return res
            statements.append(statement)
            self.update(res)
            more_statements = True
        if self.current_tok.type == TT_DS:
            pos_start=self.current_tok.pos_start.copy()
            self.update(res)
            if self.current_tok.type == TT_EOF  or self.current_tok.type == TT_NEWLINE:
                expr = None
            else:
                expr = res.register(self.expr())
                if res.error: return res
            statements.append(ReturnNode(expr, pos_start, self.current_tok.pos_start.copy()))
        return res.success(ListNode(
            statements,
            pos_start,
            self.current_tok.pos_end.copy()
        ))
    def statement(self):
        res = ParseResult()
        pos_start = self.current_tok.pos_start.copy()
        expr = res.register(self.expr())
        if res.error: res
        return res.success(expr)
    def expr(self):
        res = ParseResult()
        node = res.register(self.bin_op(self.equal,(TT_EQ,)))
        if res.error: return res
        return res.success(node)
    def equal(self):
        return self.bin_op(self.comp_expr, ((TT_KEYWORD, 'AND'), (TT_KEYWORD, 'OR')))
    def comp_expr(self):
        res = ParseResult()
        if self.current_tok.matches(TT_KEYWORD, 'NOT'):
            op_tok = self.current_tok
            res.register_advancement()
            self.advance()

            node = res.register(self.comp_expr())
            if res.error: return res
            return res.success(UnaryOpNode(op_tok, node))
        
    #    node = res.register(self.bin_op(self.unpack,(TT_COMMA,)))
        
        z =  self.unpack()
        res.register(z)
        if res.error: return res
        if self.not_temp_node == False:
            if self.current_tok.type == TT_COMMA:
                z = self.templist.add(z.node)
                while self.current_tok.type == TT_COMMA:
                    self.advance()
                    s = res.register(self.unpack())
                    if res.error: return res
                    if s:
                        z = self.templist.add(s)
                z = self.templist.copy()
                self.templist.fresh()
        return z
    def unpack(self):
        return self.bin_op(self.arith_expr, (TT_EE,TT_RS,TT_LS, TT_NE, TT_LT, TT_GT, TT_LTE, TT_GTE))
    def arith_expr(self):
        return  self.bin_op(self.term, (TT_PLUS, TT_MINUS))
    def term(self):
        return self.bin_op(self.factor,(TT_MUL, TT_DIV,TT_RD))
    def factor(self):
        res = ParseResult()
        tok = self.current_tok
        if tok.type in (TT_PLUS, TT_MINUS):
            self.update(res)
            factor = res.register(self.factor())
            if res.error: return res
            return res.success(UnaryOpNode(tok, factor))
        return self.power()

    def power(self):
        return self.bin_op(self.attr, (TT_DOT, ))
    def attr(self):
        return self.bin_op(self.call, (TT_POW, ), self.factor)
    def call(self):
        res = ParseResult()
        atom = res.register(self.atom())
        if res.error: return res
        if self.current_tok.type == TT_LPAREN:
            res.register_advancement()
            self.advance()
            arg_nodes = []
            if self.current_tok.type == TT_RPAREN:
                res.register_advancement()
                self.advance()
            else:
                self.not_temp_node = True
                arg_nodes.append(res.register(self.expr()))
                if res.error:
                    return res.failure(InvalidSyntaxError(
                        self.current_tok.pos_start, self.current_tok.pos_end,
                        "Expected ')', 'VAR', 'IF', 'FOR', 'WHILE', 'fun', int, float, identifier, '+', '-', '(' or 'NOT'"
                    ))
                
                while self.current_tok.type == TT_COMMA:
                    res.register_advancement()
                    self.advance()
                    arg_nodes.append(res.register(self.expr()))
                    if res.error: return res
                if self.current_tok.type != TT_RPAREN:
                    return res.failure(InvalidSyntaxError(
                        self.current_tok.pos_start, self.current_tok.pos_end,
                        f"Expected ',' or ')'"
                    ))
                res.register_advancement()
                self.advance()
            return res.success(CallNode(atom, arg_nodes))
        elif self.current_tok.type == TT_LSQUARE:
            self.advance()
            start,stop,skip = None,None,None
            if self.current_tok.type == TT_INT:
                start = self.current_tok
                self.advance()
            if  self.current_tok.type == TT_COLON:
                self.advance()
            if self.current_tok.type == TT_INT:
                stop = self.current_tok
                self.advance()
            if  self.current_tok.type == TT_COLON:
                self.advance()
            if self.current_tok.type == TT_INT:
                stop = self.current_tok
                self.advance()
            if not self.current_tok.type == TT_RSQUARE:
                    return res.failure(InvalidSyntaxError(
                        self.current_tok.pos_start, self.current_tok.pos_end,
                        f"EXPECTED ']'"
                    ))
            self.advance()
            return res.success(SliceNode(atom,start,stop,skip ))
        return res.success(atom)
    def matches_error(self,name):
        if not self.current_tok.matches(TT_KEYWORD, name):
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected '{name}'"
            ))
    def atom(self):
        res = ParseResult()
        tok = self.current_tok
        if tok.type in (TT_INT, TT_FLOAT):
            res.register_advancement()
            self.advance()
            return res.success(NumberNode(tok))
        elif tok.type == TT_STRING:
            res.register_advancement()
            self.advance()
            return res.success(StringNode(tok))
        elif tok.type == TT_IDENTIFIER:
            res.register_advancement()
            self.advance()
            return res.success(VarAccessNode(tok))
        elif tok.type == TT_VBAR:
            res.register_advancement()
            return res.success(self.container()).node
        elif tok.matches(TT_KEYWORD, 'from') or tok.matches(TT_KEYWORD, 'import_'):
            res.register_advancement()
            return res.success(res.register(self.module()))
        elif tok.type == TT_NONE:
            res.register_advancement()
            self.advance()
            return res.success(NoneType(tok))
        elif tok.type == TT_LPAREN:
            res.register_advancement()
            self.advance()
            expr = res.register(self.expr())
            if res.error: return res
            if self.current_tok.type == TT_RPAREN:
                res.register_advancement()
                self.advance()
                if res.error : return res
                return res.success(expr)
            else:
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    "Expected ')'"
                ))
        elif tok.type == TT_LSQUARE:
            list_expr = res.register(self.list_expr())
            self.not_temp_node = True
            self.list_node = False
            if res.error: return res
            return res.success(list_expr)
        elif tok.matches(TT_BOOL, 'True') or tok.matches(TT_BOOL, 'False'):
            res.register_advancement()
            self.advance()
            return res.success(BoolType(tok))
        elif tok.value in ["str","int","list","tuple","dict","function","fn","cls"]:
            res.register_advancement()
            self.advance()
            return res.success(ClassType(tok))
        elif tok.matches(TT_KEYWORD, 'IF'):
            if_expr = res.register(self.if_expr())
            if res.error: return res
            x = res.success(if_expr)
            return x
        elif tok.matches(TT_KEYWORD, 'FOR'):
            for_expr = res.register(self.for_expr())
            if res.error: return res
            return res.success(for_expr)
        elif tok.matches(TT_KEYWORD, 'pass'):
            res.register_advancement()
            self.advance()
            return res.success(Pass_Node(tok))
        elif tok.matches(TT_KEYWORD, 'WHILE'):
            while_expr = res.register(self.while_expr())
            if res.error: return res
            return res.success(while_expr)
        elif tok.matches(TT_KEYWORD, 'class'):
            class_expr = res.register(self.class_expr())
            if res.error: return res
            return res.success(class_expr)
        elif tok.matches(TT_KEYWORD, 'fun'):
            func_def = res.register(self.func_def1())
            if res.error: return res
            return res.success(func_def)
        else:
            return res.failure(InvalidSyntaxError(
                tok.pos_start, tok.pos_end,
                "expected int, float, identifier, '+', '-', '(', 'if', 'for', 'while', 'fun'"
            ))
    def for_expr(self):
        res = ParseResult()

        if not self.current_tok.matches(TT_KEYWORD, 'FOR'):
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected 'FOR'"
            ))

        res.register_advancement()
        self.advance()
        print(self.current_tok)

        if self.current_tok.type != TT_IDENTIFIER:
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected identifier"
            ))
        var_name = self.current_tok
        res.register_advancement()
        self.advance()
        
        if not self.current_tok.matches(TT_KEYWORD, 'in'):
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected in"
            ))
        self.advance()
        res.register_advancement()
        if self.current_tok.type == TT_COLON:
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected identifier or some value"
            ))
        parent = res.register(self.expr())
        
        if not self.current_tok.type == TT_COLON:
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected :"
            ))
        self.advance()
        res.register_advancement()
        if not self.current_tok.type == TT_NEWLINE:
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected an indentation or newline"
            )) 
        self.advance()
        res.register_advancement()
        body = res.register(self.statements())
        if not self.current_tok.matches(TT_KEYWORD, 'END'):
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected END"
            ))
        self.advance()
        res.register_advancement()
        if res.error: return res
        return res.success(ForNode(var_name,parent,body))

    def class_expr(self):
        res = ParseResult()
        arg_name_tok = []
        tok = self.current_tok
        if self.current_tok.matches(TT_KEYWORD, 'class'):
            self.update(res)
            if not self.current_tok.type == TT_IDENTIFIER:
                return res.failure(InvalidSyntaxError(
                    tok.pos_start, tok.pos_end,
                    "Expected int, float, identifier, '+', '-', '(', 'IF', 'FOR', 'WHILE', 'fun'"
                ))
            name = self.current_tok
            self.advance()
        if self.current_tok.type == TT_LPAREN:
            if self.current_tok.type == TT_IDENTIFIER:
                arg_name_toks.append(self.current_tok)
                res.register_advancement()
                self.advance()
                while self.current_tok.type == TT_COMMA:
                    res.register_advancement()
                    self.advance()
                    if self.current_tok.type != TT_IDENTIFIER:
                        return res.failure(InvalidSyntaxError(
                            self.current_tok.pos_start, self.current_tok.pos_end,
                            f"Expected identifier"
                        ))
                    arg_name_toks.append(self.current_tok)
                    res.register_advancement()
                    self.advance()
                if self.current_tok.type != TT_RPAREN:
                    return res.failure(InvalidSyntaxError(
                        self.current_tok.pos_start, self.current_tok.pos_end,
                        f"Expected ',' or ')'"
                    ))
            else:
                if self.current_tok.type != TT_RPAREN:
                    return res.failure(InvalidSyntaxError(
                        self.current_tok.pos_start, self.current_tok.pos_end,
                        f"Expected identifier or ')'"
                    ))
        if not self.current_tok.type == TT_COLON :
            return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    f"Expected :')'"
            ))
        self.advance()
        while self.current_tok.type == TT_NEWLINE:
            self.advance()
        body = self.statements()
        if not self.current_tok.matches(TT_KEYWORD, 'END'):
                return res.failure(InvalidSyntaxError(
                    tok.pos_start, tok.pos_end,
                    "Expected int, float, identifier, '+', '-', '(', 'IF', 'FOR', 'WHILE', 'fun'"
                ))
        self.advance()
        return ClassNode(name,arg_name_tok,body)
    def module(self):
        res = ParseResult()
        if self.current_tok.matches(TT_KEYWORD, 'from'):
            self.advance()
            if not self.current_tok.type == TT_IDENTIFIER:
                return res.failure(InvalidSyntaxError(
                    tok.pos_start, tok.pos_end,
                    "Expected int, float, identifier, '+', '-', '(', 'IF', 'FOR', 'WHILE', 'fun'"
                ))
            to_load = self.current_tok
            self.advance()
        else:
            to_load = self.current_tok
            self.advance()
            to_get = self.current_tok
            self.advance()
        res.register_advancement()
        return res.success(ImportNode(
        VarAccessNode(to_load) , VarAccessNode(to_get)
        ))
    def list_expr(self):
        res = ParseResult()
        element_nodes = []
        self.not_temp_node = True
        self.list_node = True
        pos_start = self.current_tok.pos_start.copy()
        if self.current_tok.type != TT_LSQUARE:
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected '['"
            ))
        res.register_advancement()
        self.advance()
        if self.current_tok.type == TT_RSQUARE:
            res.register_advancement()
            self.advance()
        else:
            element_nodes.append(res.register(self.expr()))
            if res.error:
                return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                "Expected ']', 'VAR', 'IF', 'FOR', 'WHILE', 'fun', int, float, identifier, '+', '-', '(', '[' or 'NOT'"
                ))
            while self.current_tok.type == TT_COMMA:
                res.register_advancement()
                self.advance()
                element_nodes.append(res.register(self.expr()))
                if res.error: return res
            if self.current_tok.type != TT_RSQUARE:
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    f"Expected ',' or ']'"
                ))
            res.register_advancement()
            self.advance()
        return res.success(ListNode(
          element_nodes,
          pos_start,
          self.current_tok.pos_end.copy()
        ))
    def if_expr(self):
        res = ParseResult()
        all_cases = res.register(self.if_expr_cases('IF'))
        if res.error: return res
        cases, else_case = all_cases
        return res.success(IfNode(cases, else_case))

    def if_expr_b(self):
        return self.if_expr_cases('ELIF')
        
    def if_expr_c(self):
        res = ParseResult()
        else_case = None
        

        if self.current_tok.matches(TT_KEYWORD, 'ELSE'):
            res.register_advancement()
            self.advance()

            if self.current_tok.type == TT_NEWLINE:
                res.register_advancement()
                self.advance()

                statements = res.register(self.statements())
                if res.error: return res
                else_case = (statements, True)

                if self.current_tok.matches(TT_KEYWORD, 'END'):
                    res.register_advancement()
                    self.advance()
                else:
                    return res.failure(InvalidSyntaxError(
                        self.current_tok.pos_start, self.current_tok.pos_end,
                        "Expected 'END'"
                    ))
            else:
                expr = res.register(self.statement())
                if res.error: return res
                else_case = (expr, False)

        return res.success(else_case)

    def if_expr_b_or_c(self):
        res = ParseResult()
        cases, else_case = [], None

        if self.current_tok.matches(TT_KEYWORD, 'ELIF'):
            all_cases = res.register(self.if_expr_b())
            if res.error: return res
            cases, else_case = all_cases
        else:
            else_case = res.register(self.if_expr_c())
            if res.error: return res
        
        return res.success((cases, else_case))

    def if_expr_cases(self, case_keyword):
        res = ParseResult()
        cases = []
        else_case = None

        if not self.current_tok.matches(TT_KEYWORD, case_keyword):
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected '{case_keyword}'"
            ))

        res.register_advancement()
        self.advance()

        condition = res.register(self.expr())
        if res.error: return res

        if self.current_tok.matches(TT_KEYWORD, 'THEN'):
            res.register_advancement()
            self.advance() 
            expr = res.register(self.statement())
            if res.error: return res
            cases.append((condition, expr, False))
            all_cases = res.register(self.if_expr_b_or_c())
            if res.error: return res
            new_cases, else_case = all_cases
            cases.extend(new_cases)

        elif self.current_tok.type == TT_COLON:
            res.register_advancement()
            self.advance()
            if not self.current_tok.type == TT_NEWLINE:
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    f"Expected '{case_keyword}'"
                ))
            while self.current_tok.type == TT_NEWLINE :
                self.advance()
                res.register_advancement()
            
            statements = res.register(self.statements())
            if res.error: return res
            cases.append((condition, statements, True))
            

            if self.current_tok.matches(TT_KEYWORD, 'END'):
                res.register_advancement()
                self.advance()
            else:
                all_cases = res.register(self.if_expr_b_or_c())
                if res.error: return res
                new_cases, else_case = all_cases
                cases.extend(new_cases)
        else:
            expr = res.register(self.statement())
            if res.error: return res
            cases.append((condition, expr, False))

            all_cases = res.register(self.if_expr_b_or_c())
            if res.error: return res
            new_cases, else_case = all_cases
            cases.extend(new_cases)
        x = res.success((cases, else_case))
 
        return x

    def container(self):
        get_val,right,left,type_ = None,None,None,"all"
        res = ParseResult()
        res.register_advancement()
        pos_start = self.current_tok.pos_start
        self.advance()
        if self.current_tok.type == TT_VBAR:
            self.advance()
            res.register_advancement()
            return Container("all",NoneType(self.current_tok),pos_start,self.current_tok.pos_end)
        else:
            if self.current_tok.type == TT_IDENTIFIER:
                type_ = self.current_tok.value
                self.advance()
                if not self.current_tok.type == TT_COMMA and not self.tokens[self.tok_idx].type == TT_VBAR:
                    return res.failure(InvalidSyntaxError(
                       self.current_tok.pos_start, self.current_tok.pos_end,
                       f"Expected '|'"
                    ))
                left = self.expr()
                if not self.current_tok.type == TT_LCUR:
                    return res.failure(InvalidSyntaxError(
                        self.current_tok.pos_start, self.current_tok.pos_end,
                        f"Expected 'fun'"
                    ))
                get_val = self.get_cont(type_)
                right = self.expr()
                return get_val if get_val else Container("all",get_val,pos_start,self.current_tok.pos_end)
    def get_cont(self,type_ = None):
        if self.current_tok.type == TT_LCUR:
            self.advance()
            if not self.current_tok.type == TT_RCUR:
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    f"Expected  ']'"
                ))
            else:
                self.advance()
        else:
            self.advance()
            return Container("all",None,pos_start,self.current_tok.pos_end)
    def while_expr(self):
        res = ParseResult()
        if not self.current_tok.matches(TT_KEYWORD, 'WHILE'):
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected 'WHILE'"
            ))

        res.register_advancement()
        self.advance()

        condition = res.register(self.expr())
        if res.error: return res

        if not self.current_tok.type == TT_COLON:
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected ':'"
            ))

        res.register_advancement()
        self.advance()

        if self.current_tok.type == TT_NEWLINE:
            res.register_advancement()
            self.advance()

            body = res.register(self.statements())
            if res.error: return res
            if not self.current_tok.matches(TT_KEYWORD, 'END'):
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    f"Expected 'END'"
                ))

            res.register_advancement()
            self.advance()

            return res.success(WhileNode(condition, body, True))

        body = res.register(self.statement())
        if res.error: return res

        return res.success(WhileNode(condition, body, False))
    def func_def1(self):
        res = ParseResult()
        self.FUN_node = True
        self.matches_error('fun')
        res.register_advancement()
        self.advance()
        
        if self.current_tok.type == TT_IDENTIFIER:
            var_name_tok = self.current_tok
            res.register_advancement()
            self.advance()
            if self.current_tok.type != TT_LPAREN:
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    f"Expected '('"
                ))
        else:
            var_name_tok = None
            if self.current_tok.type != TT_LPAREN:
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    f"Expected identifier or '('"
                ))
        res.register_advancement()
        self.advance()
        arg_name_toks = []
        if self.current_tok.type == TT_MUL:
            print("UNDER DEVELOPMENT of *kwargs")
        if self.current_tok.type == TT_IDENTIFIER:
            arg_name_toks.append(self.current_tok)
            res.register_advancement()
            self.advance()
            while self.current_tok.type == TT_COMMA:
                res.register_advancement()
                self.advance()
                if self.current_tok.type != TT_IDENTIFIER:
                    self.advance()
                    return res.failure(InvalidSyntaxError(
                        self.current_tok.pos_start, self.current_tok.pos_end,
                        f"Expected identifier"
                    ))
                arg_name_toks.append(self.current_tok)
                res.register_advancement()
                self.advance()

            if self.current_tok.type != TT_RPAREN:
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    f"Expected ',' or ')'"
                ))
        else:
            if self.current_tok.type != TT_RPAREN:
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    f"Expected identifier or ')'"
                ))
        res.register_advancement()
        self.advance()
        if self.current_tok.type != TT_DS:
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected '//' "
            ))
        res.register_advancement()
        self.advance()
        if self.current_tok.type != TT_NEWLINE:
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected NEWLINE"
            ))
        res.register_advancement()
        self.advance()
        body = res.register(self.fun_stat())
        if res.error: return res
        if not self.current_tok.type == TT_NEWLINE:
            res.register_advancement()
        return res.success(FuncDefNode(
            var_name_tok,
            arg_name_toks,
            body,
            False
        ))
    def func_def(self):
        res = ParseResult()
        if not self.current_tok.matches(TT_KEYWORD, 'fun'):
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected 'fun'"
            ))
        res.register_advancement()
        self.advance()
        if self.current_tok.type == TT_IDENTIFIER:
            var_name_tok = self.current_tok
            res.register_advancement()
            self.advance()
            if self.current_tok.type != TT_LPAREN:
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    f"Expected '('"
                ))
        else:
            var_name_tok = None
            if self.current_tok.type != TT_LPAREN:
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    f"Expected identifier or '('"
                ))
        res.register_advancement()
        self.advance()
        arg_name_toks = []
        if self.current_tok.type == TT_IDENTIFIER:
            arg_name_toks.append(self.current_tok)
            res.register_advancement()
            self.advance()
            while self.current_tok.type == TT_COMMA:
                res.register_advancement()
                self.advance()
                if self.current_tok.type != TT_IDENTIFIER:
                    return res.failure(InvalidSyntaxError(
                        self.current_tok.pos_start, self.current_tok.pos_end,
                        f"Expected identifier"
                    ))
                arg_name_toks.append(self.current_tok)
                res.register_advancement()
                self.advance()
            if self.current_tok.type != TT_RPAREN:
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    f"Expected ',' or ')'"
                ))
        else:
            if self.current_tok.type != TT_RPAREN:
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    f"Expected identifier or ')'"
                ))
        res.register_advancement()
        self.advance()
        if self.current_tok.type == TT_ARROW:
            res.register_advancement()
            self.advance()
            bode = res.register(self.expr())
            if res.error: return res
            return res.success(FuncDefNode(
                var_name_tok,
                arg_name_toks,
                bode,
                True
            ))
        if self.current_tok.type != TT_NEWLINE:
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected '->' or NEWLINE"
            ))
        res.register_advancement()
        self.advance()
        body = res.register(self.statements())
        self.matches_error('END')
        res.register_advancement()
        self.advance()
        return res.success(FuncDefNode(
            var_name_tok,
            arg_name_toks,
            body,
            False
        ))
    def bin_op(self, func_a, ops, func_b=None):
        if func_b == None:
            func_b = func_a
        res = ParseResult()
        x = func_a()
        left = res.register(x)
        if res.error: return res
        while self.current_tok.type in ops or (self.current_tok.type, self.current_tok.value) in ops:
            op_tok = self.current_tok
            res.register_advancement()
            self.advance()
            right = res.register(func_b())
            type_ = "get" if self.current_tok.type != TT_EQ else "set"
            if res.error: return res
            left = BinOpNode(left, op_tok, right) if op_tok.type != TT_DOT else AttributeNode(right,left,type_)
        return res.success(left)
    
Number(Value)
Temp(Value)
class Class_(BaseFunction):
    def __init__(self, name,context = None, body_node = None, arg_names = None):
        super().__init__(Value)
        self.name = name
        self.repr = f"__main__.{self.name} object of grapes"
        if body_node:
            self.body_node = body_node.node
        self.context = context
        self.arg_names = arg_names
    def execute(self,args):
        res = RTResult()
        if "__init__" in self.__dict__.keys():
            
            x = self.check(self.__init__,args)
            if x:
                res.failure(x)
        args = "" if not args else args
        if res.error:
            return res
        setattr(self,"repr", f"< class {str(self.name)} $attr({args}) > object of grapes")
        return res.success(self) 
    def init(self,name,fun,args):
        res = RTResult()
        
        interpreter = Interpreter()
        exec_ctx = self.generate_new_context()
        res.register(self.check_and_handle_args(fun.arg_names, [String(name)]+args, exec_ctx))
        setattr(self,"self",name)
        if res.should_return(): return res
        value = res.register(fun.execute([String(name)]+args,self))
        
    def check(self,fun,args):
        try:
            its = fun.arg_names[0]
            self.init(its,fun,args)
        except Exception as a:
            return Value_Error(fun.pos_start,fun.pos_end,f"{self.name}.{fun.name} takes 0 positional args 1 given") if len(fun.arg_names) == 0 else None
    def dotted_to(self,other):
        return getattr(self.value,other.var_name_tok.value)
    def format_(self, args,__init__ = False):
        res = RTResult()
        interpreter = Interpreter()
        exec_ctx = self.generate_new_context()

        res.register(self.check_and_handle_args(self.arg_names, args, exec_ctx))
        if res.should_return(): return res
        value = res.register(interpreter.visit(self.body_node, exec_ctx))
        x = Class_(self.name,self.context)
        for element in value.elements:
            x = getattr(self,f"{type(element).__name__}__node")(x,element, exec_ctx )
        self.context.symbol_table.set(self.name,x)

        return res.success(x)
    def Number__node(self,x,elem,exec_ctx):
        return x
    def Identifier__node(self,x,elem,exec_ctx):
        setattr(x,elem.value,exec_ctx.symbol_table.get(elem.value))
        self.repr = f" {self.name}.element.value of grapes"
        return x
    def Function__node(self,x,elem,exec_ctx):
        setattr(x,elem.name,elem)
        return x
    def Function_node(self,func,args):
        setattr(self,"repr",f" {self.name}.element.name of grapes")
        return func.execute(args)
    def VarAccessNode_node(self,name,chain):
        setattr(self,"repr",f" {self.name}.element.name of grapes")
        return getattr(name,chain)
    def copy(self, repr_ = None):
        copy = repr_
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def type_(self):
        return Class(type(self.value)).set_context(self.context), None
    def is_true(self):
        return self.value != 0
    def set_class(self,value):
        if type(value) == int:
            return Number(value)
        elif type(value) == str:
            return String(value)
        elif type(value) == list:
            return List(value)
        else:
            return Class(value)
    def get_comparison_eq(self, other):
        if isinstance(other, Class):
            try:
                return Number(int(self.value.value == other.value)).set_context(self.context), None
            except Exception as a:
                return Number(int(self.value == other.value.value)).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)
    def __repr__(self):
        return self.repr 
class Function(BaseFunction):
  def __init__(self, name, body_node, arg_names, should_auto_return):
    super().__init__(name)
    self.body_node = body_node
    self.repr = f"<bound function {self.name} of gprs>"
    self.arg_names = arg_names
    self.should_auto_return = should_auto_return
  def GRSP_fun():
      pass
      
  def execute(self, args,init = None):
    res = RTResult()
    interpreter = Interpreter()
    exec_ctx = self.generate_new_context()
    res.register(self.check_and_handle_args(self.arg_names, args, exec_ctx))
    self.repr = f"<function {self.name}>"
    if res.should_return(): return res
    value = res.register(interpreter.visit(self.body_node, exec_ctx ,init))
    if res.should_return() and res.func_return_value == None: return res
    ret_value = (value if self.should_auto_return else None) or res.func_return_value or None_.null
    return res.success(ret_value)
  def get_comparison_eq(self, other):
      return Bool(str(self.value == other.value)).set_context(self.context), None
  def copy(self,z = None):
    copy = Function(self.name, self.body_node, self.arg_names, self.should_auto_return)
    if z:
        setattr(copy,"name",z.name)
        setattr(copy,"repr",z.repr)
    copy.set_context(self.context)
    copy.set_pos(self.pos_start, self.pos_end)
    return copy
  def type_(self):
      return Class(type(Function.GRSP_fun)).set_context(self.context), None
  def __repr__(self):
    return self.repr

class Interpreter:
    def visit(self, node, context,type_ = None):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit_method)
        if type_ == "VarAccessNode" or type_ == "AttributeNode":
            return method(node, context,type_)
        elif type_ == "Templist":
            return method(node, context,type_)
        elif type_:
            return method(node, context,type_)
        else:
            return method(node, context)
    def no_visit_method(self, node, context):
        raise Exception(f'No visit_{type(node).__name__} method defined')
    def visit_SliceNode(self,node,context):
        res = RTResult()
        var_name = node.parent.var_name_tok.value
        value = context.symbol_table.get(var_name)
        if not value:
            return res.failure(RTError(
                node.pos_start, node.pos_end,
                f"'{var_name}' is not defined",
                context
            ))
        value,error = value.slice(node.start,node.stop,node.skip)
        return RTResult().success(
            (value).set_context(context).set_pos(node.pos_start, node.pos_end)
            )
    def visit_Pass_Node(self, node, context):
        return RTResult().success(
            Number.null.set_pos(node.pos_start, node.pos_end)
        )
    def visit_Container(self,node, context):
        x = ContainerType(node)
        x.arrange()
        return RTResult().success(
            x.set_context(context).set_pos(node.pos_start, node.pos_end)
        )
    def visit_NumberNode(self, node, context):
        x = Number(node.tok.value)
        return RTResult().success(
            x.set_context(context).set_pos(node.pos_start, node.pos_end)
        )
    def visit_AttributeNode(self, node, context,exter = None):
        res = RTResult()
        class_ = Class(None)
        type_ = node.type_
        i = Interpreter()
        parent = node.parent
        chain = node.chain
        attr = Attribute(parent,parent,chain)
        if node.type_ == "get":
            value,error = attr.getattr1_(parent,chain,i,node,context,exter)  
            type_ = None
            if error:
                return error
            return RTResult().success(
                (value.value).set_context(context).set_pos(node.pos_start, node.pos_end)
                )
        else :
            value = attr.setattr_(parent,chain,i,node,context,exter)
            return RTResult().success(
                    Attribute(value,parent,chain,exter).set_context(context).set_pos(node.pos_start, node.pos_end)
                     )
    def visit_BoolType(self, node, context):
        x = Bool(node.tok.value)
        return RTResult().success(
            x.set_context(context).set_pos(node.pos_start, node.pos_end)
        )
    def visit_ClassType(self, node, context):
        x = Class(node.tok.value)
        if x.value == "int":
            value = int
        elif x.value == "str":
            value = str
        elif x.value == "list":
            value = list
        elif x.value == "tuple":
            value = tuple
        elif x.value == "dict":
            value = dict
        elif x.value in ['fn',"function"]:
            value = type(Function.GRSP_fun)
        elif x.value == "cls":
            value = type(Class)

        context.symbol_table.set(x.value,Class(value))
        return RTResult().success(
            Class(value).set_context(context).set_pos(node.pos_start, node.pos_end)
        )
    def visit_NoneType(self, node, context):
        x = None_(node.tok.value)
        return RTResult().success(
            None_("None").set_context(context).set_pos(node.pos_start, node.pos_end)
        )
    def visit_ReturnNode(self, node, context,exter = None):
        res = RTResult()
        if node.node_to_return:
           value = res.register(self.visit(node.node_to_return, context))
           return res.success_return(value)
        else:
           return res.success(None_.null)
    def visit_StringNode(self, node, context):
        return RTResult().success(
            String(node.tok.value).set_context(context).set_pos(node.pos_start, node.pos_end)
        )
    def visit_Templist(self, node, context, type_ = None): 
        x = Temp(node)

        mode = None
        if type_:
            mode = "make_equal"
        x = x.arrange(node,mode,Interpreter())
        y = Temp(x)
        return RTResult().success(
            y.set_context(context).set_pos(node.pos_start, node.pos_end)
        )
    def visit_VarAccessNode(self, node, context,type_= None):
        res = RTResult()
        if type_:
            x = Identifier(node.var_name_tok.value)
            return RTResult().success(
                x.set_context(context).set_pos(node.pos_start, node.pos_end)
            )
        var_name = node.var_name_tok.value
        value = context.symbol_table.get(var_name)
        if not value:
            return res.failure(RTError(
                node.pos_start, node.pos_end,
                f"'{var_name}' is not defined",
                context
            ))
        return res.success(value)
    def visit_VarAssignNode(self, node, context):
        res = RTResult()
        var_name = node.var_name_tok.value
        value = res.register(self.visit(node.value_node, context))
        if res.error: return res
        context.symbol_table.set(var_name, value)
        return res.success(value)
    def visit_BinOpNode(self, node, context,init= None):
        res = RTResult()
        v = None
        if node.op_tok.type == TT_EQ or node.op_tok.type == TT_DOT:
            v = type(node.left_node).__name__
            if v == "VarAccessNode":
                y = self.visit(node.left_node, context,v)
            elif v == "Templist":
                y = self.visit(node.left_node, context,v)
            
            else:
                y = self.visit(node.left_node, context,init)
                
        else:
            y  = self.visit(node.left_node, context,init)
        left = res.register(y)
        if res.error: return res
        right = res.register(self.visit(node.right_node, context))
        if res.error: return res
        if node.op_tok.type == TT_PLUS:
            result, error = left.added_to(right)
        elif node.op_tok.type == TT_MINUS:
            result, error = left.subbed_by(right)
        elif node.op_tok.type == TT_MUL:
            result, error = left.multed_by(right)
        elif node.op_tok.type == TT_DIV:
            result, error = left.dived_by(right)
        elif node.op_tok.type == TT_RD:
            result, error = left.rdived_by(right)
        elif node.op_tok.type == TT_POW:
            result, error = left.powed_by(right)
        elif node.op_tok.type == TT_EE:
            result, error = left.get_comparison_eq(right)
        elif node.op_tok.type == TT_DOT :
            result, error = left.dotted_to(right)
        elif node.op_tok.type == TT_RS:
            result, error = left.right_shift(right)
        elif node.op_tok.type == TT_LS:
            result, error = left.left_shift(right)
        elif node.op_tok.type == TT_NE:
            result, error = left.get_comparison_ne(right)
        elif node.op_tok.type == TT_LT:
            result, error = left.get_comparison_lt(right)
        elif node.op_tok.type == TT_EQ:
            result,error = left.makeequal(right)
        elif node.op_tok.type == TT_GT:
            result, error = left.get_comparison_gt(right)
        elif node.op_tok.type == TT_LTE:
            result, error = left.get_comparison_lte(right)
        elif node.op_tok.type == TT_GTE:
            result, error = left.get_comparison_gte(right)
        elif node.op_tok.matches(TT_KEYWORD, 'AND'):
            result, error = left.anded_by(right)
        elif node.op_tok.matches(TT_KEYWORD, 'OR'):
            result, error = left.ored_by(right)
        if error:
            return res.failure(error)
        else:
            return res.success(result.set_pos(node.pos_start, node.pos_end))
    def visit_UnaryOpNode(self, node, context):
        res = RTResult()
        number = res.register(self.visit(node.node, context))
        if res.error: return res
        error = None
        if node.op_tok.type == TT_MINUS:
            number, error = number.multed_by(Number(-1))
        elif node.op_tok.matches(TT_KEYWORD, 'NOT'):
            number, error = number.notted()
        if error:
            return res.failure(error)
        else:
            return res.success(number.set_pos(node.pos_start, node.pos_end))
    def visit_IfNode(self, node, context):
        res = RTResult()
        for condition, expr, should_return_null in node.cases:
            condition_value = res.register(self.visit(condition, context))
            if res.should_return(): return res
            if condition_value.is_true():
                expr_value = res.register(self.visit(expr, context))
                if res.should_return(): return res
                return res.success(Number.null if should_return_null else expr_value)
        if node.else_case:
            expr, should_return_null = node.else_case
            expr_value = res.register(self.visit(expr, context))
            if res.should_return(): return res
            return res.success(Number.null if should_return_null else expr_value)
        return res.success(Number.null)
    def visit_ListNode(self, node, context,init = None):
        res = RTResult()
        elements = []
        for element_node in node.element_nodes:
            elements.append(res.register(self.visit(element_node, context,init)))
            x = res.should_return()
            if x:
                return res
        return res.success(
            List(elements).set_context(context).set_pos(node.pos_start, node.pos_end)
        )
    def visit_ForNode(self, node, context):
        res = RTResult()
        var = node.var.value
        parent = node.parent
        body= node.body
        par_value = res.register(self.visit(parent,context))
        if res.error : return res
        par_value = par_value.value
        
        start = 0
        if type(par_value).__name__ == 'Temp':
            par_value = par_value.value
        end = len(par_value)
        while start != end:
            value = par_value[start]
            start+=1
            value = self.form(value)
            context.symbol_table.set(var,value)
            bod_value = res.register(self.visit(body,context))
            print(bod_value)            
            
        return res.success(
            Number.null
            )
    def form(self,value):
        if type(value) == str:
            print("yes")
            value = String(value)
        elif type(value) == int:
            value = Number(value)
        elif type(value) == list:
            value = List(value)
        return value
        
    def visit_ClassNode(self, node, context):
        res = RTResult()
        class_name = node.var_name_tok.value if node.var_name_tok else None
        body_node = node.body_node
        arg_names = [arg_name.value for arg_name in node.arg_name_toks]
        class_value = Class_(class_name,context, body_node, arg_names).set_context(context)
        class_value.format_(arg_names)
        return res.success(class_value)
    def visit_WhileNode(self, node, context):
        res = RTResult()
        elements = []
        while True:
            condition = res.register(self.visit(node.condition_node, context))
            if res.should_return(): return res
            if not condition.is_true():
                break
            value = res.register(self.visit(node.body_node, context))
            if res.should_return() and res.loop_should_continue == False and res.loop_should_break == False: return res
            if res.loop_should_continue:
                continue
            if res.loop_should_break:
                break
            elements.append(value)
        return res.success(
            Number.null if node.should_return_null else
            List(elements).set_context(context).set_pos(node.pos_start, node.pos_end)
        )
    def visit_FuncDefNode(self, node, context):
        res = RTResult()
        func_name = node.var_name_tok.value if node.var_name_tok else None
        body_node = node.body_node
        arg_names = [arg_name.value for arg_name in node.arg_name_toks]
        func_value = Function(func_name, body_node, arg_names, node.should_auto_return).set_context(context).set_pos(node.pos_start, node.pos_end)
        if node.var_name_tok:
            context.symbol_table.set(func_name, func_value)
        return res.success(func_value)
    def visit_CallNode(self, node, context,exter = None):

        global to_print
        res = RTResult()
        args = []
        return_value = None
        value_to_call = res.register(self.visit(node.node_to_call, context))
        if res.should_return(): return res
        if type(value_to_call).__name__ == "Class_":
            value_to_call = value_to_call.copy(value_to_call).set_pos(node.pos_start, node.pos_end)
        else:
            value_to_call = value_to_call.copy().set_pos(node.pos_start, node.pos_end)
        for arg_node in node.arg_nodes:
            if exter:
                name = type(arg_node).__name__
                name,value = getattr(self,f"{name}_name")(arg_node,exter,context)
                if name == exter.self :
                    args.append(res.register(RTResult().success(value)))
            else:
                args.append(res.register(self.visit(arg_node, context)))
            if res.should_return():    return res
        try:
            if type(value_to_call.value).__name__ == "function":
                self.py_fun(value_to_call.value,args)
                return_value = Class(value_to_call.value())
        except Exception as a:
            return_value = res.register(value_to_call.execute(args))
        if res.should_return(): return res
        return_value = return_value.copy(return_value) if type(return_value).__name__ == "Class_" else return_value.copy()
        return_value = return_value.set_pos(node.pos_start, node.pos_end).set_context(context)
        return res.success(return_value)
    def py_fun(self,fun,args):
        pass
    def visit_ImportNode(self,mod,context):
        res = RTResult()
        value_to_call = res.register(self.visit(mod.mod, context))
        return_value = res.register(value_to_call.x(mod.get))
        context.symbol_table.set(mod.get.var_name_tok.value,Module(return_value))
        return res.success(Module(return_value))
    def visit_Class_(self,node,context): return node
    def BinOpNode_name(self,obj,exter,context):
        value = self.visit(obj,context,exter).value
        name,val = getattr(self,f"{type(obj.left_node).__name__}_name")(obj.left_node)
        name = obj.left_node.parent.var_name_tok.value
        return name,value
    def VarAccessNode_name(self,obj,exter,context):
        name = obj.var_name_tok.value
        value = self.visit(exter,context)
        return name,value
    def AttributeNode_name(self,obj,exter = None,context = None):
        name = obj.parent.var_name_tok.value

        value = self.visit(obj,context,exter).value if exter else None
        return name,value
class BuiltInFunction(BaseFunction):
  def __init__(self, name):
    super().__init__(name)
  def execute(self, args):
    res = RTResult()
    exec_ctx = self.generate_new_context()
    method_name = f'execute_{self.name}'
    method = getattr(self, method_name, self.no_visit_method)
    res.register(self.check_and_handle_args(method.arg_names, args, exec_ctx))
    if self.name != "print":
        func = In_Built(self.name)
        return_value = res.register(func.function(exec_ctx,self.pos_start,self.pos_end))
    else:
        return_value = res.register(method(exec_ctx))
    if res.should_return(): return res
    return res.success(return_value)
  def no_visit_method(self, node, context):
    raise Exception(f'No execute_{self.name} method defined')
  def copy(self):
    copy = BuiltInFunction(self.name)
    copy.set_context(self.context)
    copy.set_pos(self.pos_start, self.pos_end)
    return copy

  def __repr__(self): return f"<built-in function {self.name}>"
  def execute_print(self, exec_ctx):
    global to_print
   # print("value is ",exec_ctx.symbol_table.get('value'))
    """
    to_print = []
    to_print += [f">>  {str(repr(exec_ctx.symbol_table.get('value')))}"]
    """

 #   for symbol in exec_ctx.symbol_table.symbols:
 #       symbol = exec_ctx.symbol_table.get(symbol)
 #       print(symbol,type(symbol).__name__)
  #      if type(symbol).__name__ == "Identifier":
##            i = Interpreter()
#            print(i.visit(symbol,exec_ctx))
     #       print(self.symbol_table)
    print(f">>  {str(repr(exec_ctx.symbol_table.get('value')))}")
    return RTResult().success(Number.null)
  execute_print.arg_names = ['value']
  def execute_print_ret(self, exec_ctx): pass
  execute_print_ret.arg_names = ['value']
  def execute_is_num(self, exec_ctx): pass
  execute_is_num.arg_names = ["value"]
  def execute_is_str(self, exec_ctx): pass
  execute_is_str.arg_names = ["value"]
  def execute_Input(self, exec_ctx): 
      print(">>",end = " ")
  execute_Input.arg_names = ["value"]
  def execute_ord(self, exec_ctx): pass
  execute_ord.arg_names = ["value"]
  def execute___all__(self, exec_ctx): pass
  execute___all__.arg_names = ["value"]
  def execute_bool(self, exec_ctx): pass
  execute_bool.arg_names = ["value"]
  def execute_is_bool(self, exec_ctx): pass
  execute_is_bool.arg_names = ["value"]
  def execute_chr(self, exec_ctx): pass
  execute_chr.arg_names = ["value"]
  def execute_is_list(self, exec_ctx): pass
  execute_is_list.arg_names = ["value"]
  def execute_is_fun(self, exec_ctx): pass
  execute_is_fun.arg_names = ["value"]
  def execute_abs(self, exec_ctx): pass
  execute_abs.arg_names = ["value"]
  def execute_iter(self, exec_ctx): pass
  execute_iter.arg_names = ['value']
  def execute_ln(self, exec_ctx): pass
  execute_ln.arg_names = ["list"]
  def execute_type(self, exec_ctx): pass
  execute_type.arg_names = ["value"] 
  def execute_open(self, exec_ctx): pass
  execute_open.arg_names = ["value"] 
  def execute_range(self, exec_ctx): pass
  execute_range.arg_names = ["start","stop"]
  
class BuiltInModule(BaseModule):
  def __init__(self, name): super().__init__(name)
  def no_visit_method(self, node, context): raise Exception(f'No execute_{self.name} method defined')
  def copy(self):
    copy = BuiltInModule(self.name)
    copy.set_context(self.context)
    copy.set_pos(self.pos_start, self.pos_end)
    return copy
  def x(self,get):
      try:
          from importlib import import_module as a
          x = a(get.var_name_tok.value)

          return RTResult().success(x)
      except Exception as g:
          try:
              with open(f"modules//{get.var_name_tok.value}.grps","r") as a:
                  x,y = run(f"{get.var_name_tok.value}.grps",a.read())
                #  val = Attribute.set_grps_mod(x,get.var_name_tok.value)
                #  print("finally",type(val))
                  return RTResult().success(x)
          except Exception as a:
              return RTResult().success(Number(f"{a} \n Grapes/Python has no module named \"{get.var_name_tok.value}\""))
  def __repr__(self):
    return f"<built-in Module {self.name}>"

def execute_print(exec_ctx):
    global to_print
    """
    to_print = []
    to_print += [f">>  {str(repr(exec_ctx.symbol_table.get('value')))}"]
    """
    print(f">>  {str(repr(exec_ctx.symbol_table.get('value')))}")
    return RTResult().success(Number.null)

BuiltInFunction.print =  BuiltInFunction("print")
BuiltInFunction.ln =  BuiltInFunction("ln")
BuiltInFunction.print_ret =  BuiltInFunction("print_ret")
BuiltInFunction.is_number =  BuiltInFunction("is_num")
BuiltInFunction.is_function =  BuiltInFunction("is_fun")
BuiltInFunction.append =  BuiltInFunction("append")#later
BuiltInFunction.is_string =  BuiltInFunction("is_str")
BuiltInFunction.is_list =  BuiltInFunction("is_list")
BuiltInFunction.Input       = BuiltInFunction("Input")
BuiltInModule.import_       = BuiltInModule("import_")
BuiltInFunction.abs       = BuiltInFunction("abs")
BuiltInFunction.iter      = BuiltInFunction("iter")
BuiltInFunction.bool      = BuiltInFunction("bool")
BuiltInFunction.is_bool      = BuiltInFunction("is_bool")
BuiltInFunction.is_bool      = BuiltInFunction("is_bool")
BuiltInFunction.ord      = BuiltInFunction("ord")
BuiltInFunction.chr      = BuiltInFunction("chr")
BuiltInFunction.__all__    = BuiltInFunction("__all__")
BuiltInFunction.type    = BuiltInFunction("type")
BuiltInFunction.open   = BuiltInFunction("open")
BuiltInFunction.range   = BuiltInFunction("range")


global_symbol_table.set('import_', BuiltInModule.import_)#
global_symbol_table.set("INPUT", BuiltInFunction.Input)#
global_symbol_table.set("show", BuiltInFunction.print)#
global_symbol_table.set("PRINT_RET", BuiltInFunction.print_ret)
global_symbol_table.set("ln", BuiltInFunction.ln)#
global_symbol_table.set("is_num", BuiltInFunction.is_number)#
global_symbol_table.set("is_fun", BuiltInFunction.is_function)#
global_symbol_table.set("is_list", BuiltInFunction.is_list)#
global_symbol_table.set("is_str", BuiltInFunction.is_string)#
global_symbol_table.set("abs", BuiltInFunction.abs)#
global_symbol_table.set("iter", BuiltInFunction.iter)
global_symbol_table.set("bool", BuiltInFunction.bool)
global_symbol_table.set("is_bool", BuiltInFunction.is_bool)
global_symbol_table.set("is_bool", BuiltInFunction.is_bool)
global_symbol_table.set("ord", BuiltInFunction.ord)
global_symbol_table.set("chr", BuiltInFunction.chr)
global_symbol_table.set("__all__", BuiltInFunction.__all__)
global_symbol_table.set("type", BuiltInFunction.type)
global_symbol_table.set("open", BuiltInFunction.open)
global_symbol_table.set("range", BuiltInFunction.range)

def run(fn, text ,self_ = None):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error: return None, error
    parser = Parser(tokens)
    ast = parser.parse()
    if ast.error: return None, ast.error
    if ast.node:
        interpreter = Interpreter()
        context = Context('<program>')
        context.symbol_table = global_symbol_table
        if self_ :
            print(global_symbol_table.type(self_))
        result = interpreter.visit(ast.node, context)
        return result.value , result.error
    else:
        return None,None
def start_normal(dir_ = None,file = "untitled",text = None):
    while True:
        text = input(">> ")
        START = time.time()
        x,y = run(file,text)
        if y:
            print(f"\n{y.show_error()} \n")
        else:
            END = time.time()
            if x:
                print(f"{to_print}\nsuccess \n completed in {END-START} seconds   :)")
            else:
                print(f"None")
        START,END = 0,0
def start_GUI(dir_ = None,file = "untitled",text = None):
        print(f"running....  file_name = {file}.grps \nat wdir = {dir_}")
        result , error = run(file,text)
        if error:
            return  None, f"\n {error.show_error()} \n"
        else:
            return to_print,f"\nsuccess \n  completed in "
def all_():
    return global_symbol_table.view()
if __name__ == "__main__":
    self_ = True
 #   test = "class a: ; fun __init__(self)//;self.d = 45;//;END;show(a().d)"
 #   test= 'import_ xmap ; xmap.change("44") '
    x,y = run("SAdfa",'x,my = 6,7')
    if x:
        print(x)
    else:
        if y: 
            print(y.show_error())
        else:
            print("pass")
'''
        start_value = res.register(self.visit(node.start_value_node, context))
        if res.error: return res
        end_value = res.register(self.visit(node.end_value_node, context))
        if res.error: return res
        if node.step_value_node:
            step_value = res.register(self.visit(node.step_value_node, context))
            if res.error: return res
        else:
            step_value = Number(1)
        i = start_value.value
        if step_value.value >= 0:
            condition = lambda: i < end_value.value
        else:
            condition = lambda: i > end_value.value
        while condition():
            context.symbol_table.set(node.var_name_tok.value, Number(i))
            i += step_value.value
            res.register(self.visit(node.body_node, context))
            if res.error: return res
        return res.success(None)
''' 
"""
        mode = None
        if type_:
            mode = "make_equal"
        return RTResult().success(
            Temp(Temp(node).arrange(node,mode,Interpreter())).set_context(context).set_pos(node.pos_start, node.pos_end)
        )
"""