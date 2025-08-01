'''
Lexer.py

The lexer (tokenizer) converts the input source code string into a sequence of tokens.
It tracks character positions for accurate error reporting and supports custom token types defined in "tokens.py".
'''

import string
from tokenizer import Token
from Position import Position
from tokens import *
__all__ = ['Lexer']

DIGITS = '0123456789'
LETTERS = string.ascii_letters
LETTERS_DIGITS = LETTERS + DIGITS

class Lexer:
    def __init__(self, fn, text):
        self.fn = fn
        self.text = text
        self.pos = Position(-1, 0, -1, fn, text)
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char in "_":
                self.advance()
                if self.current_char ==  "/":
                    tokens.append(Token(TT_RD, pos_start=self.pos))
                    self.advance()
                else:
                    tokens.append(self.make_identifier("_"))
            elif self.current_char in LETTERS+"_":
                tokens.append(self.make_identifier())
            elif self.current_char == '"' or self.current_char == "'":
                type_ = "'" if self.current_char == "'" else '"'
                tokens.append(self.make_string(type_))
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS, pos_start=self.pos))
                self.advance()
            elif self.current_char in ';\n':
                tokens.append(Token(TT_NEWLINE, pos_start=self.pos))
                self.advance()
            elif self.current_char == '-':
                if self.pos.idx+1 < len(self.text):
                    if self.text[self.pos.idx+1] == '-':
                        error = self.skip_comment()
                        
                        self.advance()
                        if error: return [] , error
                if self.current_char == '-':
                    tokens.append(self.make_minus_or_arrow())
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL, pos_start=self.pos))
                self.advance()
            elif self.current_char == '/':
                self.advance()
                if self.current_char == '/':
                    tokens.append(Token(TT_DS, pos_start=self.pos))
                    self.advance()
                else:
                    tokens.append(Token(TT_DIV, pos_start=self.pos))
            elif self.current_char == '^':
                tokens.append(Token(TT_POW, pos_start=self.pos))
                self.advance()
            elif self.current_char == '.':
                tokens.append(Token(TT_DOT, pos_start=self.pos))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN, pos_start=self.pos))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN, pos_start=self.pos))
                self.advance()
            elif self.current_char == '}':
                tokens.append(Token(TT_RCUR, pos_start=self.pos))
                self.advance()
            elif self.current_char == '~':
                tokens.append(Token(TT_NRLY, pos_start=self.pos))
                self.advance()
            elif self.current_char == '{':
                tokens.append(Token(TT_LCUR, pos_start=self.pos))
                self.advance()
            elif self.current_char == '[':
                tokens.append(Token(TT_LSQUARE, pos_start=self.pos))
                self.advance()
            elif self.current_char == ']':
                tokens.append(Token(TT_RSQUARE, pos_start=self.pos))
                self.advance()
            elif self.current_char == '|':
                tokens.append(Token(TT_VBAR, pos_start=self.pos))
                self.advance()
            elif self.current_char == ':':
                tokens.append(Token(TT_COLON, pos_start=self.pos))
                self.advance()
            elif self.current_char == '_':
                self.advance()
                if self.current_char == '/':
                    tokens.append(Token(TT_RD, pos_start=self.pos))
                    self.advance()
                else:
                    tokens.append(Token(TT_US, pos_start=self.pos))
            elif self.current_char == '!':
                token, error = self.make_not_equals()
                if error: return [], error
                tokens.append(token)
            elif self.current_char == '=':
                tokens.append(self.make_equals())
            
            elif self.current_char == '<':
                tokens.append(self.make_less_than())
            elif self.current_char == '>':
                tokens.append(self.make_greater_than())
            elif self.current_char == ',':
                tokens.append(Token(TT_COMMA, pos_start=self.pos))
                self.advance()
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, "'" + char + "'")

        tokens.append(Token(TT_EOF, pos_start=self.pos))
        return tokens, None

    def make_number(self):
        num_str = ''
        dot_count = 0
        pos_start = self.pos.copy()

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
            num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(TT_INT, int(num_str), pos_start, self.pos)
        else:
            return Token(TT_FLOAT, float(num_str), pos_start, self.pos)

    def make_string(self,type_):
        string = ''
        pos_start = self.pos.copy()
        escape_character = False
        self.advance()

        escape_characters = {
            'n': '\n',
            't': '\t'
        }

        while self.current_char != None and (self.current_char != type_ or escape_character):
            if escape_character:
                string += escape_characters.get(self.current_char, self.current_char)
            else:
                if self.current_char == '\\':
                    escape_character = True
                else:
                    string += self.current_char
            self.advance()
            escape_character = False
        self.advance()
        return Token(TT_STRING, string, pos_start, self.pos)

    def make_identifier(self,s = ""):
        id_str = s+''
        pos_start = self.pos.copy()

        while self.current_char != None and self.current_char in LETTERS_DIGITS + '_':
            id_str += self.current_char
            self.advance()
        if id_str in KEYWORDS:
            tok_type = TT_KEYWORD
        elif id_str in BOOL:
            tok_type = TT_BOOL
        elif id_str == TT_NONE:
            tok_type = TT_NONE
        else:
            tok_type = TT_IDENTIFIER
        return Token(tok_type, id_str, pos_start, self.pos)

    def make_minus_or_arrow(self):
        tok_type = TT_MINUS
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == '>':
            self.advance()
            tok_type = TT_ARROW

        return Token(tok_type, pos_start=pos_start, pos_end=self.pos)

    def make_not_equals(self):
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == '=':
            self.advance()
            return Token(TT_NE, pos_start=pos_start, pos_end=self.pos), None

        self.advance()
        return None, ExpectedCharError(pos_start, self.pos, "'=' (after '!')")
    
    def make_equals(self):
        tok_type = TT_EQ
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == '=':
            self.advance()
            tok_type = TT_EE

        return Token(tok_type, pos_start=pos_start, pos_end=self.pos)

    def make_less_than(self):
        tok_type = TT_LT
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == '=':
            self.advance()
            tok_type = TT_LTE
        elif self.current_char == '<':
            self.advance()
            tok_type = TT_LS

        return Token(tok_type, pos_start=pos_start, pos_end=self.pos)

    def make_greater_than(self):
        tok_type = TT_GT
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == '=':
            self.advance()
            tok_type = TT_GTE
        elif self.current_char == '>':
            self.advance()
            tok_type = TT_RS
        return Token(tok_type, pos_start=pos_start, pos_end=self.pos)

    def skip_comment(self):
        comment_ind = self.pos.col
        pos_start = self.pos.copy()
        self.advance()
        if self.current_char == "-":
            self.advance()
            if self.current_char == "-" and comment_ind == 0:
                self.stop___ = self.text.find("---",self.pos.idx)
                if self.stop___ == -1:
                    return InvalidSyntaxError(pos_start, self.pos, "unexpected use of comment")
                else:
                    for i in range(self.stop___-self.pos.idx+2):
                        self.advance()
            else:
                self.stop__ = self.text.find("--",self.pos.idx)
                if self.stop__ != -1:
                    for i in range(self.stop__-self.pos.idx+1):
                        self.advance()
                else:
                    return InvalidSyntaxError(pos_start, self.pos, "unexpected use of comment")