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
- (Mandatory) Unary operators + and - (voltooid NOG KIJKEN VOOR unsigned en signed)
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
    - return (voltooid maar geen LLVM)
    - void (niet voltooid)
- (Mandatory) Scopes (voltooid maar testen)
- (Mandatory) Local and global variables (niet voltooid)
- (Mandatory) Functions (nog niet voltooid)

geïmplementeerd van opdracht 6 (niet voltooid)

TODO:
1) opdracht 1 --> Error wanneer float % float nog doen (denk ik)
2) opdracht 1 --> test van float -float is fneg i.p.v. sub (laten we het zo of toch veranderen)
3) opdracht 1 --> fadd, fsub, fmul hebben een spatie te veel in LLVM waarom???

    

