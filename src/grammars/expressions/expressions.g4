grammar expressions;

prog:   stat+ ;

stat:   expr END_INSTR                     // Semi-colon separated statements
    ;

expr:   LBRACKET expr RBRACKET             // Parentheses
    |   unary_op=(ADD|SUB|NOT) expr        // Unary integer operator
//    |   unary_op=(NOT) expr           // Unary boolean operator
    |   expr binary_op=(MUL|DIV|MOD) expr  // Binary multiplicative operator
    |   expr binary_op=(ADD|SUB) expr      // Binary additive operator
    |   expr binary_op=(LT|GT|LTE|GTE)     // Binary relational operator
    |   expr binary_op=(EQ|NEQ)            // Binary equality operator
    |   expr binary_op=(AND|OR)            // Binary logical operator
    |   INT                         // Integer
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