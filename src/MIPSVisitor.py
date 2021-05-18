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
        self.branch_counter = Counter()
        self.symbol_table = SymbolTable()
        self.literal_table = dict()
        self.zero = LiteralNode(0, "i8", -1)

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

    def getOpCode(self, node):
        if "string" in node.type_semantics:
            return 4
        elif node.type == "i8":
            return 11
        elif node.type in DECIMAL_TYPES:
            return 2
        elif node.type in INTEGER_TYPES:
            return 1

    def loadVariable(self, node):
        # Every time a  variable is used it has to be loaded in
        instr = ""
        params = ""
        if isinstance(node, LiteralNode):
            # Variables with type float or double are loaded differently than int type (loads from the .data segment)
            if node.type == "i8":
                #TODO: li want literals worden geladen?
                instr = "lb"
            elif node.type == "i8*":
                # TODO: li want literals worden geladen?
                instr = "la"
            if node.type in INTEGER_TYPES:
                instr = "li"
            elif node.type == "float":
                instr = "l.s"
            elif node.type == "double":
                instr = "l.d"
            params = "$2," + str(node.value)

        elif isinstance(node, IdentifierNode):
            instr = "lw"
            params = "$2," + str(node.temp_address) + "($fp)"
        self.addInstruction(instr, params)


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
        elif "string" in node.type_semantics:
            name = "string" + self.data_counter["string"]
            self.addInstruction(f".asciiz {node.value}", before=True)
            node.value = name

    def exitBinaryOperation(self, node):
        # Convert binary operation node to MIPS
        child1 = self.getSymbol(node.children[0])
        child2 = self.getSymbol(node.children[1])
        # For each child that is a variable, load the variable into a new temporary address
        for child in [child1, child2]:
            if isinstance(child, IdentifierNode):
                self.loadVariable(child)
        # Store the result of the binary operation in a new address
        node.temp_address = "$2"
        # Convert the children to MIPS, depending on their node types
        children_MIPS = []
        the_type = getBinaryType(child1.type, child2.type)
        node.type = the_type
        for child in [child1, child2]:
            # Convert the child to the binary operation type, so that both children have the same type
            # TODO: We gaan waarchijnlijk ook nog een converttype moeten maken voor MIPS
            #self.convertType(child, IdentifierNode(None, None, the_type))
            # TODO: nog een getValue maken voor MIPS
            children_MIPS.append(child.getValue())
        # Construct the LLVM instruction
        # TODO: zijn register om op te slagen is hardcoded op $2
        param = f"$2,{','.join(children_MIPS)}"
        self.addInstruction(self.binaryOpToMIPS(node), param)

    def exitUnaryOperation(self, node):
        #  # Convert unary operation node to MIPS
        #  child = self.getSymbol(node.children[0])
        #  # If the child is a variable, load the variable into a new temporary address
        #  if isinstance(child, IdentifierNode):
        #      self.loadVariable(child)
        #  # Store the result of the unary operation in a new address
        #  node.temp_address = "$2"
        #  # Convert the children to MIPS, depending on their node types
        #  node.type = child.type
        #  # Convert the child to the binary operation type, so that both children have the same type
        #  # TODO: We gaan waarchijnlijk ook nog een converttype moeten maken voor MIPS
        #  #self.convertType(child, IdentifierNode(None, None, child.type))
        #  # Construct the LLVM instruction
        #  # TODO: zijn register om op te slagen is hardcoded op $2
        #  # TODO: nog een getValue maken voor MIPS
        #  param = f"$2,{child.getValue()}"
        if node.operation == "-":
            self.zero.type == node.children[0].type
            bin_op = BinaryOperationNode("-", -1)
            bin_op.add_child(self.zero)
            bin_op.add_child(node.children[0])
            self.exitBinaryOperation(self, bin_op)
        # TODO: not operatie uitzoeken, vooral verschil bij andere types
        # TODO: pointer en array operations

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

    def exitFunctionDefinition(self, node):
        # TODO: If void, then do here a 'nop'.
        # allocate space on the stack for everything inside the function scope
        self.addInstruction("move",     "$sp,$fp")
        self.addInstruction("ld",       "$fp,TBA($sp)")
        self.addInstruction("daddiu",   "$sp,$sp,TBA")
        self.addInstruction("j",        "$31")
        self.addInstruction("nop")

    def exitReturn(self, node):
        # TODO: Return wordt automatisch aangemaakt wanneer er geen return is, mag opzich wel denk ik zou geen probleem moeten vormen in MIPS
        # TODO: niet altijd nop enkel bij void
        self.addInstruction("nop")

    def exitDeclaration(self, node):
        identifier = node.children[0]
        if not isinstance(node.parent.parent, ArgListNode):
            self.symbol_table.add_symbol(identifier)
        if "global" in identifier.type_semantics:
            #TODO: NOG DOEN
            self.addInstruction(identifier.name, ".TYPE VALUE" )

    def exitDefinition(self, node):
        # When there is a definition, do a store word
        self.loadVariable(node.children[1])
        identifier = node.children[0].children[0]
        align = identifier.alignment()
        identifier.temp_address = self.counter.incr_amount(int(align))
        self.storeVariable(node.children[0].children[0])

    def exitAssignment(self, node):
        # When there is an assignement, check if it's already stored. If not then store
        self.loadVariable(node.children[1])
        # if the identifier is not stored somewhere then store in a new address else store in previous address
        # TODO: ALs identifier gedefinieerd is weer in table kijken want type en tempaddres is altijd none anders
        self.storeVariable(node.children[0])

    def type_fprint(self, function_type):
        #TODO: waar REGISTER staat moet het register/naam komen van waar de variabele is
        opcode = None
        if function_type == "i8*":
            self.addInstruction("la", "$a0, REGISTER")
            opcode = 4
        elif function_type == "i8":
            self.addInstruction("lb", "$a0, REGISTER")
            opcode = 11
        elif function_type.startswith("i"):
            self.addInstruction("lw", "$a0, REGISTER")
            opcode = 1
        elif function_type == "float":
            self.addInstruction("l.s", "$f12, REGISTER")
            opcode = 2
        elif function_type == "double":
            self.addInstruction("l.d", "$f12, REGISTER")
            opcode = 3
        self.addInstruction(f"li $v0, {opcode}")
        # syscall does the actual print
        self.addInstruction("syscall")

    def type_scanf(self, function_type):
        opcode = None
        VorF = None
        if function_type.startswith("i"):
            opcode = 5
            VorF = "v0"
        elif function_type == "float":
            opcode = 6
            VorF = "f0"
        #TODO: NOG STRING HIER HELEMAAL DOEN
        #elif function_type == "string":
        #    VorF = "v0"
        #    opcode = 4
        elif function_type == "char":
            opcode = 12
            VorF = "v0"
        # syscall does the actual print
        self.addInstruction("li", f"$v0, {opcode}")
        self.addInstruction("syscall")
        self.addInstruction("sw", f"${VorF}, LOCATION")

    def exitFunctionCall(self, node):
        # Get the function with the right addresses from the table
        function = self.getSymbol(node.children[0])

        # Special cases 'printf' and 'scanf'
        if function.name == "printf":
            #TODO: (mss best in de type_fprint doen) het eerste is altijd een string, dus deze moet nog opgedeeld worden en in MIPS afgeprint worden (wordt voor nu geskipt)
            # Do a print in MIPS for every variable mentioned in the string parameter
            for child in function.parent.children[1].children:
                if child == function.parent.children[1].children[0]:
                    continue
                else:
                    # load the parameter according to the type
                    self.type_fprint(child.type)
        elif function.name == "scanf":
            #TODO: kan deze meerdere parameters hebben?
            self.type_scanf(function.children[1].type)

    def enterWhile(self, node):
        node.start_address = str(self.branch_counter)
        self.addInstruction("b", "$L" + self.branch_counter.incr())
        self.addInstruction("nop")
        self.addInstruction()
        self.addInstruction(f"$L {node.start_address}")

    def enterScope(self, node):
        self.symbol_table.enter_scope()
        if isinstance(node.parent, WhileNode):
            # TODO: de branch id hier staat moet brnachen naar de volgende maar in de condtion gebeurt er zwz een branch die dan niet zal moeten
            # TODO: Hier nog een binary op (hangt af van welke condition)
            self.addInstruction("nop")
            self.addInstruction()
            self.addInstruction("$L" + self.branch_counter.incr())

    def exitScope(self, node):
        self.symbol_table.exit_scope()
        self.addInstruction()

    def exitWhile(self, node):
        self.addInstruction(f"$L {node.start_address}")
