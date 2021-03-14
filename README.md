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

Alle mandatories van opdracht 1 & 2. 

Optionals geïmplementeerd van opdracht 1:

- Binary operator %
- Comparison operators >=, <=, and !=
- Logical operators &&, ||, and !
- Constant folding

Optionals geïmplementeerd van opdracht 2:

- Identifier Operations.
- 

