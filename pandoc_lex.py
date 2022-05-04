import ply.lex as lex 
import ply.yacc as yacc



literals = ["{", "}", "<", ">"]


#ver isto que nao sei usar
reserved = {"for": "for",
            "foreach"
            }

tokens = ["ID", "NUM"] + list(reserved.values())

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z]'
    t.type = reserved.get(t.value, 'ID')
    return t

t_ignore = " \t\n\r"

def p_template(p):
    "template : comandos"
    p[0] = p[1]

def p_comandos(p):
    "comandos : comandos comando"
    p[0] = 

def p_comando_declaracao(p):
    "comando : declaracao"
    p[0] = p[1]

def p_comando_if(p):
    "comando : 'if' cond declaracao"
    p[0] = p[3]

def p_comando_for(p):
    "comando : 'for' num declaracao"
    p[0] = p[3] 

def p_comando_foreach(p):
    "comando : 'foreach' ID 'in' ID"
    p[0] = p[4] 

def p_declaracao(p):
    "declaracao : '{' ID '=' NUM '}'"
    p[0] = 

def p_cond_maior(p):
    "cond : exp '>' exp"
    p[0] =

def p_cond_menor(p):
    "cond : exp '<' exp"
    p[0] =

def p_cond_maiorigual(p):
    "cond : exp '>=' exp"
    p[0] =

def p_cond_menorigual(p):
    "cond : exp '<=' exp"
    p[0] =

def p_cond_igual(p):
    "cond : exp '==' exp"
    p[0] =

def p_exp_num(p):
    "exp : NUM"
    p[0] = p[1]

def p_exp(p):
    "exp : ID '.get(' NUM ')'"
    p[0] =