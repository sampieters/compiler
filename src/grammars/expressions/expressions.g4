grammar expressions;

prog:   stat+                                # Program
    ;

stat:   expr END_INSTR                       # Expression       // Semi-colon separated statements
    ;

expr:   LBRACKET expr RBRACKET            # Brackets  // Parentheses
    |   (ADD|SUB) expr                    # UnaryOp   // Unary integer operator
    |   (NOT) expr                        # UnaryOpBoolean   // Unary boolean operator
    |   expr (MUL|DIV|MOD) expr           # BinaryOp  // Binary multiplicative operator
    |   expr (ADD|SUB) expr               # BinaryOp  // Binary additive operator
    |   expr (LT|GT|LTE|GTE) expr         # BinaryOpBoolean  // Binary relational operator
    |   expr (EQ|NEQ) expr                # BinaryOpBoolean  // Binary equality operator
    |   expr (AND|OR) expr                # BinaryOpBoolean  // Binary logical operator
    |   INT                               # Integer   // Integer
    ;


MUL :   '*' ; // assigns token name to '*' used above in grammar
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
LT  :   '<' ;
GT  :   '>' ;
EQ  :   '==' ;
MOD :   '%' ;
LTE :   '<=' ;
GTE :   '>=' ;
NEQ :   '!=' ;
AND :   '&&' ;
OR  :   '||' ;
NOT :   '!' ;
INCR:   '++' ;
DECR:   '--' ;
LBRACKET: '(' ;
RBRACKET: ')' ;
END_INSTR: ';' ;

// ID  :   [a-zA-Z]+ ;      // match identifiers
INT :   [1-9][0-9]* ;         // match integers
WS  :   [ \n\t\r]+ -> skip ; // toss out whitespace