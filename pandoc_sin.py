import ply.lex as lex 
import ply.yacc as yacc



literals = ["$", "(", ")", '<', '>' ]


reserved = {"for": "K_FOR",
            "foreach" : "K_FOREACH",
            "if": "K_IF",
            "print": "K_PRINT"
            }

tokens = ["ID", "NUM", "LE","GE","EQUALS","NOTEQUALS", "IN"] + list(reserved.values())


def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z]'
    t.type = reserved.get(t.value, 'ID')
    return t


t_LE = "<="
t_GE = ">="
t_EQUALS = "=="
t_NOTEQUALS = "!="
t_IN = "in"
t_ignore = " \t\n\r"

def t_error(t):
    print("Illegal character " + t.value[0])


def p_template(p):
    "template : comandos"

def p_comandos(p):
    "comandos : comandos comando"

def p_comandos_empty(p):
    "comandos : "
    
def p_comando_declaracao(p):
    "comando : declaracao"

def p_declaracao_ID(p):
    "declaracao : '$' ID '$' "
    print("ola")
    # ir buscar ao dicionario ????

def p_declaracao_NUM(p):
    "declaracao : NUM"
    p[0] = p[1]

def p_comando_ciclo(p):
    "comando : ciclo"

def p_ciclo_for(p):
    "ciclo : K_FOR '(' declaracao ')' '{' comandos '}'"
    for i in range(p[3]):
       #print(p[5]) Pensar depois
       pass

def p_ciclo_foreach(p):
    "ciclo : K_FOREACH ID IN ID '{' comandos '}'"
    for p[2] in p[4]:
        # p[6]
        # fzr depois
        pass

def p_comando_condicao(p):
    "comando : condicao"    

def p_condicao(p):
    "condicao : K_IF '(' cond ')' '{' comandos '}' "
    if p[3]:
        #Fzr dps
        pass

def p_cond_maior(p):
    "cond : declaracao '>' declaracao"
    if p[1] > p[4]:
         p[0] = True
    else: p[0] = False

def p_cond_menor(p):
    "cond : declaracao '<' declaracao"
    if p[1] < p[4]:
         p[0] = True
    else: p[0] = False

def p_cond_GE(p):
    "cond : declaracao GE declaracao"
    if p[1] >= p[4]:
         p[0] = True
    else: p[0] = False

def p_cond_LE(p):
    "cond : declaracao LE declaracao"
    if p[1] <= p[4]:
         p[0] = True
    else: p[0] = False

def p_cond_EQUALS(p):
    "cond : declaracao EQUALS declaracao"
    if p[1] == p[4]:
         p[0] = True
    else: p[0] = False

def p_cond_NOTEQUALS(p):
    "cond : declaracao NOTEQUALS declaracao"
    if p[1] != p[4]:
         p[0] = True
    else: p[0] = False

def p_comando_print(p):
    "comando : print"

def p_print_declaracao(p):
    "print : K_PRINT '(' declaracao ')'"
    print(p[3])

def p_print_id(p):
    "print : K_PRINT ID"
    print(p[2])

def p_error(p):
    parser.success = False
    print("Syntax error")

# Build the parser
parser = yacc.yacc()
lexer = lex.lex()

# Read line from input and parse it
import sys
parser.success = True

for linha in sys.stdin:
    parser.parse(linha)
    if parser.success:
        print("Programa estruturalmente correto!")
    else:
        print("Programa com erros... Corrija e tente novamente!")