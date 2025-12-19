from lark import Lark

grammar = r"""
start: statement+

statement: NAME "is" value

?value: NUMBER        -> number
      | STRING        -> string
      | array
      | const_ref

array: "{" [value ("," value)*] "}"
const_ref: "|" NAME "|"

NAME: /[a-z]+/
NUMBER: /[1-9][0-9]*/
STRING: /@"[^"]*"/

%import common.WS
%ignore WS
"""

parser = Lark(grammar, parser="lalr")