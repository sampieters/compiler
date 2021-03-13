import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from grammars.variables.variablesLexer import variablesLexer
from grammars.variables.variablesParser import variablesParser
from ASTListener import ASTListener
from ASTVisitor import ASTVisitor
from OptimisationVisitor import OptimisationVisitor
from LLVMVisitor import LLVMVisitor

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = variablesLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = variablesParser(token_stream)
    tree = parser.prog()

    lisp_tree_str = tree.toStringTree(recog=parser)
    print(lisp_tree_str)

    listener = ASTListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    AST = listener.curr_node
    AST.to_dot("AST")

    visitor = OptimisationVisitor()
    visitor.visit(AST)

    visitor_2 = LLVMVisitor()
    visitor_2.visit(AST)
    print(visitor_2.LLVM)

    AST.to_dot("AST_OPT")