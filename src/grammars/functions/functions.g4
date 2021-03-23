grammar functions;

prog: stat+                             # Program
    ;

stat: definition END_INSTR              # DefinitionStatement
    | declaration END_INSTR             # DeclarationStatement
    | assignment END_INSTR              # AssignmentStatement
    | expr END_INSTR                    # ExpressionStatement       // Semi-colon separated statements
    ;

expr: LBRACKET expr RBRACKET            # Brackets  // Parentheses
    | (MUL|REF) ID                      # UnaryOpPointer  // Unary pointer operation
    | (INCR|DECR) ID                    # UnaryOpIdentifierPrefix // Unary identifier operation (prefix)
    | ID (INCR|DECR)                    # UnaryOpIdentifierSuffix // Unary identifier operation (suffix)
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

loop_stat: stat
         | BREAK END_INSTR
         | CONTINUE END_INSTR
         ;

block_stat: FOR LBRACKET (definition | assignment) END_INSTR expr END_INSTR expr RBRACKET LCURLY loop_stat* RCURLY
          | WHILE LBRACKET expr RBRACKET LCURLY loop_stat* RCURLY
          | IF LBRACKET expr RBRACKET LCURLY loop_stat* RCURLY (ELIF LBRACKET expr RBRACKET LCURLY loop_stat* RCURLY)* (ELSE loop_stat*)?
          | SWITCH LBRACKET expr RBRACKET LCURLY (CASE D_POINT stat)* (DEFAULT D_POINT stat)? (CASE D_POINT stat)* RCURLY
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

function_call: PRINTF LBRACKET expr RBRACKET     # PrintF
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
LCURLY :        '{' ;
RCURLY :        '}' ;
END_INSTR :     ';' ;
D_POINT :       ':' ;
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

PRINTF : 'printf' ;
IF : 'if' ;
ELIF : 'else if' ;
ELSE : 'else' ;
FOR : 'for' ;
WHILE : 'while' ;
BREAK : 'break' ;
CONTINUE : 'continue' ;
SWITCH : 'switch' ;
CASE : 'case' ;
DEFAULT : 'default' ;

ID : [a-zA-Z_][a-zA-Z0-9_]* ;

WS  :   [ \n\t\r]+ -> skip ; // toss out whitespace

SINGLE_COMMENT : '//' .*? '\n' -> skip ; // toss out comments, for now
MULTI_COMMENT : '/*' .*? '*/' -> skip ;