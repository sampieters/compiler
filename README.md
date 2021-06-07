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

Hierna kan men 1 invoeren, om automatisch voor alle .c files in src/tests/benchmarks/CorrectCode/ LLVM te genereren, deze uit te voeren en de output te vergelijken met de gewenste output die door de juist LLVM wordt gegenereerd. Dit zal ook de MIPS genereren in een .asm file maar deze niet vergelijken met de verwachte output.

Ook kan men dit op individuele bestanden uitvoeren door 2 in te voeren, waarna men de filenames invoert.

Als men 3 of 4 invoert, zal hetzelfde gebeuren als voor 1 of 2, enkel zal hier de mips output getoond worden voor vergelijking met de verwachte output. Aangezien MIPS in sommige gevallen licht andere resultaten print (bv. floats worden 5.0 ipv 5.00000, license staat bovenaan) wordt de output niet automatisch vergeleken. De gebruiker zal zelf een "s"(ucceed) of "f"(ailed) moeten ingeven als hij ziet dat de outputs correct of fout zijn

Elke test die dezelfde uitvoer heeft door de LLVM van onze compiler en de echte LLVM te runnen en vergelijken, zal in results.txt komen te staan als filename succeeded. Als 3 of 4 wordt uitgevoerd zal results.txt de zelf ingevoerde resultaten bevatten.

Alle tests die compileren maar een andere uitvoer geven zullen in results.txt komen te staan als filename failed.

Alle tests die niet compileren vanwege een crash of een semantical error, zal in results.txt komen te staan als filename crashed.

Voor meer details bij een crash, zoals de semantical error message moet je main.py op de file uitvoeren.

####MIPS

Voor MIPS wordt er ook hetzelfde door de main.py en test.py files gegenereerd. Deze files kunnen dan in MARS worden uitgevoerd.
Om de files in MARS uit te voeren moet de setting "Initialize program counter to 'main' if defined" aangezet worden, anders werkt de file niet. Deze setting is te vinden onder:

    MARS toolbar --> Settings --> Initialize program counter to 'main' if defined

Men kan de files ook runnen in de terminal (zoals test.py hier doet) door gebruik te maken van `java -jar Mars4_5.jar sm {file_path}_RESULT.asm` 
Hier zal sm zorgen voor de setting dat de program counter op 'main' begint

### 3) geïmplementeerd

Alles wat voltooid is, is zowel voor LLVM als MIPS voltooid

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
- (Optional) Identifier Operations (niet voltooid)
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
- dereferenceAssignment (werkt, zonder (*xp)++ (gebruik in de plaats *xp = *xp + 1))
- fibonacciRecursive (werkt, zonder i++ in while)
- floatToIntConversion (werkt)
- for (werkt)
- forwardDeclaration (werkt)
- if (werkt, zonder &&)
- ifElse (werkt, zonder &&)
- intToFloatConversion (werkt)
- modulo (werkt)
- pointerArgument (werkt)
- prime (werkt)
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