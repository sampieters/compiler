grammar C;

prog: INCLUDE_IO? (stat | scope)+                 # Program
    ;

stat: definition END_INSTR              # DefinitionStatement
    | declaration END_INSTR             # DeclarationStatement
    | assignment END_INSTR              # AssignmentStatement
    | expr END_INSTR                    # ExpressionStatement       // Semi-colon separated statements
    | BREAK END_INSTR                   # BreakStatement
    | CONTINUE END_INSTR                # ContinueStatement
    | for_stat                          # ForStatement
    | while_stat                        # WhileStatement
    | if_stat                           # IfStatement
    | switch_stat                       # SwitchStatement
    | function_declaration END_INSTR    # FunctionDeclarationStatement
    | function_definition               # FunctionDefinitionStatement
    | RETURN expr? END_INSTR            # ReturnStatement
    | END_INSTR                         # EmptyStatement
    ;

expr: LBRACKET expr RBRACKET            # Brackets  // Parentheses
    | (MUL|REF) identifier              # UnaryOpPointer  // Unary pointer operation
    | (INCR|DECR) identifier            # UnaryOpIdentifierPrefix // Unary identifier operation (prefix)
    | identifier (INCR|DECR)            # UnaryOpIdentifierSuffix // Unary identifier operation (suffix)
    | (ADD|SUB) expr                    # UnaryOp   // Unary integer operation
    | (NOT) expr                        # UnaryOpBoolean   // Unary boolean operation
    | expr (MUL|DIV|MOD) expr           # BinaryOp  // Binary multiplicative operation
    | expr (ADD|SUB) expr               # BinaryOp  // Binary additive operation
    | expr (LT|GT|LTE|GTE) expr         # BinaryOpBoolean  // Binary relational operation
    | expr (DEQ|NEQ) expr               # BinaryOpBoolean  // Binary equality operation
    | expr (AND|OR) expr                # BinaryOpBoolean  // Binary logical operation
    | literal                           # LiteralExpr
    | identifier                        # IdentifierExpr
    | function_call                     # FunctionCall
    ;

identifier: ID                          # Identifier
          | ID (LSQUARE expr RSQUARE)+  # ArrayElement
          ;

scope: LCURLY stat* RCURLY
     ;

for_stat: FOR LBRACKET (definition | assignment) END_INSTR expr END_INSTR (expr | assignment) RBRACKET scope
        ;

while_stat: WHILE LBRACKET expr RBRACKET scope
          ;

if_stat: IF LBRACKET expr RBRACKET scope elif_stat* else_stat?
       ;

elif_stat: ELIF LBRACKET expr RBRACKET scope
         ;

else_stat: ELSE scope
         ;

switch_stat: SWITCH LBRACKET expr RBRACKET LCURLY (CASE COLON stat)* (DEFAULT COLON stat)? (CASE COLON stat)* RCURLY
           ;

type_specifier: CONST? (SIGNED|UNSIGNED)? (SHORT_PREF|INT_PREF|LONG_PREF|LONG_LONG_PREF|CHAR_PREF) MUL*
              | CONST? (FLOAT_PREF|DOUBLE_PREF|LONG_DOUBLE_PREF) MUL*
              | VOID_PREF
              ;

literal: FLOAT   # Float
       | INT     # Integer
       | STRING  # String
       | CHAR    # Character
       ;

declaration: type_specifier ID (LSQUARE expr? RSQUARE)*
           ;

function_declaration: type_specifier ID arg_list # FunctionDeclaration
                    ;

definition: declaration EQ expr
          ;

function_definition: function_declaration scope
                   ; 

assignment: identifier EQ expr
          ;

function_call: ID call_list         # CustomFunctionCall
             | PRINTF call_list     # PrintfFunctionCall
             | SCANF call_list      # ScanfFunctionCall
             ;

arg_list: LBRACKET ((declaration COMMA)* declaration)? RBRACKET
        ;

call_list: LBRACKET ((expr COMMA)* expr)? RBRACKET
         ;

initializer_list: LCURLY ((expr COMMA)* expr)? RCURLY   # InitializerList
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
LSQUARE :       '[' ;
RSQUARE :       ']' ;
LCURLY :        '{' ;
RCURLY :        '}' ;
END_INSTR :     ';' ;
COLON :       ':' ;
DOT :           '.' ;
REF :           '&' ;
SQUOTE :        '\'' ;
ESC :           '\\' ;
COMMA :         ',' ;

CONST :         'const' ;
SIGNED :        'signed' ;
UNSIGNED :      'unsigned' ;

INT_PREF : 'int' ;
VOID_PREF: 'void' ;
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
SCANF : 'scanf' ;
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
RETURN : 'return' ;
INCLUDE_IO : '#include <stdio.h>' ;

ID : [a-zA-Z_][a-zA-Z0-9_]* ;

WS  :   [ \n\t\r]+ -> skip ; // toss out whitespace

SINGLE_COMMENT : '//' .*? '\n' -> skip ; // toss out comments, for now
MULTI_COMMENT : '/*' .*? '*/' -> skip ;