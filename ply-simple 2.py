import ply.lex as lex 
import ply.yacc as yacc

literals = ['=',',']

tokens = ['LEX','STRING','OPENLIST','CLOSELIST','LITERALS','IGNORE','TOKENS','EXPREG','CODE','YACC','PRECEDENT','COMMENT','PRODUCAO','STARTOFCODE','TEXT','ENDCODE','NEWLINE']

states = [('initial','inclusive'),
          ('list','exclusive'),
          ('comment','exclusive'),
          ('expreg','exclusive'),
          ('code','exclusive'),
          ('function','exclusive'),
          ('codeproductions','exclusive')]
          
t_ANY_ignore = ' \t\r'
t_NEWLINE = r'\n'
t_ANY_STRING = r'\".*\"'
t_ANY_LEX = r'%%\s*LEX'
t_ANY_LITERALS = r'%literals'
t_ANY_IGNORE = r'%ignore'
t_ANY_TOKENS = r'%tokens'
t_ANY_YACC = r'%%\s+YACC'
t_PRECEDENT = r'%precedence'

def t_STARTOFCODE(t):
    r'\$\$'
    lexer.push_state('code')
    return t

def t_ENDCODE(t):
    r'\$\$'
    lexer.pop_state()
    return t



def t_ANY_error(t):
    print("Illegal character " + t.value[0])
    lexer.skip(1)

def p_Ply(p):
    'Ply : Lex Yacc '
    print("hello ply")

def p_Lex(p):
    "Lex : LEX NEWLINE"
    print("hello lex")

def p_Yacc(p):
    "Yacc : YACC NEWLINE"
    print("hello YACC")


def p_error(p):
    if p:
        print("Error when trying to read the symbol '%s' (Token type: %s)" % (p.value, p.type))
    else:
        print("Syntax error at EOF")
        parser.success = False

parser= yacc.yacc()
lexer = lex.lex()
parser.success = True
# Read line from input and parse it
import sys

for linha in sys.stdin:
        lexer.input(linha)
        parser.parse(linha)
        for tok in lexer:
            print(tok)
        
        if parser.success:
            print("Programa estruturalmente correto!")
        else:
            print("Programa com erros... Corrija e tente novamente!")

