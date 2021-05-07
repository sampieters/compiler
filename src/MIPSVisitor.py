from ASTVisitor import *
from ASTNode import *
from utils import *
from SymbolTable import *
from collections import Counter as Ctr


class MIPSVisitor(ASTVisitor):
    def __init__(self):
        self.before_MIPS = [".data"]
        self.MIPS = [".text"]
        self.after_MIPS = []
        self.counter = Counter()
        self.data_counter = Ctr()
        self.symbol_table = SymbolTable()
        self.literal_table = dict()

    def addInstruction(self, instr="", params="", spacing=True, before=False, after=False):
        if before:
            self.before_MIPS.append(instr + ": " + params)
        elif after:
            self.after_MIPS.append(int(spacing) * 8 * ' ' + instr.ljust(8) + params)
        else:
            self.MIPS.append(int(spacing) * 8 * ' ' + instr.ljust(8) + params)

    def getSymbol(self, node):
        if (isinstance(node, IdentifierNode) or isinstance(node, FunctionNode)) and not node.name in [None, "printf", "scanf"]:
            return self.symbol_table.get_symbol(node.name)
        else:
            return node

    def loadVariable(self, node):
        # Every time a  variable is used it has to be loaded in
        if isinstance(node, LiteralNode):
            # Variables with type float or double are loaded differently than int type (loads from the .data segment)
            if node.type in INTEGER_TYPES:
                instr = "li"
            elif node.type == "float":
                instr = "l.s"
            elif node.type == "double":
                instr = "l.d"
            params = "$2," + str(node.value)
            self.addInstruction(instr, params)

        align = node.children[0].children[0].alignment()
        node.children[0].children[0].temp_address = self.counter.incr_amount(align)

    def storeVariable(self, node):
        # TODO: ALs identifier gedefinieerd is weer in table kijken want type en tempaddres is altijd none anders
        self.addInstruction("sw", "$2," + str(node.temp_address) + "($fp)")

    def binaryOpToMIPS(self, node):
        child1 = self.getSymbol(node.children[0])
        child2 = self.getSymbol(node.children[1])

        the_type = getBinaryType(child1.type, child2.type)

        ret_val = ""
        try:
            operation = BINARY_OPS_MIPS[node.operation]
        except KeyError:
            raise Exception(f"Invalid binary operation '{node.operation}'")

        # STEP 1: The actual operation
        ret_val += operation

        # STEP 2: check for float or double (less exceptions)
        if the_type == "float":
            ret_val += ".s"

        elif the_type == "double":
            ret_val += ".d"

        else:
            # STEP 3: if type is integer, check for immediate operation (this is for addi and subi)
            if (isinstance(child1, LiteralNode) or isinstance(child2, LiteralNode)) and operation in ["add", "sub"]:
                ret_val += "i"

            # STEP 4: if type is integer, check if signed or unsigned
            if "unsigned" in child1.type_semantics or "unsigned" in child2.type_semantics:
                ret_val += "u"
        return ret_val

    def enterLiteral(self, node):
        # if type is float or double, then the literals are saved in the .data segment
        if node.type in DECIMAL_TYPES:
            self.data_counter.update({node.type: 1})
            name = node.type + self.data_counter[node.type]
            value = f".{node.type} {node.value}"
            self.addInstruction(name, value, before=True)
            node.value = name

    def exitBinaryOperation(self, node):
        # Convert binary operation node to MIPS
        child1 = self.getSymbol(node.children[0])
        child2 = self.getSymbol(node.children[1])
        # For each child that is a variable, load the variable into a new temporary address
        for child in [child1, child2]:
            self.loadVariable(child)
        # Store the result of the binary operation in a new address
        node.temp_address = "$2"
        # Convert the children to MIPS, depending on their node types
        children_MIPS = []
        the_type = getBinaryType(child1.type, child2.type)
        for child in [child1, child2]:
            # Convert the child to the binary operation type, so that both children have the same type
            # TODO: We gaan waarchijnlijk ook nog een converttype moeten maken voor MIPS
            #self.convertType(child, IdentifierNode(None, None, the_type))
            children_MIPS.append(child.getValue())
        # Construct the LLVM instruction
        instruction = f"{node.getValue()} = {self.binaryOpToMIPS(node)} {the_type} {', '.join(children_MIPS)}"
        self.LLVM.append("  " + instruction)

    def exitFunctionDeclaration(self, node):
        function = node.children[0]
        self.symbol_table.add_symbol(function)

    def enterFunctionDefinition(self, node):
        # Define a function in MIPS starting with the name of the function and allocating eenough space on the stack
        self.addInstruction("")
        function = node.children[0].children[0]
        self.addInstruction(function.name + ":", spacing=False)
        #TODO: TBA moet nog gealloceerde plaats zijn
        self.addInstruction("daddiu",   "$sp,$sp, -TBA")
        self.addInstruction("sd",       "$fp,TBA($sp)")
        self.addInstruction("move",     "$fp,$sp")

    def enterScope(self, node):
        self.symbol_table.enter_scope()

    def exitScope(self, node):
        if isinstance(node.parent, FunctionDefinitionNode):
            # TODO: If void, then do here a 'nop'.
            # allocate space on the stack for everything inside the function scope
            self.addInstruction("move",     "$sp,$fp")
            self.addInstruction("ld",       "$fp,TBA($sp)")
            self.addInstruction("daddiu",   "$sp,$sp,TBA")
            self.addInstruction("j",        "$31")
            self.addInstruction("nop")
        self.symbol_table.exit_scope()

    def exitReturn(self, node):
        # TODO: Return wordt automatisch aangemaakt wanneer er geen return is, mag opzich wel denk ik zou geen probleem moeten vormen in MIPS
        # TODO: niet altijd nop enkel bij void
        self.addInstruction("nop")

    def exitDeclaration(self, node):
        identifier = node.children[0]
        if not isinstance(node.parent.parent, ArgListNode):
            self.symbol_table.add_symbol(identifier)

    def exitDefinition(self, node):
        # When there is a definition, do a store word
        self.loadVariable(node.children[1])
        identifier = node.children[0].children[0]
        align = identifier.alignment()
        identifier.temp_address = self.counter.incr_amount(align)
        self.addInstruction("sw", f"$2,{identifier.temp_address}($fp)")
        self.storeVariable(node.children[0].children[0])

    def exitAssignment(self, node):
        # When there is an assignement, check if it's already stored. If not then store
        self.loadVariable(node.children[1])
        # if the identifier is not stored somewhere then store in a new address else store in previous address
        # TODO: ALs identifier gedefinieerd is weer in table kijken want type en tempaddres is altijd none anders
        self.addInstruction("sw", f"$2,{str(node.children[0].temp_address)}($fp)")
        self.storeVariable(node.children[0])

# TODO: laatste doet een move waarom? -> als 2 gebruikt wordt 0 worden voor andere functies???
#self.MIPS.append(self.spacing + "move    $2,$0")











