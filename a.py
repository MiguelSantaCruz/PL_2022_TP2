import ply.lex as lex

literals = ["+-/*=()"]
ignore = [" \t\n"]
tokens = ['VAR','NUMBER' ]

def t_VAR(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	t.value = t.value
	return t

def t_NUMBER(t):
	r'\d+(\.\d+)?'
	t.value = float(t.value)
	return t

def t_error(t):
	print(f"Illegal character '{t.value[0]}', [{t.lexer.lineno}]")
	t.lexer.skip(1) 

import ply.yacc as yacc

precedent = [('left','+','-'),
('left','*','/'),
('right','UMINUS'),
]

ts = { }

def p_0(p):
	"stap : VAR '=' exp"
	ts[p[1]] = p[3]
def p_1(p):
	"stap : exp"
	print(p[1])
def p_2(p):
	"exp : exp '+' exp"
	p[0] = p[1] + p[3]
def p_3(p):
	"exp : exp '-' exp"
	p[0] = p[1] - p[3]
def p_4(p):
	"exp : exp '*' exp"
	p[0] = p[1] * p[3]
def p_5(p):
	"exp : exp '/' exp"
	p[0] = p[1] / p[3]
def p_6(p):
	"exp : '-' exp"
	p[0] = -p[2]
def p_7(p):
	"exp : '(' exp ')'"
	p[0] = p[2]
def p_8(p):
	"exp : NUMBER"
	p[0] = p[1]
def p_9(p):
	"exp : VAR"
	p[0] = getval(p[1])

def p_error(t):
    print(f"Syntax error at '{t.value}', [{t.lexer.lineno}]")
    
def getval(n):
    if n not in ts: print(f"Undefined name '{n}'")
    return ts.get(n,0)
y=yacc()
y.parse("3+4*7")

