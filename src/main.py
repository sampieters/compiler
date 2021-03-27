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

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

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
    print("\n".join(visitor_llvm.LLVM))
    AST.to_dot("AST_OPT")