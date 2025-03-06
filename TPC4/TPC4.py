import ply.lex as lex


txt = """

# DBPedia: obras de Chuck Berry

select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000

"""
tokens = ['SELECT', 'NUMBER', 'AC', 'FC', 
          'WHERE', 'LIMIT', 'VAR', 'STRING']


t_SELECT = r'select'
t_WHERE = r'where'
t_LIMIT = r'LIMIT'
t_VAR = r'\?[a-zA-Z_]\w*'
t_STRING = r'\"[^\"]*\"(@[a-zA-Z]+)?'
t_AC = r'\{'
t_FC = r'\}'
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno+=len(t.value)

def t_error(t):
    t.lexer.skip(1)
    
def t_COMMENT(t):
    r'\#.*'
    pass 


def t_NUMBER(t):
    r'-?\d+'
    t.value = int(t.value)
    return t


lexer = lex.lex()

lexer.input(txt)


with open("output/output.txt", "w", encoding="utf-8") as file:
    for token in lexer:
        file.write(f"{token}\n")
