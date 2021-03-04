grammar variables;

prog: stat+                             # Program
    ;

stat: definition END_INSTR              # DefinitionStatement
    | declaration END_INSTR             # DeclarationStatement
    | assignment END_INSTR              # AssignmentStatement
    | expr END_INSTR                    # ExpressionStatement       // Semi-colon separated statements
    ;

expr: LBRACKET expr RBRACKET            # Brackets  // Parentheses
    | (MUL|REF) ID                      # UnaryOpPointer  // Unary pointer operation
    | (INCR|DECR) ID                    # UnaryOpIdentifier // Unary identifier operation
    | ID (INCR|DECR)                    # UnaryOpIdentifier // Unary identifier operation
    | (ADD|SUB) expr                    # UnaryOp   // Unary integer operation
    | (NOT) expr                        # UnaryOpBoolean   // Unary boolean operation
    | expr (MUL|DIV|MOD) expr           # BinaryOp  // Binary multiplicative operation
    | expr (ADD|SUB) expr               # BinaryOp  // Binary additive operation
    | expr (LT|GT|LTE|GTE) expr         # BinaryOpBoolean  // Binary relational operation
    | expr (DEQ|NEQ) expr               # BinaryOpBoolean  // Binary equality operation
    | expr (AND|OR) expr                # BinaryOpBoolean  // Binary logical operation
    | literal                           # LiteralExpr  
    | ID                                # Identifier
    ;   

type_specifier: CONST? (SIGNED|UNSIGNED)? (SHORT_PREF|INT_PREF|LONG_PREF|LONG_LONG_PREF|CHAR_PREF) MUL?   
              | CONST? (FLOAT_PREF|DOUBLE_PREF|LONG_DOUBLE_PREF) MUL?
              ;   

literal: FLOAT   # Float 
       | INT     # Integer
       | STRING  # String
       | CHAR    # Character
       ;

declaration: type_specifier ID
           ;   

definition: declaration EQ expr
          ;

assignment: ID EQ expr
          ;

MUL :           '*' ; // assigns token name to '*' used above in grammar
DIV :           '/' ;
ADD :           '+' ;
SUB :           '-' ;
LT  :           '<' ;
GT  :           '>' ;
DEQ :           '==' ;
EQ :            '=' ;
MOD :           '%' ;
LTE :           '<=' ;
GTE :           '>=' ;
NEQ :           '!=' ;
AND :           '&&' ;
OR  :           '||' ;
NOT :           '!' ;
INCR :          '++' ;
DECR :          '--' ;
LBRACKET :      '(' ;
RBRACKET :      ')' ;
END_INSTR :     ';' ;
DOT :           '.' ;
REF :           '&' ;
SQUOTE :        '\'' ;
ESC :           '\\' ;

CONST :         'const' ;
SIGNED :        'signed' ;
UNSIGNED :      'unsigned' ;

INT_PREF : 'int' ;
SHORT_PREF : 'short' | 'short int' ;
LONG_PREF : 'long' | 'long int' ;
LONG_LONG_PREF: 'long long' | 'long long int' ;        
INT : [1-9][0-9]* | '0' ;         

FLOAT_PREF : 'float' ;
DOUBLE_PREF : 'double' ;
LONG_DOUBLE_PREF : 'long double' ;
FLOAT : INT? DOT [0-9]+ ;

CHAR_PREF : 'char' ;
CHAR : SQUOTE ESC? [!-~] SQUOTE ;
STRING : '"'CHAR*'"' ;
      
ID : [a-zA-Z_][a-zA-Z0-9_]* ;

WS  :   [ \n\t\r]+ -> skip ; // toss out whitespace