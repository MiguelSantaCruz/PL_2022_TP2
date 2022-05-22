import ply.lex as lex 
import ply.yacc as yacc
import re

pcount = {}



literals = ['=',',']

tokens = ['LEX','STRING','CLOSELIST','LITERALS','IGNORE','TOKENS','EXPREG','CODE','YACC','PRECEDENT','COMMENT',
'PRODUCAO','STARTOFCODE','ENDCODE','INDEPENDENTCODE','CLOSEDIC','DIC']

states = [('initial','inclusive'),
          ('list','exclusive'),
          ('dictionary','exclusive'),
          ('comment','exclusive'),
          ('expreg','exclusive'),
          ('code','exclusive'),
          ('function','exclusive'),
          ('codeproductions','exclusive')]

t_list_ignore = " \n\t\r"
t_dictionary_ignore = " \n\t\r"
t_comment_ignore = " \n\t\r"
t_expreg_ignore = " \n\t\r"
t_code_ignore = "\n"
t_codeproductions_ignore = " \n\t\r"
t_function_ignore = " \n\t\r"
t_ignore = " \n\t\r"
    

t_ANY_STRING = r'\".*\"'
t_ANY_LEX = r'%%\s*LEX'
t_ANY_LITERALS = r'%literals'
t_ANY_IGNORE = r'%ignore'
t_ANY_TOKENS = r'%tokens'
t_ANY_YACC = r'%%\s*YACC'
t_ANY_PRECEDENT = r'%precedence'
t_ANY_DIC = r'\&[a-zA-Z_]+'

def t_STARTOFCODE(t):
    r'\$\$'
    lexer.push_state('code')
    return t



def t_openlist(t):
    r'\['
    lexer.push_state('list')

def t_list_STRING(t):
    r'[^\]]+'
    return t

def t_list_CLOSELIST(t):
    r'\]'
    lexer.pop_state()

def t_dicionario(t):
    r'\{'
    lexer.push_state('dictionary')

def t_dictionary_STRING(t):
    r'[^\}]+'
    return t

def t_dictionary_CLOSEDIC(t):
    r'\}'
    lexer.pop_state()
    return t

def t_COMMENT(t):
    r'\#\#'
    lexer.push_state('comment')

def t_comment_COMMENT(t):
    r'[^\n]+'
    lexer.pop_state()
    return t

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

def t_ANY_error(t):
    print("Illegal character: " + t.value[0] + str(t.lexer.lineno))
    lexer.skip(1)

# ---- Parser -----------------------------------------------------------

def p_Ply(p):
    "Ply : Lex Yacc Codigo"
    p[0] = str(p[1]) + str(p[2]) + str(p[3])
    print(p[0])

def p_Lex(p):
    "Lex : LEX Listas Expregulares"
    p[0] = "import ply.lex as lex\n\n" + str(p[2]) + str(p[3])

def p_Listas_list(p):
    "Listas : Listas Lista"
    p[0] = str(p[1]) + str(p[2])

def p_Listas_empty(p):
    "Listas : "
    p[0] = ""

def p_Lista_tokens(p):
    "Lista : TOKENS '=' STRING"
    p[0] = "tokens = [" + str(p[3]) + "]\n\n"

def p_Lista_literals(p):
    "Lista : LITERALS '=' STRING"
    p[0] = "literals = [" + str(p[3][1:-1]) + "]\n"
    
def p_Lista_ignore(p):
    "Lista : IGNORE '=' STRING"
    p[0] = "ignore = [" + str(p[3]) + "]\n"

def p_Lista_precedent(p):
    "Lista : PRECEDENT '=' STRING"
    p[0] = "precedent = [" + str(p[3]) + "]\n\n"

def p_Lista_ts(p):
    "Lista : DIC '=' STRING CLOSEDIC" 
    p[0] = str(p[1][1:]) + " = {" + str(p[3]) + "}\n"

