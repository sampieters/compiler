import sys
import filecmp
from antlr4 import *
from antlr4.InputStream import InputStream
from grammars.variables.variablesLexer import variablesLexer
from grammars.variables.variablesParser import variablesParser
from ASTListener import ASTListener
from ASTVisitor import ASTVisitor
from SemanticalErrorVisitor import SemanticalErrorVisitor
from OptimisationVisitor import OptimisationVisitor
from LLVMVisitor import LLVMVisitor

if __name__ == '__main__':
    var = input("Please enter test file: ")

    f1 = open("tests/" + var)
    line = f1.read()
    f1.close()

    input_stream = InputStream(line)
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
    AST.to_dot("tests/TEST_AST")

    visitor_err = SemanticalErrorVisitor()
    visitor_err.visit(AST)

    #visitor_opt = OptimisationVisitor()
    #visitor_opt.visit(AST)

    visitor_llvm = LLVMVisitor()
    visitor_llvm.visit(AST)

    AST.to_dot("tests/TEST_AST_OPT")

    with open("tests/" + var + "_RESULT", 'w') as f2:
        f2.write("\n".join(visitor_llvm.LLVM))
    f2.close()

    # HERE COMPARISON OF THE TWO FILES

    #    f1 = open("tests/" + var + "_RESULT", 'r')
    #f2 = open("tests/CMP_" + var, 'r')

    #i = 0
    #for line1 in f1:
    #    i += 1
    #    for line2 in f2:
    #        # matching line1 from both files
    #        if line1 == line2:
    #            # print IDENTICAL if similar
    #            print("Line ", i, ": IDENTICAL")
    #        else:
    #            print("Line ", i, ":")
    #            # else print that line from both files
    #            print("\tFile 1:", line1, end='')
    #            print("\tFile 2:", line2, end='')
    #        break
    # closing files
    f1.close()
    f2.close()
