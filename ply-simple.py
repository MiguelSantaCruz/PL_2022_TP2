import ply.lex as lex 
import ply.yacc as yacc

literals = ['=',',']

tokens = ['LEX','STRING','OPENLIST','CLOSELIST','LITERALS','IGNORE','TOKENS','EXPREG','CODE','YACC','PRECEDENT','COMMENT','PRODUCOES','STARTOFCODE','TEXT','ENDCODE']

# falta SYMBOLTABLE

states = [('initial','inclusive'),
          ('list','exclusive'),
          ('comment','exclusive'),
          ('expreg','exclusive'),
          ('code','exclusive'),
          ('function','exclusive'),
          ('codeproductions','exclusive')]

t_ANY_STRING = r'\".*\"'
t_ANY_LEX = r'%%\s*LEX'
t_ANY_LITERALS = r'%literals'
t_ANY_IGNORE = r'%ignore'
t_ANY_TOKENS = r'%tokens'
t_YACC = r'%%\s* YACC'
t_PRECEDENT = r'%precedence'

def t_STARTOFCODE(t):
    r'\$\$'
    lexer.push_state('code')

def t_OPENLIST(t):
    r'\['
    lexer.push_state('list')

def t_list_STRING(t):
    r'[^\]]+'
    return t

def t_list_CLOSE(t):
    r'\]'
    lexer.pop_state()

def t_COMMENT(t):
    r'\#\#'
    lexer.push_state('comment')

def t_comment_END(t):
    r'[^\n]+'
    lexer.pop_state()

def t_EXPREG(t):
    r'r\'.*\''
    lexer.push_state('expreg')

def t_expreg_CODEEND(t):
    r'[^\n]+'
    lexer.pop_state()

def t_producoes(t):
    r'\w+\s*:\s*[^\{]*'
    lexer.push_state('codeproductions')

def t_codeproductions_STRING(t):
    r'[^\}]+'
    return t

def t_codeproductions_CLOSE(t):
    r'}'
    lexer.pop_state()

def t_OPENFUNC(t):
    r'def'
    lexer.push_state('function')

def t_function_STRING(t):
    r'[^\n]+'
    lexer.pop_state()
    return t

def t_code_TEXT(t):
    r'(.)+\n'
    return t

def t_code_ENDCODE(t):
    r'/\$\$'
    lexer.pop_state()
    return t

t_ANY_ignore = " \t\n\r"

def t_ANY_error(t):
    print("Illegal character " + t.value[0])
    lexer.skip(1)

# Build the parser
#parser = yacc.yacc()
lexer = lex.lex()
# Read line from input and parse it
import sys
#parser.success = True

for linha in sys.stdin:
        lexer.input (linha)
        for tok in lexer:
            print(tok)
    #parser.parse(linha)
    #if parser.success:
    #    print("Programa estruturalmente correto!")
    #else:
    #    print("Programa com erros... Corrija e tente novamente!")