def p_Lista_tsempty(p):
    "Lista : DIC '=' CLOSEDIC"
    p[0] = "ts = { }\n"

def p_Lista_comment(p):
    "Lista : COMMENT"
    p[0] =  "# " + p[1] + "\n"

def p_Expregulares_list(p):
    "Expregulares : Expregulares Expregular"
    p[0] = str(p[1]) + str(p[2])

def p_Expregulares_empty(p):
    "Expregulares : "
    p[0] = ""

def p_Expregular_exp(p):
    "Expregular : EXPREG CODE"
    string = re.split(r"\(",p[2])
    if string[0] == "return":
        returnArgs = re.split(r"\'",p[2])
        p[0] = "def t_" + returnArgs[1] + "(t):\n\t"
        p[0] = str(p[0]) + p[1] + "\n"
        code = returnArgs[2].split(",")
        p[0] = str(p[0]) + "\tt.value =" + code[1][:-1] + "\n"
        p[0] = str(p[0]) + "\treturn t\n\n" 
    elif string[0] == "error":
        p[0] = "def t_error(t):\n"
        strPrint = p[2].split("\"")
        p[0] = str(p[0]) + "\tprint(f\"" + strPrint[1] + "\")"
        code = strPrint[2].split(",")
        for i in code:
            if i.endswith("))"):
                p[0] = str(p[0]) + "\t" + i[:-1].strip() + "\n"
            else:
                p[0] = str(p[0]) + "\t" + i.strip() + "\n"
    p[0] = str(p[0]) + "\n"

def p_Expregular_comment(p):
    "Expregular : COMMENT"
    p[0] =  "# " + p[1] + "\n"

def p_Yacc_list(p):
    "Yacc : YACC Listas Producoes"
    p[0]="import ply.yacc as yacc\n\n"  + str(p[2]) + "\n"+ str(p[3]) + "\n"

def p_Producoes_notempty(p):
    "Producoes : Producoes Producao"
    p[0] = str(p[1]) + str(p[2])

def p_Producoes_empty(p):
    "Producoes :  "
    p[0] = ""

def p_Producao(p):
    "Producao : PRODUCAO CODE"
    #global pcount
    nomeproducao = str(p[1].rstrip(" ")).split(" ",1)
    if nomeproducao[0] in pcount:
        pcount[nomeproducao[0]] = pcount[nomeproducao[0]] + 1
        p[0] = "def p_" + str(nomeproducao[0]) + "_" + str(pcount[nomeproducao[0]]) + "(p):\n\t\"" +str(p[1].rstrip(" ")) + "\"\n\t" + str(p[2][1:]).strip(" ") + "\n"
    else:
        pcount[nomeproducao[0]] = 0
        p[0] = "def p_" + str(nomeproducao[0]) + "_" + str(pcount[nomeproducao[0]]) + "(p):\n\t\"" +str(p[1].rstrip(" ")) + "\"\n\t" + str(p[2][1:]).strip(" ") + "\n"

def p_Producao_comment(p):
    "Producao : COMMENT"
    p[0] =  "# " + p[1] + "\n"

def p_Codigo_notempty(p):
    "Codigo : STARTOFCODE ListaComandos ENDCODE"
    p[0] = p[2]

def p_Codigo_empty(p):
    "Codigo : "
    p[0] = ""
    
def p_ListaComandos_independentcode(p):
    "ListaComandos : ListaComandos INDEPENDENTCODE"
    p[0] = str(p[1]) +  str(p[2])
    
def p_ListaComandos_empty(p):
    "ListaComandos : "
    p[0] = ""

def p_error(p):
    print("Syntax Error: ",p)
    parser.success = False

parser = yacc.yacc()

lexer = lex.lex()
# Read line from input and parse it
import sys
parser.success = True


program = sys.stdin.read()
parser.parse(program)
if not parser.success:
    print("Programa com erros... Corrija e tente novamente!")

""" lexer.input(program)
for tok in lexer:
    print(tok) """
