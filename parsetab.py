
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMPERS AND ARRAY AT BEGIN BOOLAND BOOLOR BREAK CASE CLASS COLON COMMA COMMENT COMPX DEF DIVIDE DO DOLLARSGN DOT DUODOT ELSE ELSIF END ENSURE EQCOMP EQUALS EXPON FALSE FLOAT FOR GREATEQTH GREATH ID IF IN INT LBRACE LBRAKET LESSEQTH LESSTH LPAREN MINUS MINUSEQ MODULE NEW NEXT NIL NOT NOTEQ OR PIPE PLUS PLUSEQ RAT RBRACE RBRAKET RETRY RETURN ROCKET RPAREN SELF SEMICOLON SET STRING SUPER THEN TILDE TIMES TRIDOT TRUE UNDERSCR UNLESS UNTIL WHEN WHILEinit : cmmdbool : TRUE\n    | FALSE\n    num : INT\n    | FLOAT\n    | RAT\n    | COMPX\n    optr : PLUS\n    | MINUS\n    | TIMES\n    | DIVIDE\n    | MODULE\n    | EXPON\n    optn : num optr numcomptn : obj comptr objcomptr : EQCOMP\n    | LESSTH\n    | LESSEQTH\n    | GREATH\n    | GREATEQTH\n    | NOTEQ\n    var : ID EQUALS obj\n    | ID EQUALS ID\n    | ID EQUALS NIL\n    \n    func : DEF ID LPAREN objs RPAREN cmmd END\n    | DEF ID LPAREN RPAREN cmmd END\n    | DEF ID cmmd END\n    | DEF ID LPAREN objs RPAREN cmmd RETURN obj END\n    | DEF ID LPAREN RPAREN cmmd RETURN obj END\n    | DEF ID cmmd RETURN obj END\n    else : ELSE comptn cmmd\n    | ELSE bool cmmd\n    elsif : ELSIF comptn cmmd\n    | ELSIF bool cmmd\n    elses : else\n    | elsif elses\n    control : IF comptn cmmd END\n    | IF bool cmmd END\n    | IF comptn cmmd elses END\n    | IF bool cmmd elses END\n    control : UNLESS comptn COLON cmmd END\n    | UNLESS bool COLON cmmd END\n    | UNLESS comptn cmmd elses END\n    | UNLESS bool cmmd elses END\n    when : WHEN objs\n    | WHEN objs THEN\n    | WHEN comptn\n    whens : when\n    | when whens\n    control : CASE ID whens else END\n    | CASE ID whens END\n    ids : ID\n    | ID COMMA idsarray : LBRAKET objs RBRAKET\n    | LBRAKET ids RBRAKET\n    | LBRAKET objs COMMA ids RBRAKET\n    | LBRAKET ids COMMA objs RBRAKET\n    strucSet : SET DOT NEW\n    | SET DOT NEW LPAREN RPAREN\n    | SET DOT NEW LPAREN array RPAREN\n    | SET array\n    claveHash : STRING\n    | num\n    | bool\n    | range\n    | matrix\n    elementHash : claveHash ROCKET objelementsHash  : elementHash COMMA elementHash\n     | elementHash COMMA elementsHash\nhash : LBRACE elementsHash RBRACE\n    control : WHILE comptn DO cmmd END\n    | WHILE bool DO cmmd ENDobjs : obj\n    | obj COMMA objs\n    obj : STRING\n    | num\n    | bool\n    | range\n    | matrix\n    | hash\n    | strucSet\n    range : LPAREN INT DOT DOT INT RPAREN\n    | INT DOT DOT INT\n    | LPAREN STRING DOT DOT STRING\n    | STRING DOT DOT STRING\n    cmmd : var\n    | func\n    | control\n    | optn\n    matrix : LBRAKET rows RBRAKET rows : row\n    | row COMMA rowsrow : array'
    
