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
- (optional) Logical operators &&, ||, and ! (niet voltooid)

- (optional) Constant folding (voltooid)

geïmplementeerd van opdracht 2:

- (Mandatory) Types (voltooid)
- (Mandatory) reserved words (voltooid)
- (Mandatory) Variables (voltooid)
- (Mandatory) Pointer Operations (Nog uitgebreid testen / niet voltooid)
- (Optional) Identifier Operations (Nog uitgebreid testen / niet voltooid)
- (Optional) Conversions (testen / voltooid)

- (Optional) Constant Propagation (niet voltooid)

geïmplementeerd van opdracht 3:

- (Mandatory) Comments (voltooid)
    - (Optional) retain comments (niet voltooid)
    - (Optional) comment every instruction (niet voltooid)
- (Mandatory) Printf (niet voltooid)

geïmplementeerd van opdracht 4:

- (Mandatory) Reserved words
    - (Mandatory) for (voltooid)
    - (Mandatory) break (voltooid maar geen LLVM)
    - (Mandatory) continue (voltooid maar geen LLVM)
    - (Optional) switch, case and default (niet voltooid)
- (Mandatory) Scopes (niet voltooid)

geïmplementeerd van opdracht 5:

- (Mandatory) reserved words
    - return (voltooid)
    - void (niet voltooid)
- (Mandatory) Scopes (voltooid maar testen)
- (Mandatory) Local and global variables (niet voltooid)
- (Mandatory) Functions (nog niet voltooid)

geïmplementeerd van opdracht 6 (niet voltooid)


### 4) Benchmarks

- binaryOperations1 (werkt)
- binaryOperations2 (werkt)
- breakAndContinue (werkt)
- comparisons1 (werkt, dankzij folding)
- comparisons2 (werkt, dankzij folding)
- dereferenceAssignment (crasht)
- fibonacciRecursive (crasht)
- floatToIntConversion (crasht)
- for (werkt)
- forwardDeclaration (crasht)
- if (werkt, zonder &&)
- ifElse (werkt, zonder &&)
- intToFloatConversion (crasht)
- modulo (werkt)
- pointerArgument (crasht)
- prime (crasht)
- printf1 (crasht)
- printf2 (crasht)
- printf3 (crasht)
- scanf1 (werkt?)
- scanf2 (crasht)
- scoping (crasht)
- unaryOperations (crasht)
- variables1 (crasht)
- variables2 (crasht)
- variables3 (crasht)
- variables4 (crasht)
- variables5 (crasht)
- variables6 (crasht)
- variables7 (crasht)
- variables8 (crasht)
- while (werkt)

#TODO:
1) zext aub weg bij while loops
2) icmp slt bij while loop heeft een spatie te weinig, maar kvind ni war die da doet
3) for loop doet nog iets anders (extra branch)
4) if else doet een branch instructie anders -> nog aanpassen maar zorgen dat de adrres blijft wanneer enkel if
# VRAGEN