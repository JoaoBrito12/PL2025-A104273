import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'NUMBER',
    'ADD',  
    'SUB',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN'
)

t_ADD = r'\+'
t_SUB = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ignore = " \t"

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()

precedence = (
    ('left', 'ADD', 'SUB'),
    ('left', 'TIMES', 'DIVIDE'),
)

def p_expression_binop(p):
    """expression : expression ADD expression
                  | expression SUB expression
                  | expression TIMES expression
                  | expression DIVIDE expression"""
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        if p[3] == 0:
            print("Erro: Divisão por zero")
            p[0] = None
        else:
            p[0] = p[1] / p[3]

def p_expression_number(p):
    "expression : NUMBER"
    p[0] = p[1]

def p_expression_paren(p):
    "expression : LPAREN expression RPAREN"
    p[0] = p[2]

def p_error(p):
    print("Syntax error")

parser = yacc.yacc()

r = parser.parse("(9-2)*(13-4)")
print(r)