_lr_action_items = {'ID':([0,8,11,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,36,37,51,67,80,81,83,88,89,92,104,112,114,117,130,136,137,138,139,141,142,145,146,147,149,173,177,182,183,184,185,],[7,19,38,-5,-6,-7,48,7,7,7,-2,-3,-75,-76,-78,-79,-80,-81,-4,7,7,-77,111,-61,7,7,7,7,7,-15,-90,-70,-58,7,7,7,7,7,-85,-83,-54,111,-55,111,-84,-59,-82,-56,-57,-60,]),'DEF':([0,15,16,17,19,20,21,23,24,25,26,27,28,29,30,31,36,37,51,80,81,83,88,89,92,104,112,114,117,130,136,137,138,139,141,142,145,147,173,177,182,183,184,185,],[8,-5,-6,-7,8,8,8,-2,-3,-75,-76,-78,-79,-80,-81,-4,8,8,-77,-61,8,8,8,8,8,-15,-90,-70,-58,8,8,8,8,8,-85,-83,-54,-55,-84,-59,-82,-56,-57,-60,]),'IF':([0,15,16,17,19,20,21,23,24,25,26,27,28,29,30,31,36,37,51,80,81,83,88,89,92,104,112,114,117,130,136,137,138,139,141,142,145,147,173,177,182,183,184,185,],[9,-5,-6,-7,9,9,9,-2,-3,-75,-76,-78,-79,-80,-81,-4,9,9,-77,-61,9,9,9,9,9,-15,-90,-70,-58,9,9,9,9,9,-85,-83,-54,-55,-84,-59,-82,-56,-57,-60,]),'UNLESS':([0,15,16,17,19,20,21,23,24,25,26,27,28,29,30,31,36,37,51,80,81,83,88,89,92,104,112,114,117,130,136,137,138,139,141,142,145,147,173,177,182,183,184,185,],[10,-5,-6,-7,10,10,10,-2,-3,-75,-76,-78,-79,-80,-81,-4,10,10,-77,-61,10,10,10,10,10,-15,-90,-70,-58,10,10,10,10,10,-85,-83,-54,-55,-84,-59,-82,-56,-57,-60,]),'CASE':([0,15,16,17,19,20,21,23,24,25,26,27,28,29,30,31,36,37,51,80,81,83,88,89,92,104,112,114,117,130,136,137,138,139,141,142,145,147,173,177,182,183,184,185,],[11,-5,-6,-7,11,11,11,-2,-3,-75,-76,-78,-79,-80,-81,-4,11,11,-77,-61,11,11,11,11,11,-15,-90,-70,-58,11,11,11,11,11,-85,-83,-54,-55,-84,-59,-82,-56,-57,-60,]),'WHILE':([0,15,16,17,19,20,21,23,24,25,26,27,28,29,30,31,36,37,51,80,81,83,88,89,92,104,112,114,117,130,136,137,138,139,141,142,145,147,173,177,182,183,184,185,],[12,-5,-6,-7,12,12,12,-2,-3,-75,-76,-78,-79,-80,-81,-4,12,12,-77,-61,12,12,12,12,12,-15,-90,-70,-58,12,12,12,12,12,-85,-83,-54,-55,-84,-59,-82,-56,-57,-60,]),'INT':([0,9,10,12,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,34,36,37,41,42,43,44,45,46,47,51,52,56,57,58,59,60,61,62,67,80,81,83,87,88,89,92,95,100,101,104,106,112,114,115,116,117,130,132,136,137,138,139,141,142,143,145,147,148,165,173,177,180,182,183,184,185,],[14,31,31,31,-5,-6,-7,31,14,14,14,-2,-3,-75,-76,-78,-79,-80,-81,-4,65,31,14,14,14,-8,-9,-10,-11,-12,-13,-77,31,31,-16,-17,-18,-19,-20,-21,31,-61,14,14,31,14,14,14,31,31,31,-15,142,-90,-70,31,31,-58,14,31,14,14,14,14,-85,-83,172,-54,-55,31,31,-84,-59,31,-82,-56,-57,-60,]),'FLOAT':([0,9,10,12,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,34,36,37,41,42,43,44,45,46,47,51,52,56,57,58,59,60,61,62,67,80,81,83,87,88,89,92,95,100,101,104,112,114,115,116,117,130,132,136,137,138,139,141,142,145,147,148,165,173,177,180,182,183,184,185,],[15,15,15,15,-5,-6,-7,15,15,15,15,-2,-3,-75,-76,-78,-79,-80,-81,-4,15,15,15,15,-8,-9,-10,-11,-12,-13,-77,15,15,-16,-17,-18,-19,-20,-21,15,-61,15,15,15,15,15,15,15,15,15,-15,-90,-70,15,15,-58,15,15,15,15,15,15,-85,-83,-54,-55,15,15,-84,-59,15,-82,-56,-57,-60,]),'RAT':([0,9,10,12,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,34,36,37,41,42,43,44,45,46,47,51,52,56,57,58,59,60,61,62,67,80,81,83,87,88,89,92,95,100,101,104,112,114,115,116,117,130,132,136,137,138,139,141,142,145,147,148,165,173,177,180,182,183,184,185,],[16,16,16,16,-5,-6,-7,16,16,16,16,-2,-3,-75,-76,-78,-79,-80,-81,-4,16,16,16,16,-8,-9,-10,-11,-12,-13,-77,16,16,-16,-17,-18,-19,-20,-21,16,-61,16,16,16,16,16,16,16,16,16,-15,-90,-70,16,16,-58,16,16,16,16,16,16,-85,-83,-54,-55,16,16,-84,-59,16,-82,-56,-57,-60,]),'COMPX':([0,9,10,12,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,34,36,37,41,42,43,44,45,46,47,51,52,56,57,58,59,60,61,62,67,80,81,83,87,88,89,92,95,100,101,104,112,114,115,116,117,130,132,136,137,138,139,141,142,145,147,148,165,173,177,180,182,183,184,185,],[17,17,17,17,-5,-6,-7,17,17,17,17,-2,-3,-75,-76,-78,-79,-80,-81,-4,17,17,17,17,-8,-9,-10,-11,-12,-13,-77,17,17,-16,-17,-18,-19,-20,-21,17,-61,17,17,17,17,17,17,17,17,17,-15,-90,-70,17,17,-58,17,17,17,17,17,17,-85,-83,-54,-55,17,17,-84,-59,17,-82,-56,-57,-60,]),'$end':([1,2,3,4,5,6,14,15,16,17,23,24,25,26,27,28,29,30,31,48,49,50,51,80,90,94,96,102,112,114,117,123,134,140,141,142,145,147,155,156,157,158,159,161,162,164,167,173,177,179,182,183,184,185,187,188,],[0,-1,-86,-87,-88,-89,-4,-5,-6,-7,-2,-3,-75,-76,-78,-79,-80,-81,-4,-23,-22,-24,-77,-61,-14,-27,-37,-38,-90,-70,-58,-51,-39,-40,-85,-83,-54,-55,-41,-43,-42,-44,-50,-71,-72,-26,-30,-84,-59,-25,-82,-56,-57,-60,-29,-28,]),'END':([3,4,5,6,14,15,16,17,23,24,25,26,27,28,29,30,31,48,49,50,51,53,54,55,80,85,86,90,93,94,96,97,98,102,103,104,112,114,117,118,119,120,121,122,123,124,125,126,127,128,129,131,133,134,135,140,141,142,145,147,155,156,157,158,159,160,161,162,163,164,166,167,168,169,173,177,179,181,182,183,184,185,186,187,188,],[-86,-87,-88,-89,-4,-5,-6,-7,-2,-3,-75,-76,-78,-79,-80,-81,-4,-23,-22,-24,-77,94,96,102,-61,123,-48,-14,-73,-27,-37,134,-35,-38,140,-15,-90,-70,-58,155,156,157,158,159,-51,-49,-45,-47,-73,161,162,164,167,-39,-36,-40,-85,-83,-54,-55,-41,-43,-42,-44,-50,-46,-71,-72,179,-26,-74,-30,-31,-32,-84,-59,-25,187,-82,-56,-57,-60,188,-29,-28,]),'RETURN':([3,4,5,6,14,15,16,17,23,24,25,26,27,28,29,30,31,48,49,50,51,53,80,90,94,96,102,112,114,117,123,131,134,140,141,142,145,147,155,156,157,158,159,161,162,163,164,167,173,177,179,182,183,184,185,187,188,],[-86,-87,-88,-89,-4,-5,-6,-7,-2,-3,-75,-76,-78,-79,-80,-81,-4,-23,-22,-24,-77,95,-61,-14,-27,-37,-38,-90,-70,-58,-51,165,-39,-40,-85,-83,-54,-55,-41,-43,-42,-44,-50,-71,-72,180,-26,-30,-84,-59,-25,-82,-56,-57,-60,-29,-28,]),'ELSE':([3,4,5,6,14,15,16,17,23,24,25,26,27,28,29,30,31,48,49,50,51,54,55,80,82,84,85,86,90,93,94,96,99,102,104,112,114,117,123,124,125,126,127,134,140,141,142,145,147,155,156,157,158,159,160,161,162,164,166,167,170,171,173,177,179,182,183,184,185,187,188,],[-86,-87,-88,-89,-4,-5,-6,-7,-2,-3,-75,-76,-78,-79,-80,-81,-4,-23,-22,-24,-77,100,100,-61,100,100,100,-48,-14,-73,-27,-37,100,-38,-15,-90,-70,-58,-51,-49,-45,-47,-73,-39,-40,-85,-83,-54,-55,-41,-43,-42,-44,-50,-46,-71,-72,-26,-74,-30,-33,-34,-84,-59,-25,-82,-56,-57,-60,-29,-28,]),'ELSIF':([3,4,5,6,14,15,16,17,23,24,25,26,27,28,29,30,31,48,49,50,51,54,55,80,82,84,90,94,96,99,102,112,114,117,123,134,140,141,142,145,147,155,156,157,158,159,161,162,164,167,170,171,173,177,179,182,183,184,185,187,188,],[-86,-87,-88,-89,-4,-5,-6,-7,-2,-3,-75,-76,-78,-79,-80,-81,-4,-23,-22,-24,-77,101,101,-61,101,101,-14,-27,-37,101,-38,-90,-70,-58,-51,-39,-40,-85,-83,-54,-55,-41,-43,-42,-44,-50,-71,-72,-26,-30,-33,-34,-84,-59,-25,-82,-56,-57,-60,-29,-28,]),'EQUALS':([7,],[18,]),'TRUE':([9,10,12,18,34,52,56,57,58,59,60,61,62,67,87,95,100,101,115,116,132,148,165,180,],[23,23,23,23,23,23,23,-16,-17,-18,-19,-20,-21,23,23,23,23,23,23,23,23,23,23,23,]),'FALSE':([9,10,12,18,34,52,56,57,58,59,60,61,62,67,87,95,100,101,115,116,132,148,165,180,],[24,24,24,24,24,24,24,-16,-17,-18,-19,-20,-21,24,24,24,24,24,24,24,24,24,24,24,]),'STRING':([9,10,12,18,32,34,52,56,57,58,59,60,61,62,67,87,95,100,101,105,115,116,132,144,148,165,180,],[25,25,25,25,66,74,25,25,-16,-17,-18,-19,-20,-21,25,25,25,25,25,141,74,25,25,173,25,25,25,]),'LPAREN':([9,10,12,18,19,34,52,56,57,58,59,60,61,62,67,87,95,100,101,115,116,117,132,148,165,180,],[32,32,32,32,52,32,32,32,-16,-17,-18,-19,-20,-21,32,32,32,32,32,32,32,154,32,32,32,32,]),'LBRAKET':([9,10,12,18,33,34,35,52,56,57,58,59,60,61,62,67,87,95,100,101,113,115,116,132,148,154,165,180,],[33,33,33,33,67,33,67,33,33,-16,-17,-18,-19,-20,-21,33,33,33,33,33,67,33,33,33,33,67,33,33,]),'LBRACE':([9,10,12,18,52,56,57,58,59,60,61,62,67,87,95,100,101,116,132,148,165,180,],[34,34,34,34,34,34,-16,-17,-18,-19,-20,-21,34,34,34,34,34,34,34,34,34,34,]),'SET':([9,10,12,18,52,56,57,58,59,60,61,62,67,87,95,100,101,116,132,148,165,180,],[35,35,35,35,35,35,-16,-17,-18,-19,-20,-21,35,35,35,35,35,35,35,35,35,35,]),'PLUS':([13,14,15,16,17,],[42,-4,-5,-6,-7,]),'MINUS':([13,14,15,16,17,],[43,-4,-5,-6,-7,]),'TIMES':([13,14,15,16,17,],[44,-4,-5,-6,-7,]),'DIVIDE':([13,14,15,16,17,],[45,-4,-5,-6,-7,]),'MODULE':([13,14,15,16,17,],[46,-4,-5,-6,-7,]),'EXPON':([13,14,15,16,17,],[47,-4,-5,-6,-7,]),'EQCOMP':([15,16,17,21,22,23,24,25,26,27,28,29,30,31,37,40,51,80,112,114,117,127,137,139,141,142,145,147,173,177,182,183,184,185,],[-5,-6,-7,-77,57,-2,-3,-75,-76,-78,-79,-80,-81,-4,-77,-77,-77,-61,-90,-70,-58,57,-77,-77,-85,-83,-54,-55,-84,-59,-82,-56,-57,-60,]),'LESSTH':([15,16,17,21,22,23,24,25,26,27,28,29,30,31,37,40,51,80,112,114,117,127,137,139,141,142,145,147,173,177,182,183,184,185,],[-5,-6,-7,-77,58,-2,-3,-75,-76,-78,-79,-80,-81,-4,-77,-77,-77,-61,-90,-70,-58,58,-77,-77,-85,-83,-54,-55,-84,-59,-82,-56,-57,-60,]),'LESSEQTH':([15,16,17,21,22,23,24,25,26,27,28,29,30,31,37,40,51,80,112,114,117,127,137,139,141,142,145,147,173,177,182,183,184,185,],[-5,-6,-7,-77,59,-2,-3,-75,-76,-78,-79,-80,-81,-4,-77,-77,-77,-61,-90,-70,-58,59,-77,-77,-85,-83,-54,-55,-84,-59,-82,-56,-57,-60,]),'GREATH':([15,16,17,21,22,23,24,25,26,27,28,29,30,31,37,40,51,80,112,114,117,127,137,139,141,142,145,147,173,177,182,183,184,185,],[-5,-6,-7,-77,60,-2,-3,-75,-76,-78,-79,-80,-81,-4,-77,-77,-77,-61,-90,-70,-58,60,-77,-77,-85,-83,-54,-55,-84,-59,-82,-56,-57,-60,]),'GREATEQTH':([15,16,17,21,22,23,24,25,26,27,28,29,30,31,37,40,51,80,112,114,117,127,137,139,141,142,145,147,173,177,182,183,184,185,],[-5,-6,-7,-77,61,-2,-3,-75,-76,-78,-79,-80,-81,-4,-77,-77,-77,-61,-90,-70,-58,61,-77,-77,-85,-83,-54,-55,-84,-59,-82,-56,-57,-60,]),'NOTEQ':([15,16,17,21,22,23,24,25,26,27,28,29,30,31,37,40,51,80,112,114,117,127,137,139,141,142,145,147,173,177,182,183,184,185,],[-5,-6,-7,-77,62,-2,-3,-75,-76,-78,-79,-80,-81,-4,-77,-77,-77,-61,-90,-70,-58,62,-77,-77,-85,-83,-54,-55,-84,-59,-82,-56,-57,-60,]),'ROCKET':([15,16,17,23,24,31,73,74,75,76,77,78,112,141,142,173,182,],[-5,-6,-7,-2,-3,-4,116,-62,-63,-64,-65,-66,-90,-85,-83,-84,-82,]),'COMMA':([15,16,17,23,24,25,26,27,28,29,30,31,51,69,70,72,80,93,109,110,111,112,114,117,127,141,142,145,147,151,153,166,173,176,177,182,183,184,185,],[-5,-6,-7,-2,-3,-75,-76,-78,-79,-80,-81,-4,-77,113,-93,115,-61,132,146,148,149,-90,-70,-58,132,-85,-83,-54,-55,115,-67,-74,-84,-53,-59,-82,-56,-57,-60,]),'RPAREN':([15,16,17,23,24,25,26,27,28,29,30,31,51,52,80,91,93,112,114,117,141,142,145,147,154,166,172,173,177,178,182,183,184,185,],[-5,-6,-7,-2,-3,-75,-76,-78,-79,-80,-81,-4,-77,92,-61,130,-73,-90,-70,-58,-85,-83,-54,-55,177,-74,182,-84,-59,185,-82,-56,-57,-60,]),'COLON':([15,16,17,23,24,25,26,27,28,29,30,31,36,37,51,80,104,112,114,117,141,142,145,147,173,177,182,183,184,185,],[-5,-6,-7,-2,-3,-75,-76,-78,-79,-80,-81,-4,81,83,-77,-61,-15,-90,-70,-58,-85,-83,-54,-55,-84,-59,-82,-56,-57,-60,]),'DO':([15,16,17,23,24,25,26,27,28,29,30,31,39,40,51,80,104,112,114,117,141,142,145,147,173,177,182,183,184,185,],[-5,-6,-7,-2,-3,-75,-76,-78,-79,-80,-81,-4,88,89,-77,-61,-15,-90,-70,-58,-85,-83,-54,-55,-84,-59,-82,-56,-57,-60,]),'WHEN':([15,16,17,23,24,25,26,27,28,29,30,31,38,51,80,86,93,104,112,114,117,125,126,127,141,142,145,147,160,166,173,177,182,183,184,185,],[-5,-6,-7,-2,-3,-75,-76,-78,-79,-80,-81,-4,87,-77,-61,87,-73,-15,-90,-70,-58,-45,-47,-73,-85,-83,-54,-55,-46,-74,-84,-59,-82,-56,-57,-60,]),'RBRAKET':([15,16,17,23,24,25,26,27,28,29,30,31,51,68,69,70,80,93,109,110,111,112,114,117,141,142,145,147,150,166,173,174,175,176,177,182,183,184,185,],[-5,-6,-7,-2,-3,-75,-76,-78,-79,-80,-81,-4,-77,112,-91,-93,-61,-73,145,147,-52,-90,-70,-58,-85,-83,-54,-55,-92,-74,-84,183,184,-53,-59,-82,-56,-57,-60,]),'THEN':([15,16,17,23,24,25,26,27,28,29,30,31,51,80,93,112,114,117,125,127,141,142,145,147,166,173,177,182,183,184,185,],[-5,-6,-7,-2,-3,-75,-76,-78,-79,-80,-81,-4,-77,-61,-73,-90,-70,-58,160,-73,-85,-83,-54,-55,-74,-84,-59,-82,-56,-57,-60,]),'RBRACE':([15,16,17,23,24,25,26,27,28,29,30,31,51,71,80,112,114,117,141,142,145,147,151,152,153,173,177,182,183,184,185,],[-5,-6,-7,-2,-3,-75,-76,-78,-79,-80,-81,-4,-77,114,-61,-90,-70,-58,-85,-83,-54,-55,-68,-69,-67,-84,-59,-82,-56,-57,-60,]),'NIL':([18,],[50,]),'DOT':([25,31,35,63,64,65,66,74,107,108,],[63,64,79,105,106,107,108,63,143,144,]),'NEW':([79,],[117,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'cmmd':([0,19,20,21,36,37,81,83,88,89,92,130,136,137,138,139,],[2,53,54,55,82,84,118,120,128,129,131,163,168,169,170,171,]),'var':([0,19,20,21,36,37,81,83,88,89,92,130,136,137,138,139,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'func':([0,19,20,21,36,37,81,83,88,89,92,130,136,137,138,139,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'control':([0,19,20,21,36,37,81,83,88,89,92,130,136,137,138,139,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'optn':([0,19,20,21,36,37,81,83,88,89,92,130,136,137,138,139,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'num':([0,9,10,12,18,19,20,21,34,36,37,41,52,56,67,81,83,87,88,89,92,95,100,101,115,116,130,132,136,137,138,139,148,165,180,],[13,26,26,26,26,13,13,13,75,13,13,90,26,26,26,13,13,26,13,13,13,26,26,26,75,26,13,26,13,13,13,13,26,26,26,]),'comptn':([9,10,12,87,100,101,],[20,36,39,126,136,138,]),'bool':([9,10,12,18,34,52,56,67,87,95,100,101,115,116,132,148,165,180,],[21,37,40,51,76,51,51,51,51,51,137,139,76,51,51,51,51,51,]),'obj':([9,10,12,18,52,56,67,87,95,100,101,116,132,148,165,180,],[22,22,22,49,93,104,93,127,133,22,22,153,93,93,181,186,]),'range':([9,10,12,18,34,52,56,67,87,95,100,101,115,116,132,148,165,180,],[27,27,27,27,77,27,27,27,27,27,27,27,77,27,27,27,27,27,]),'matrix':([9,10,12,18,34,52,56,67,87,95,100,101,115,116,132,148,165,180,],[28,28,28,28,78,28,28,28,28,28,28,28,78,28,28,28,28,28,]),'hash':([9,10,12,18,52,56,67,87,95,100,101,116,132,148,165,180,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'strucSet':([9,10,12,18,52,56,67,87,95,100,101,116,132,148,165,180,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'optr':([13,],[41,]),'comptr':([22,127,],[56,56,]),'rows':([33,113,],[68,150,]),'row':([33,113,],[69,69,]),'array':([33,35,113,154,],[70,80,70,178,]),'elementsHash':([34,115,],[71,152,]),'elementHash':([34,115,],[72,151,]),'claveHash':([34,115,],[73,73,]),'whens':([38,86,],[85,124,]),'when':([38,86,],[86,86,]),'objs':([52,67,87,132,148,],[91,109,125,166,175,]),'elses':([54,55,82,84,99,],[97,103,119,121,135,]),'else':([54,55,82,84,85,99,],[98,98,98,98,122,98,]),'elsif':([54,55,82,84,99,],[99,99,99,99,99,]),'ids':([67,146,149,],[110,174,176,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> cmmd','init',1,'p_init','semtic.py',16),
  ('bool -> TRUE','bool',1,'p_bool','semtic.py',20),
  ('bool -> FALSE','bool',1,'p_bool','semtic.py',21),
  ('num -> INT','num',1,'p_num','semtic.py',26),
  ('num -> FLOAT','num',1,'p_num','semtic.py',27),
  ('num -> RAT','num',1,'p_num','semtic.py',28),
  ('num -> COMPX','num',1,'p_num','semtic.py',29),
  ('optr -> PLUS','optr',1,'p_optr','semtic.py',34),
  ('optr -> MINUS','optr',1,'p_optr','semtic.py',35),
  ('optr -> TIMES','optr',1,'p_optr','semtic.py',36),
  ('optr -> DIVIDE','optr',1,'p_optr','semtic.py',37),
  ('optr -> MODULE','optr',1,'p_optr','semtic.py',38),
  ('optr -> EXPON','optr',1,'p_optr','semtic.py',39),
  ('optn -> num optr num','optn',3,'p_optn','semtic.py',44),
  ('comptn -> obj comptr obj','comptn',3,'p_comptn','semtic.py',48),
  ('comptr -> EQCOMP','comptr',1,'p_comptr','semtic.py',52),
  ('comptr -> LESSTH','comptr',1,'p_comptr','semtic.py',53),
  ('comptr -> LESSEQTH','comptr',1,'p_comptr','semtic.py',54),
  ('comptr -> GREATH','comptr',1,'p_comptr','semtic.py',55),
  ('comptr -> GREATEQTH','comptr',1,'p_comptr','semtic.py',56),
  ('comptr -> NOTEQ','comptr',1,'p_comptr','semtic.py',57),
  ('var -> ID EQUALS obj','var',3,'p_var','semtic.py',62),
  ('var -> ID EQUALS ID','var',3,'p_var','semtic.py',63),
  ('var -> ID EQUALS NIL','var',3,'p_var','semtic.py',64),
  ('func -> DEF ID LPAREN objs RPAREN cmmd END','func',7,'p_func','semtic.py',70),
  ('func -> DEF ID LPAREN RPAREN cmmd END','func',6,'p_func','semtic.py',71),
  ('func -> DEF ID cmmd END','func',4,'p_func','semtic.py',72),
  ('func -> DEF ID LPAREN objs RPAREN cmmd RETURN obj END','func',9,'p_func','semtic.py',73),
  ('func -> DEF ID LPAREN RPAREN cmmd RETURN obj END','func',8,'p_func','semtic.py',74),
  ('func -> DEF ID cmmd RETURN obj END','func',6,'p_func','semtic.py',75),
  ('else -> ELSE comptn cmmd','else',3,'p_else','semtic.py',80),
  ('else -> ELSE bool cmmd','else',3,'p_else','semtic.py',81),
  ('elsif -> ELSIF comptn cmmd','elsif',3,'p_elsif','semtic.py',86),
  ('elsif -> ELSIF bool cmmd','elsif',3,'p_elsif','semtic.py',87),
  ('elses -> else','elses',1,'p_elses','semtic.py',92),
  ('elses -> elsif elses','elses',2,'p_elses','semtic.py',93),
  ('control -> IF comptn cmmd END','control',4,'p_contol_if','semtic.py',98),
  ('control -> IF bool cmmd END','control',4,'p_contol_if','semtic.py',99),
  ('control -> IF comptn cmmd elses END','control',5,'p_contol_if','semtic.py',100),
  ('control -> IF bool cmmd elses END','control',5,'p_contol_if','semtic.py',101),
  ('control -> UNLESS comptn COLON cmmd END','control',5,'p_control_unless','semtic.py',106),
  ('control -> UNLESS bool COLON cmmd END','control',5,'p_control_unless','semtic.py',107),
  ('control -> UNLESS comptn cmmd elses END','control',5,'p_control_unless','semtic.py',108),
  ('control -> UNLESS bool cmmd elses END','control',5,'p_control_unless','semtic.py',109),
  ('when -> WHEN objs','when',2,'p_when','semtic.py',114),
  ('when -> WHEN objs THEN','when',3,'p_when','semtic.py',115),
  ('when -> WHEN comptn','when',2,'p_when','semtic.py',116),
  ('whens -> when','whens',1,'p_whens','semtic.py',121),
  ('whens -> when whens','whens',2,'p_whens','semtic.py',122),
  ('control -> CASE ID whens else END','control',5,'p_control_case','semtic.py',127),
  ('control -> CASE ID whens END','control',4,'p_control_case','semtic.py',128),
  ('ids -> ID','ids',1,'p_ids','semtic.py',133),
  ('ids -> ID COMMA ids','ids',3,'p_ids','semtic.py',134),
  ('array -> LBRAKET objs RBRAKET','array',3,'p_array','semtic.py',138),
  ('array -> LBRAKET ids RBRAKET','array',3,'p_array','semtic.py',139),
  ('array -> LBRAKET objs COMMA ids RBRAKET','array',5,'p_array','semtic.py',140),
  ('array -> LBRAKET ids COMMA objs RBRAKET','array',5,'p_array','semtic.py',141),
  ('strucSet -> SET DOT NEW','strucSet',3,'p_strucSet','semtic.py',146),
  ('strucSet -> SET DOT NEW LPAREN RPAREN','strucSet',5,'p_strucSet','semtic.py',147),
  ('strucSet -> SET DOT NEW LPAREN array RPAREN','strucSet',6,'p_strucSet','semtic.py',148),
  ('strucSet -> SET array','strucSet',2,'p_strucSet','semtic.py',149),
  ('claveHash -> STRING','claveHash',1,'p_claveHash','semtic.py',154),
  ('claveHash -> num','claveHash',1,'p_claveHash','semtic.py',155),
  ('claveHash -> bool','claveHash',1,'p_claveHash','semtic.py',156),
  ('claveHash -> range','claveHash',1,'p_claveHash','semtic.py',157),
  ('claveHash -> matrix','claveHash',1,'p_claveHash','semtic.py',158),
  ('elementHash -> claveHash ROCKET obj','elementHash',3,'p_elementHash','semtic.py',163),
  ('elementsHash -> elementHash COMMA elementHash','elementsHash',3,'p_elementsHash','semtic.py',167),
  ('elementsHash -> elementHash COMMA elementsHash','elementsHash',3,'p_elementsHash','semtic.py',168),
  ('hash -> LBRACE elementsHash RBRACE','hash',3,'p_hash','semtic.py',171),
  ('control -> WHILE comptn DO cmmd END','control',5,'p_control_while','semtic.py',175),
  ('control -> WHILE bool DO cmmd END','control',5,'p_control_while','semtic.py',176),
  ('objs -> obj','objs',1,'p_objs','semtic.py',180),
  ('objs -> obj COMMA objs','objs',3,'p_objs','semtic.py',181),
  ('obj -> STRING','obj',1,'p_obj','semtic.py',186),
  ('obj -> num','obj',1,'p_obj','semtic.py',187),
  ('obj -> bool','obj',1,'p_obj','semtic.py',188),
  ('obj -> range','obj',1,'p_obj','semtic.py',189),
  ('obj -> matrix','obj',1,'p_obj','semtic.py',190),
  ('obj -> hash','obj',1,'p_obj','semtic.py',191),
  ('obj -> strucSet','obj',1,'p_obj','semtic.py',192),
  ('range -> LPAREN INT DOT DOT INT RPAREN','range',6,'p_range','semtic.py',197),
  ('range -> INT DOT DOT INT','range',4,'p_range','semtic.py',198),
  ('range -> LPAREN STRING DOT DOT STRING','range',5,'p_range','semtic.py',199),
  ('range -> STRING DOT DOT STRING','range',4,'p_range','semtic.py',200),
  ('cmmd -> var','cmmd',1,'p_cmmd','semtic.py',205),
  ('cmmd -> func','cmmd',1,'p_cmmd','semtic.py',206),
  ('cmmd -> control','cmmd',1,'p_cmmd','semtic.py',207),
  ('cmmd -> optn','cmmd',1,'p_cmmd','semtic.py',208),
  ('matrix -> LBRAKET rows RBRAKET','matrix',3,'p_matrix','semtic.py',212),
  ('rows -> row','rows',1,'p_rows','semtic.py',215),
  ('rows -> row COMMA rows','rows',3,'p_rows','semtic.py',216),
  ('row -> array','row',1,'p_row','semtic.py',219),
]
