import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from grammars.C.CLexer import CLexer
from grammars.C.CParser import CParser
from ASTListener import ASTListener
from ASTVisitor import ASTVisitor
from SemanticalErrorVisitor import SemanticalErrorVisitor
from OptimisationVisitor import OptimisationVisitor
from LLVMVisitor import LLVMVisitor
from MIPSVisitor import MIPSVisitor

if __name__ == '__main__':
    # Path to benchmarks
    file_path = "src/tests/benchmarks/CorrectCode/"
    # If a file as given as argument, read it as the inputstream
    if len(sys.argv) > 1:
        f1 = open(f"{file_path + sys.argv[1]}.c")
        input_stream = InputStream(f1.read())
        f1.close()
    # Otherwise wait for input
    else:
        input_stream = InputStream(sys.stdin.readline())

    # Generate CST
    lexer = CLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CParser(token_stream)
    tree = parser.prog()

    lisp_tree_str = tree.toStringTree(recog=parser)
    print(lisp_tree_str)

    # Generate AST
    listener = ASTListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    AST = listener.curr_node

    # Create DOT file of AST
    AST.to_dot("AST")


    # Optimise AST
    visitor_opt = OptimisationVisitor()
    visitor_opt.visit(AST)

    # Create DOT file of optimised AST
    AST.to_dot("AST_OPT")

    # Check AST for semantical errors
    visitor_err = SemanticalErrorVisitor()
    visitor_err.visit(AST)

    # Generate LLVM code from AST
    #visitor_llvm = LLVMVisitor()
    #visitor_llvm.visit(AST)

    # Print out the generated LLVM
    #print("\n".join(visitor_llvm.LLVM))

    # Generate MIPS code from AST
    visitor_mips = MIPSVisitor()
    visitor_mips.visit(AST)

    # Print out the generated MIPS
    print("\n".join(visitor_mips.MIPS))
    
    # AST.to_dot("AST")