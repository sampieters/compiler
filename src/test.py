import sys
import os
import filecmp
from antlr4 import *
from antlr4.InputStream import InputStream
from grammars.C.CLexer import CLexer
from grammars.C.CParser import CParser
from ASTListener import ASTListener
from ASTVisitor import ASTVisitor
from SemanticalErrorVisitor import SemanticalErrorVisitor
from OptimisationVisitor import OptimisationVisitor
from LLVMVisitor import LLVMVisitor

PATH = "src/tests/benchmarks/CorrectCode/"

filenames = input("Please enter test file(s): ")
filenames = filenames.split()

for filename in filenames:
    file_path = PATH + filename

    f1 = open(f"{file_path}.c")
    line = f1.read()
    print(line)
    f1.close()

    input_stream = InputStream(line)
    lexer = CLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CParser(token_stream)
    tree = parser.prog()

    lisp_tree_str = tree.toStringTree(recog=parser)
    print(lisp_tree_str)

    listener = ASTListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    AST = listener.curr_node
    AST.to_dot("AST")

    visitor_err = SemanticalErrorVisitor()
    visitor_err.visit(AST)

    visitor_opt = OptimisationVisitor()
    visitor_opt.visit(AST)

    visitor_llvm = LLVMVisitor()
    visitor_llvm.visit(AST)

    #AST.to_dot("tests/TEST_AST_OPT")

    with open(f"{file_path}_RESULT.ll", 'w+') as f2:
        f2.write("\n".join(visitor_llvm.LLVM))
    f2.close()

    os.system("clear")
    # HERE COMPARISON OF THE TWO FILES
    print("GENERATED:")
    os.system(f"lli {file_path}_RESULT.ll | tee {file_path}_RESULT.txt")
    f1 = open(f"{file_path}_RESULT.txt", 'r')

    print("\n\nEXPECTED:")

    os.system(f"clang -emit-llvm -S {file_path}.c -o {file_path}.ll")
    os.system(f"lli {file_path}.ll | tee {file_path}_CMP.txt")
    f2 = open(f"{file_path}_CMP.txt", 'r')

    print("\n")

    if f1.read() == f2.read():
        print(f"{filename} succeeded")
    else:
        print(f"{filename} failed")

    f1.close()
    f2.close()

    f1.close()
    f2.close()
