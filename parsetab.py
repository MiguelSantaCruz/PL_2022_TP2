
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "CLOSELIST CODE COMMENT ENDCODE EXPREG IGNORE INDEPENDENTCODE LEX LITERALS OPENLIST PRECEDENT PRODUCAO STARTOFCODE STRING TEXT TOKENS YACCPly : Lex Yacc CodigoLex : LEX Listas ExpregularesListas : Listas ListaListas : Lista : TOKENS '=' STRINGLista : LITERALS '=' STRINGLista : IGNORE '=' STRINGLista : PRECEDENT '=' STRINGExpregulares : Expregulares ExpregularExpregulares : Expregular : EXPREG CODEYacc : YACC Listas ProducoesProducoes : Producoes ProducaoProducoes :  Producao : PRODUCAO CODECodigo : STARTOFCODE ListaComandos ENDCODECodigo : ListaComandos : ListaComandos CODEListaComandos : ListaComandos INDEPENDENTCODEListaComandos : "
    
_lr_action_items = {'LEX':([0,],[3,]),'$end':([1,4,5,7,9,11,17,24,27,30,31,32,33,34,],[0,-17,-4,-1,-14,-3,-12,-16,-13,-5,-6,-7,-8,-15,]),'YACC':([2,3,6,10,11,18,29,30,31,32,33,],[5,-4,-10,-2,-3,-9,-11,-5,-6,-7,-8,]),'TOKENS':([3,5,6,9,11,30,31,32,33,],[-4,-4,12,12,-3,-5,-6,-7,-8,]),'LITERALS':([3,5,6,9,11,30,31,32,33,],[-4,-4,13,13,-3,-5,-6,-7,-8,]),'IGNORE':([3,5,6,9,11,30,31,32,33,],[-4,-4,14,14,-3,-5,-6,-7,-8,]),'PRECEDENT':([3,5,6,9,11,30,31,32,33,],[-4,-4,15,15,-3,-5,-6,-7,-8,]),'EXPREG':([3,6,10,11,18,29,30,31,32,33,],[-4,-10,19,-3,-9,-11,-5,-6,-7,-8,]),'STARTOFCODE':([4,5,9,11,17,27,30,31,32,33,34,],[8,-4,-14,-3,-12,-13,-5,-6,-7,-8,-15,]),'PRODUCAO':([5,9,11,17,27,30,31,32,33,34,],[-4,-14,-3,28,-13,-5,-6,-7,-8,-15,]),'ENDCODE':([8,16,25,26,],[-20,24,-18,-19,]),'CODE':([8,16,19,25,26,28,],[-20,25,29,-18,-19,34,]),'INDEPENDENTCODE':([8,16,25,26,],[-20,26,-18,-19,]),'=':([12,13,14,15,],[20,21,22,23,]),'STRING':([20,21,22,23,],[30,31,32,33,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Ply':([0,],[1,]),'Lex':([0,],[2,]),'Yacc':([2,],[4,]),'Listas':([3,5,],[6,9,]),'Codigo':([4,],[7,]),'Expregulares':([6,],[10,]),'Lista':([6,9,],[11,11,]),'ListaComandos':([8,],[16,]),'Producoes':([9,],[17,]),'Expregular':([10,],[18,]),'Producao':([17,],[27,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Ply","S'",1,None,None,None),
  ('Ply -> Lex Yacc Codigo','Ply',3,'p_Ply','ply-simple.py',106),
  ('Lex -> LEX Listas Expregulares','Lex',3,'p_Lex','ply-simple.py',109),
  ('Listas -> Listas Lista','Listas',2,'p_Listas_list','ply-simple.py',113),
  ('Listas -> <empty>','Listas',0,'p_Listas_empty','ply-simple.py',116),
  ('Lista -> TOKENS = STRING','Lista',3,'p_Lista_tokens','ply-simple.py',119),
  ('Lista -> LITERALS = STRING','Lista',3,'p_Lista_literals','ply-simple.py',123),
  ('Lista -> IGNORE = STRING','Lista',3,'p_Lista_ignore','ply-simple.py',128),
  ('Lista -> PRECEDENT = STRING','Lista',3,'p_Lista_precedent','ply-simple.py',132),
  ('Expregulares -> Expregulares Expregular','Expregulares',2,'p_Expregulares_list','ply-simple.py',136),
  ('Expregulares -> <empty>','Expregulares',0,'p_Expregulares_empty','ply-simple.py',139),
  ('Expregular -> EXPREG CODE','Expregular',2,'p_Expregular_exp','ply-simple.py',142),
  ('Yacc -> YACC Listas Producoes','Yacc',3,'p_Yacc_list','ply-simple.py',165),
  ('Producoes -> Producoes Producao','Producoes',2,'p_Producoes_notempty','ply-simple.py',169),
  ('Producoes -> <empty>','Producoes',0,'p_Producoes_empty','ply-simple.py',172),
  ('Producao -> PRODUCAO CODE','Producao',2,'p_Producao','ply-simple.py',175),
  ('Codigo -> STARTOFCODE ListaComandos ENDCODE','Codigo',3,'p_Codigo_notempty','ply-simple.py',182),
  ('Codigo -> <empty>','Codigo',0,'p_Codigo_empty','ply-simple.py',185),
  ('ListaComandos -> ListaComandos CODE','ListaComandos',2,'p_ListaComandos_code','ply-simple.py',188),
  ('ListaComandos -> ListaComandos INDEPENDENTCODE','ListaComandos',2,'p_ListaComandos_independentcode','ply-simple.py',193),
  ('ListaComandos -> <empty>','ListaComandos',0,'p_ListaComandos_empty','ply-simple.py',197),
]