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

<u>Python3 main.py [filenames]</u>

Als filenames worden meegegeven, zullen deze worden uitgevoerd (de files staan in src/tests/benchmarks/CorrectCode/ en de parameter hoeft geen .c extensie te bevatten)

Als geen files worden meegegeven kan een input worden ingevoerd na het uitvoeren van main.

Na uitvoer van main zal de LLVM worden uitgeprint, en de AST en geoptimaliseerde AST in dot formaat worden gegenereerd op AST.dot en AST_OPT.dot respectievelijk.

Bovendien kan ook test.py worden uitgevoerd als volgt:

<u>Python3 test.py</u>

Hierna kan men 1 invoeren, om automatisch voor alle .c files in src/tests/benchmarks/CorrectCode/ LLVM te genereren, deze uit te voeren en de output te vergelijken met de gewenste output die door de juist LLVM wordt gegenereerd.

Ook kan men dit op individuele bestanden uitvoeren door 2 in te voeren, waarna men de filenames invoert.

Elke test die dezelfde uitvoer heeft door de LLVM van onze compiler en de echte LLVM te runnen en vergelijken, zal in results.txt komen te staan als filename succeeded.

Alle tests die compileren maar een andere uitvoer geven zullen in results.txt komen te staan als filename failed.

Alle tests die niet compileren vanwege een crash of een semantical error, zal in results.txt komen te staan als filename crashed.

Voor meer details bij een crash, zoals de semantical error message moet je main.py op de file uitvoeren.


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


### 4) Benchmarks (LLVM)

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

### 4) Benchmarks (MIPS)

- binaryOperations1 (werkt)
- binaryOperations2 (werkt)
- breakAndContinue (werkt)
- comparisons1 (werkt, dankzij folding)
- comparisons2 (werkt, dankzij folding)
- dereferenceAssignment (failt, moet * operatie nog nakijken, vooral aan linkerkant van definitie)
- fibonacciRecursive (failt, zonder i++ in while, wss door functie parameters die niet worden gestored in begin v/d functies)
- floatToIntConversion (failt, conversions zijn er nog niet)
- for (werkt)
- forwardDeclaration (failt, wss door functie parameters die niet worden gestored in begin v/d functies)
- if (werkt, zonder &&)
- ifElse (werkt, zonder &&)
- intToFloatConversion (failt, conversions zijn er nog niet, s.s is fout geformat?)
- modulo (werkt)
- pointerArgument (failt, wss door functie parameters en nog iets fout met dereference)
- prime (failt, zonder multiple declaration, print "NIET ZOMAAR")
- printf1 (werkt)
- printf2 (werkt)
- printf3 (werkt)
- scanf1 (failt, probeert sw te doen naar "LOCATION"??)
- scanf2 (failt, probeert sw te doen naar "LOCATION", load "None" in)
- scoping (failt, print "x .TYPE VALUE" en "REGISTER")
- unaryOperations (failt, arrays werken nog niet helemaal, vooral berekenen van $fp adressen en linkerkant in definitie)
- variables1 (failt, kleine fout bij printen van de float (print 0.0 ipv 0.5), mss omdat het in $4 gaat ipv een float register?)
- variables2 (failt, de stores op de stack gebeuren op rar plaatsen)
- variables3 (failt)
- variables4 (failt, dereference lijkt niks te doen)
- variables5 (failt)
- variables6 (failt)
- variables7 (crasht)
- variables8 (crasht)
- while (werkt)