import ply.lex as lex 
import ply.yacc as yacc
import re

pcount = 0

literals = ['=',',']

tokens = ['LEX','STRING','OPENLIST','CLOSELIST','LITERALS','IGNORE','TOKENS','EXPREG','CODE','YACC','PRECEDENT','COMMENT','PRODUCAO','STARTOFCODE','TEXT','ENDCODE','INDEPENDENTCODE']

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
t_YACC = r'%%\s*YACC'
t_PRECEDENT = r'%precedence'

def t_STARTOFCODE(t):
    r'\$\$'
    lexer.push_state('code')
    return t

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
    r'r\'[^\']*\''
    lexer.push_state('expreg')
    return t

def t_expreg_CODE(t):
    r'[^\n]+'
    lexer.pop_state()
    return t

def t_PRODUCAO(t):
    r'\w+\s*:\s+[^\{]*'
    lexer.push_state('codeproductions')
    return t

def t_codeproductions_CODE(t):
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

def t_code_INDEPENDENTCODE(t):
    r'(.)+\n'
    return t

def t_code_CODE(t):
    r'def(.)*return.*\n'
    return t

def t_code_ENDCODE(t):
    r'/\$\$'
    lexer.pop_state()
    return t


t_ANY_ignore = " \t\n\r"

def t_ANY_error(t):
    print("Illegal character " + t.value[0])
    lexer.skip(1)

# ---- Parser -----------------------------------------------------------

def p_Ply(p):
    "Ply : Lex Yacc Codigo"

def p_Lex(p):
    "Lex : LEX Listas Expregulares"
    print("import ply.lex as lex")

def p_Listas_list(p):
    "Listas : Listas Lista"

def p_Listas_empty(p):
    "Listas : "

def p_Lista_tokens(p):
    "Lista : TOKENS '=' STRING"
    print("tokens = [" + p[3] + "]")

def p_Lista_literals(p):
    "Lista : LITERALS '=' STRING"
    print("literals = [" + p[3] + "]")
    

def p_Lista_ignore(p):
    "Lista : IGNORE '=' STRING"
    print("ignore = [" + p[3] + "]")

def p_Lista_precedent(p):
    "Lista : PRECEDENT '=' STRING"
    print("precedent = [" + p[3] + "]")

def p_Expregulares_list(p):
    "Expregulares : Expregulares Expregular"

def p_Expregulares_empty(p):
    "Expregulares : "

def p_Expregular_exp(p):
    "Expregular : EXPREG CODE"
    string = re.split(r"\(",p[2])
    if string[0] == "return":
        returnArgs = re.split(r"\'",p[2])
        print("def t_" + returnArgs[1] + "(t):\n\t",end="")
        print(p[1])
        code = returnArgs[2].split(",")
        print("\tt.value =" + code[1][:-1])
        print("\treturn t")
    elif string[0] == "error":
        print("def t_error(t):")
        # Separar error(blabla, bla) em "error"" e "blabla, bla)"
        errorCode = p[2].split("(",1)
        # Transformar "blabla, bla)" em ")alb, albalb"
        errorCodeReversed = errorCode[1][::-1]
        # Fazer split pela virgula
        parsedString = str(errorCodeReversed).split(",",1)
        print("\tprint(" + parsedString[1][::-1] + ")")
        parsedString = parsedString[0][::-1]
        print("\t" + parsedString[:-1])
    print("")

def p_Yacc_list(p):
    "Yacc : YACC Listas Producoes"
    print("import ply.yacc as yacc")

def p_Producoes_notempty(p):
    "Producoes : Producoes Producao"

def p_Producoes_empty(p):
    "Producoes :  "

def p_Producao(p):
    "Producao : PRODUCAO CODE"
    global pcount
    print("def p_" + str(pcount) + "(p):\n\t\"" + p[1].rstrip(" ") + "\"\n\t" + p[2][1:])
    pcount = pcount + 1
    print("")

def p_Codigo_notempty(p):
    "Codigo : STARTOFCODE ListaComandos ENDCODE"

def p_Codigo_empty(p):
    "Codigo : "

def p_ListaComandos_code(p):
    "ListaComandos : ListaComandos CODE"
    words = p[2].split(" ")
    print(p[2],end="")
    
def p_ListaComandos_independentcode(p):
    "ListaComandos : ListaComandos INDEPENDENTCODE"
    print()
    
def p_ListaComandos_empty(p):
    "ListaComandos : "

def p_error(p):
    print("Syntax Error: ",p)
    parser.success = False

parser = yacc.yacc()

lexer = lex.lex()
# Read line from input and parse it
import sys
parser.success = True


program = sys.stdin.read()
#parser.parse(program)
#if parser.success:
#    print("Programa estruturalmente correto!")
#else:
#    print("Programa com erros... Corrija e tente novamente!")

lexer.input(program)
for tok in lexer:
    print(tok)
