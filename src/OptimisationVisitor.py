from grammars.variables.variablesParser import variablesParser
from grammars.variables.variablesVisitor import variablesVisitor

class OptimisationVisitor(variablesVisitor):
    # Visit a parse tree produced by variablesParser#Program.
    def visitProgram(self, ctx:variablesParser.ProgramContext):
        print(self.visitChildren(ctx))