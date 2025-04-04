
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftADDSUBleftTIMESDIVIDEADD DIVIDE LPAREN NUMBER RPAREN SUB TIMESexpression : expression ADD expression\n                  | expression SUB expression\n                  | expression TIMES expression\n                  | expression DIVIDE expressionexpression : NUMBERexpression : LPAREN expression RPAREN'
    
_lr_action_items = {'NUMBER':([0,3,4,5,6,7,],[2,2,2,2,2,2,]),'LPAREN':([0,3,4,5,6,7,],[3,3,3,3,3,3,]),'$end':([1,2,9,10,11,12,13,],[0,-5,-1,-2,-3,-4,-6,]),'ADD':([1,2,8,9,10,11,12,13,],[4,-5,4,-1,-2,-3,-4,-6,]),'SUB':([1,2,8,9,10,11,12,13,],[5,-5,5,-1,-2,-3,-4,-6,]),'TIMES':([1,2,8,9,10,11,12,13,],[6,-5,6,6,6,-3,-4,-6,]),'DIVIDE':([1,2,8,9,10,11,12,13,],[7,-5,7,7,7,-3,-4,-6,]),'RPAREN':([2,8,9,10,11,12,13,],[-5,13,-1,-2,-3,-4,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,3,4,5,6,7,],[1,8,9,10,11,12,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression ADD expression','expression',3,'p_expression_binop','TP6.py',42),
  ('expression -> expression SUB expression','expression',3,'p_expression_binop','TP6.py',43),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','TP6.py',44),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','TP6.py',45),
  ('expression -> NUMBER','expression',1,'p_expression_number','TP6.py',60),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_paren','TP6.py',64),
]
