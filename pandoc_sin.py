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


def p_template(p):
    "template : comandos"

def p_comandos(p):
    "comandos : comandos comando"
    
def p_comando_declaracao(p):
    "comando : declaracao"

def p_declaracao_ID(p):
    "declaracao : '$' ID '$' "

def p_declaracao_NUM(p):
    "declaracao : NUM"

def p_comando_ciclo(p):
    "comando : ciclo"

def p_ciclo_for(p):
    "ciclo : K_FOR '(' declaracao ')' '{' comandos '}'"

def p_ciclo_foreach(p):
    "ciclo : K_FOREACH ID IN ID '{' comandos '}'"

def p_comando_condicao(p):
    "comando : condicao"

def p_condicao(p):
    "condicao : K_IF '(' cond ')' '{' comandos '}' "

def p_cond_maior(p):
    "cond : declaracao '>' declaracao"

def p_cond_menor(p):
    "cond : declaracao '<' declaracao"

def p_cond_GE(p):
    "cond : declaracao GE declaracao"

def p_cond_LE(p):
    "cond : declaracao LE declaracao"

def p_cond_EQUALS(p):
    "cond : declaracao EQUALS declaracao"

def p_cond_NOTEQUALS(p):
    "cond : declaracao NOTEQUALS declaracao"

def p_comando_print(p):
    "comando : print"

def p_print_declaracao(p):
    "print : K_PRINT '(' declaracao ')'"

def p_print_id(p):
    "print : K_PRINT ID"
