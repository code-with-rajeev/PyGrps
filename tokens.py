"""
tokens.py

This module defines all token types used in the PYGRPS language lexer and parser.
It includes keywords, operators, delimiters, and special values used during tokenization.
"""

# Token Types for Primitive Data
TT_INT            = 'INT'
TT_FLOAT          = 'FLOAT'
TT_STRING         = 'STRING'
TT_BOOL           = 'BOOL'
TT_NONE           = 'None'
TT_IDENTIFIER     = 'IDENTIFIER'

# Token Types for Operators
TT_PLUS           = 'PLUS'
TT_MINUS          = 'MINUS'
TT_MUL            = 'MUL'
TT_DIV            = 'DIV'
TT_POW            = 'POW'
TT_EQ             = 'EQ'
TT_EE             = 'EE'     # ==
TT_NE             = 'NE'     # !=
TT_LT             = 'LT'
TT_GT             = 'GT'
TT_LTE            = 'LTE'
TT_GTE            = 'GTE'
TT_ARROW          = 'ARROW'  # ->

# Token Types for Delimiters & Punctuation
TT_LPAREN         = 'LPAREN'
TT_RPAREN         = 'RPAREN'
TT_LSQUARE        = 'LSQUARE'
TT_RSQUARE        = 'RSQUARE'
TT_LCUR           = 'LCUR'
TT_RCUR           = 'RCUR'
TT_COMMA          = 'COMMA'
TT_COLON          = 'COLON'
TT_DOT            = 'DOT'
TT_NEWLINE        = 'NEW_LINE'
TT_EOF            = 'EOF'

# Custom Symbols (PYGRPS-specific)
TT_VBAR           = 'VBAR'   # |
TT_RS             = 'RS'     # >>
TT_LS             = 'LS'     # <<
TT_US             = 'US'     # __
TT_RD             = 'RD'     # ~>
TT_DS             = 'DS'     # ::
TT_NRLY           = 'NRLY'   # ~|

# Keywords in the PYGRPS Language
KEYWORDS = [
    'AND',
    'OR',
    'NOT',
    'IF',
    'ELIF',
    'ELSE',
    'pass',
    'TRUE',
    'FALSE',
    'FOR',
    'TO',
    'int',
    'str',
    'list',
    'fn',
    'fun',
    'function',
    'cls',
    'dict',
    'END',
    'STEP',
    'WHILE',
    'THEN',
    'from',
    'import_',
    'class',
    'in'
]

# Boolean Literals
BOOL = [
    "True",
    "False"
]