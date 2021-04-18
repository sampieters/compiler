# compiler
## Inleiding
Dit is de compiler van een subset van C++ naar LLVM geschreven door Joshi Dhima en Sam Pieters.

## Hoe te gebruiken
### 1) Grammar inladen
Om de compiler te gebruiken moet eerst het java bestand voor ANTLR uitgevoerd worden om de grammar
in te laden. Dit gebeurd door de volgende command in de terminal:

<u>java -jar antlr-4.9.1-complete.jar -Dlanguage=Python2 PATH/variables.g4 -visitor</u>

Met PATH het pad van waar de grammar zich bevind t.o.v. van waar de terminal is opgestart.

### 2) Input geven
Om input mee te geven aan de grammar moet de main.py uitgevoerd worden.

<u>Python3 main.py</u>

Nu kan een input worden ingevoerd. Als de main.py is uitgevoerd zal er ook een .dot formaat gegeneerd
worden van de AST van de gegeven input. 

### 3) geïmplementeerd

geïmplementeerd van opdracht 1:

- (Mandatory) Binary operations +, -, * and / (voltooid)
- (Mandatory) Comparison operators >, <, and == (voltooid)
- (Mandatory) Unary operators + and - (voltooid)
- (Mandatory) Brackets to overwrite the order of operations (voltooid)
- (Mandatory) Binary operator % (voltooid)
- (optional) Comparison operators >=, <=, != (voltooid)
- (optional) Logical operators &&, ||, and ! (enkel ! voltooid)

- (optional) Constant folding (voltooid)

geïmplementeerd van opdracht 2:

- (Mandatory) Types (voltooid)
- (Mandatory) Reserved words (voltooid)
- (Mandatory) Variables (voltooid)
- (Mandatory) Pointer Operations (voltooid)
- (Optional) Identifier Operations (werkt deels)
- (Optional) Conversions (voltooid)

- (Optional) Constant Propagation (niet voltooid)

geïmplementeerd van opdracht 3:

- (Mandatory) Comments (voltooid)
    - (Optional) retain comments (niet voltooid)
    - (Optional) comment every instruction (niet voltooid)
- (Mandatory) Printf (voltooid)

geïmplementeerd van opdracht 4:

- (Mandatory) Reserved words
    - (Mandatory) for (voltooid)
    - (Mandatory) break (voltooid)
    - (Mandatory) continue (voltooid)
    - (Optional) switch, case and default (niet voltooid)
- (Mandatory) Scopes (voltooid)

geïmplementeerd van opdracht 5:

- (Mandatory) reserved words
    - return (voltooid)
    - void (voltooid)
- (Mandatory) Scopes (voltooid)
- (Mandatory) Local and global variables (voltooid)
- (Mandatory) Functions (voltooid)

geïmplementeerd van opdracht 6:
- (Mandatory) Arrays (voltooid)
    - (Optional) multi-dimensional arrays (niet voltooid)
    - (Optional) dynamic arrays (niet voltooid)
- (Mandatory) Import (voltooid)


### 4) Benchmarks

- binaryOperations1 (werkt)
- binaryOperations2 (werkt)
- breakAndContinue (werkt)
- comparisons1 (werkt, dankzij folding)
- comparisons2 (werkt, dankzij folding)
- dereferenceAssignment (werkt)
- fibonacciRecursive (werkt, zonder i++ in while)
- floatToIntConversion (werkt)
- for (werkt)
- forwardDeclaration (werkt)
- if (werkt, zonder &&)
- ifElse (werkt, zonder &&)
- intToFloatConversion (werkt)
- modulo (werkt)
- pointerArgument (werkt)
- prime (werkt, zonder multiple declaration)
- printf1 (werkt)
- printf2 (werkt)
- printf3 (werkt)
- scanf1 (werkt)
- scanf2 (werkt)
- scoping (werkt)
- unaryOperations (werkt)
- variables1 (werkt)
- variables2 (werkt)
- variables3 (werkt)
- variables4 (werkt)
- variables5 (werkt)
- variables6 (werkt)
- variables7 (werkt)
- variables8 (werkt)
- while (werkt)