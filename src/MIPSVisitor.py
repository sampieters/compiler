from ASTVisitor import *
from ASTNode import *
from utils import *
from SymbolTable import *
from collections import Counter as Ctr


class Function_Stack():
    def __init__(self):
        self.data_in_stack = Counter()
        self.return_aanwezig = None
        self.parameter_count = None
        self.MIPS_index = None

    def get_stack_size(self):
        # An extra 4 bytes to hold the frame pointer
        return self.data_in_stack.counter * 4 + 4

    def get_framepointer_loc(self):
        return self.data_in_stack.counter * 4

    def stack_next(self):
        return int(self.data_in_stack.incr()) * 4

    def stack_size(self, size=4):
        # TODO: nog rekening houden met parameters enz
        return self.data_in_stack.counter * size

    def reset(self):
        self.data_in_stack.counter = 0
        self.return_aanwezig = None
        self.paramter_count = None


class Registers():
    # There are 64 registers
    # $0     : $zero      : Hard-wired to 0
    # $1     : $at        : Reserved for pseudo-instructions
    # $2 - $3: $v0 - $v1 : Return values from functions
    def __init__(self):
        self.registers = [False] * 64

    def UseTemporary(self):
        # TODO: make an excpetion
        for i in range(8, 15):
            if self.registers[i] is False:
                self.registers[i] = True
                return str(i)
        for i in range(24, 25):
            if self.registers[i] is False:
                self.registers[i] = True
                return str(i)
        return "Error"

    def FreeTemporary(self, register):
        # TODO: make an excpetion
        if register in range(8, 15) or register in range(24, 25):
            self.registers[register] = False
        else:
            return "exception"

    def UseFloatTemporary(self, double=False):
        for i in range(36, 42):
            if self.registers[i] is False:
                # If double, the first register needs to be an even register such that an uneven is the second register
                if i % 2 == 0 and double:
                    # This is to check if there is one register in between that is used as a float
                    if self.registers[i + 1]:
                        continue
                    # Else load the double in two registers
                    else:
                        self.registers[i] = True
                        self.registers[i + 1] = True
                # If it is a double but the register checked is uneven, then chck the following register
                elif double:
                    continue
                # Else if it is a float, it can be loaded in an even or uneven register
                else:
                    self.registers[i] = True
                return "f" + str(i - 32)
        for i in range(46, 48):
            if self.registers[i] is False:
                # If double, the first register needs to be an even register such that an uneven is the second register
                if i % 2 == 0 and double:
                    # This is to check if there is one register in between that is used as a float
                    if self.registers[i + 1]:
                        continue
                    # Else load the double in two registers
                    else:
                        self.registers[i] = True
                        self.registers[i + 1] = True
                # If it is a double but the register checked is uneven, then chck the following register
                elif double:
                    continue
                # Else if it is a float, it can be loaded in an even or uneven register
                else:
                    self.registers[i] = True
                return "f" + str(i - 42)
        return "Error"


class MIPSVisitor(ASTVisitor):
    def __init__(self):
        self.before_MIPS = [".data"]
        self.MIPS = [".globl main", ".text"]
        self.after_MIPS = []
        self.counter = Counter()
        self.data_counter = Ctr()
        self.branch_counter = Counter()
        self.loop_stack = []
        self.funct_stack = Function_Stack()
        self.temp_counter = Counter()
        self.symbol_table = SymbolTable()
        self.literal_table = dict()
        self.zero = LiteralNode(0, "i8", -1)
        self.registers = Registers()

    def addInstruction(self, instr="", params="", spacing=True, before=False, after=False):
        if before:
            self.before_MIPS.append(instr + ": " + params)
        elif after:
            self.after_MIPS.append(int(spacing) * 8 * ' ' + instr.ljust(8) + params)
        else:
            self.MIPS.append(int(spacing) * 8 * ' ' + instr.ljust(8) + params)

    def getSymbol(self, node):
        if (isinstance(node, IdentifierNode) or isinstance(node, FunctionNode)) and not node.name in [None, "printf",
                                                                                                      "scanf"]:
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

    def loadVariable(self, node, load_as_arg=False):
        # TODO: FLOATS en DOUBLE en CHAR werken echt nog niet
        # Every time a  variable is used it has to be loaded in
        instr = ""
        params = ""
        # If it's needed to load as argument for a syscall, than load it in $a0 (or $a1) or for float and doubles in $f12
        if load_as_arg:
            temp = "a0"
        # Else load in temporary for int and f registers for float and double
        else:
            if node.type == "float" or node.type == "double":
                temp = self.registers.UseFloatTemporary(node.type == "double")
            else:
                temp = self.registers.UseTemporary()
        if isinstance(node, LiteralNode):
            # Variables with type float or double are loaded differently than int type (loads from the .data segment)
            # TODO: bij stirngs lijkt het dat in .data moet geladen worden, dan het adres geladen wordt. ALs een char wil van deze string dan lb van STIRNG ADRES)
            if node.type == "i8*":
                instr = "la"
            elif node.type in INTEGER_TYPES:
                instr = "li"
            elif node.type == "float":
                instr = "l.s"
            elif node.type == "double":
                instr = "l.d"
            params = "$" + str(temp) + "," + str(node.value)

        elif isinstance(node, IdentifierNode):
            if node.type == "i8":
                instr = "lb"
            else:
                instr = "lw"
            params = "$" + str(temp) + "," + str(node.original_address) + "($fp)"
        node.temp_address = temp
        self.addInstruction(instr, params)
        return temp

    def storeVariable(self, node):
        op = None
        if node.type == "float":
            op = "s.s"
        elif node.type == "double":
            op = "s.d"
        elif node.type == "i8":
            op = "sb"
        else:
            op = "sw"

        self.addInstruction(op, "$" + str(node.temp_address) + "," + str(self.funct_stack.stack_next()) + "($fp)")
        self.registers.FreeTemporary(node.temp_address)

    def unaryOpToMIPS(self, node):
        child = self.getSymbol(node.children[0])
        self.binaryOpToMIPS(child, LiteralNode(0, child.type, -1))

    def binaryOpToMIPS(self, node):
        # TODO: nog een extra instructie voor
        child1 = self.getSymbol(node.children[0])
        child2 = self.getSymbol(node.children[1])

        the_type = getBinaryType(child1.type, child2.type)

        ret_val = ""
        try:
            operation = BINARY_OPS_MIPS[node.operation]
        except KeyError:
            raise Exception(f"Invalid binary operation '{node.operation}'")

        # STEP 0: if cmp set
        # TODO: Echt uitgebreid checken
        if operation in ["ne", "eq", "le", "ge", "gt", "lt"]:
            if the_type in ["float", "double"]:
                ret_val += "c."
            else:
                ret_val += "s"

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
            name = node.type + str(self.data_counter[node.type])
            value = f".{node.type} {node.value}"
            self.addInstruction(name, value, before=True)
            node.value = name
        elif "string" in node.type_semantics:
            self.data_counter.update({"string": 1})
            name = "string" + str(self.data_counter["string"])
            self.addInstruction(f".asciiz {node.value}", before=True)
            node.value = name

    def exitBinaryOperation(self, node):
        # Convert binary operation node to MIPS
        child1 = self.getSymbol(node.children[0])
        child2 = self.getSymbol(node.children[1])
        # For each child that is a variable, load the variable into a new temporary address

        # Both child's registers can be freed because not necessary after binary operation
        for child in [child1, child2]:
            if isinstance(child, IdentifierNode):
                self.loadVariable(child)
        for child in [child1, child2]:
            if isinstance(child, IdentifierNode) or isinstance(child, BinaryOperationNode) or isinstance(child,
                                                                                                         UnaryOperationNode):
                self.registers.FreeTemporary(child.temp_address)

        # Store the result of the binary operation in a new address (mostly the adres from the 1st or 2nd child)
        node.temp_address = self.registers.UseTemporary()

        # Convert the children to MIPS, depending on their node types
        children_MIPS = []
        the_type = getBinaryType(child1.type, child2.type)
        node.type = the_type
        for child in [child1, child2]:
            # Convert the child to the binary operation type, so that both children have the same type
            # TODO: We gaan waarchijnlijk ook nog een converttype moeten maken voor MIPS
            # self.convertType(child, IdentifierNode(None, None, the_type))
            # TODO: nog een getValue maken voor MIPS
            # hieronder stond tussen append child.getvalue()
            if isinstance(child, LiteralNode):
                children_MIPS.append(str(child.value))
            else:
                children_MIPS.append("$" + str(child.temp_address))
        # Construct the LLVM instruction
        param = f"${str(node.temp_address)},{','.join(children_MIPS)}"
        self.addInstruction(self.binaryOpToMIPS(node), param)

        # TODO: If this is the last binary op from the sequence of operations, then free

    def exitUnaryOperation(self, node):
        # TODO: not operatie uitzoeken, vooral verschil bij andere types
        # TODO: pointer en array operations
        # Get the identifier or literal
        child = self.getSymbol(node.children[0])
        # If child is an identifier, then load into a register
        if isinstance(child, IdentifierNode):
            self.loadVariable(child)
            # Free register of the identifier to load the result in the same register
            self.registers.FreeTemporary(child.temp_address)
        # Store the result of the unary operation in a new address
        node.temp_address = "$" + str(self.registers.UseTemporary())

        children_MIPS = []
        op = None
        if node.operation == "-":
            op = "subu"
            children_MIPS.append("$zero")
            children_MIPS.append(node.temp_address)
        elif node.operation == "x++":
            op = "addiu"
            children_MIPS.append(node.temp_address)
            children_MIPS.append("1")
        elif node.operation == "++x":
            op = "addiu"
            children_MIPS.append(node.temp_address)
            children_MIPS.append("1")
        elif node.operation == "x--":
            op = "addiu"
            children_MIPS.append(node.temp_address)
            children_MIPS.append("-1")
        elif node.operation == "--x":
            op = "addiu"
            children_MIPS.append(node.temp_address)
            children_MIPS.append("-1")

        param = f"{node.temp_address},{','.join(children_MIPS)}"
        self.addInstruction(op, param)

    def exitFunctionDeclaration(self, node):
        function = node.children[0]
        self.symbol_table.add_symbol(function)

    def enterFunctionDefinition(self, node):
        # Define a function in MIPS starting with the name of the function and allocating eenough space on the stack
        self.addInstruction("")
        function = node.children[0].children[0]
        self.addInstruction(function.name + ":", spacing=False)
        self.funct_stack.MIPS_index = len(self.MIPS)
        self.addInstruction("addiu", "$sp,$sp, -{LABEL}")
        self.addInstruction("sw", "$fp,{LABEL}($sp)")
        self.addInstruction("move", "$fp,$sp")

    def exitFunctionDefinition(self, node):
        self.MIPS[self.funct_stack.MIPS_index] = self.MIPS[self.funct_stack.MIPS_index].replace("{LABEL}", str(
            self.funct_stack.get_stack_size()))
        self.MIPS[self.funct_stack.MIPS_index + 1] = self.MIPS[self.funct_stack.MIPS_index + 1].replace("{LABEL}", str(
            self.funct_stack.get_framepointer_loc()))

        # allocate space on the stack for everything inside the function scope
        self.addInstruction("move", "$sp,$fp")
        self.addInstruction("lw", "$fp," + str(self.funct_stack.get_framepointer_loc()) + "($sp)")
        self.addInstruction("addiu", "$sp,$sp," + str(self.funct_stack.get_stack_size()))

        # If main function, close the program correctly
        if node.children[0].children[0].name == "main":
            self.addInstruction("li", "$v0,10")
            self.addInstruction("syscall")
        else:
            self.addInstruction("jr", "$ra")

    def exitReturn(self, node):
        # TODO: Return wordt automatisch aangemaakt wanneer er geen return is, mag opzich wel denk ik zou geen probleem moeten vormen in MIPS
        # TODO: niet altijd nop enkel bij void
        self.addInstruction("nop")

    def exitDeclaration(self, node):
        identifier = node.children[0]
        if not isinstance(node.parent.parent, ArgListNode):
            self.symbol_table.add_symbol(identifier)
        if "global" in identifier.type_semantics:
            # TODO: NOG DOEN
            self.addInstruction(identifier.name, ".TYPE VALUE")

    def exitDefinition(self, node):
        # When there is a definition, do a store word
        identifier = node.children[0].children[0]
        # print(identifier.type_semantics)
        # if "global" in identifier.type_semantics:
        #    self.addInstruction(identifier.name + ":", ".TYPE", False, True)
        #    pass
        if isinstance(node.children[1], BinaryOperationNode) or isinstance(node.children[1], UnaryOperationNode):
            align = identifier.alignment()
            identifier.original_address = self.counter.incr_amount(int(align))
            self.storeVariable(node.children[1])
        elif isinstance(node.children[1], LiteralNode):
            identifier.temp_address = self.loadVariable(node.children[1])
            align = identifier.alignment()
            identifier.original_address = self.counter.incr_amount(int(align))
            self.storeVariable(node.children[0].children[0])
        else:
            self.addInstruction("DIKKE PIEM")

    def exitAssignment(self, node):
        # When there is an assignement, check if it's already stored. If not then store
        node.children[0].temp_address = self.loadVariable(node.children[1])
        # if the identifier is not stored somewhere then store in a new address else store in previous address
        # TODO: ALs identifier gedefinieerd is weer in table kijken want type en tempaddres is altijd none anders
        self.storeVariable(node.children[0])

    def type_fprint(self, function_type):
        # TODO: waar REGISTER staat moet het register/naam komen van waar de variabele is
        opcode = None
        if function_type == "i8*":
            # self.addInstruction("la", "$a0, REGISTER")
            opcode = 4
        elif function_type == "i8":
            # self.addInstruction("lb", "$a0, REGISTER")
            opcode = 11
        elif function_type.startswith("i"):
            # self.addInstruction("lw", "$a0, REGISTER")
            opcode = 1
        elif function_type == "float":
            # self.addInstruction("l.s", "$f12, REGISTER")
            opcode = 2
        elif function_type == "double":
            # self.addInstruction("l.d", "$f12, REGISTER")
            opcode = 3
        self.addInstruction("li", f"$v0,{opcode}")
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
        # TODO: NOG STRING HIER HELEMAAL DOEN
        # elif function_type == "string":
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
            # TODO: (mss best in de type_fprint doen) het eerste is altijd een string, dus deze moet nog opgedeeld worden en in MIPS afgeprint worden (wordt voor nu geskipt)
            # Do a print in MIPS for every variable mentioned in the string parameter
            for child in function.parent.children[1].children:
                if isinstance(child, IdentifierNode):
                    child = self.getSymbol(child)
                # If the chid is the first parameter (the string) then split it
                if child == function.parent.children[1].children[0]:
                    continue
                else:
                    # load the to print variable in an argument register
                    self.loadVariable(child, True)

                    # load the parameter according to the type
                    self.type_fprint(child.type)
        elif function.name == "scanf":
            # TODO: kan deze meerdere parameters hebben?
            self.type_scanf(function.children[1].type)
        else:
            self.addInstruction("jal", node.children[0].name)

    def enterWhile(self, node):
        # TODO:  CONDITIONS KLOPPEN NIET VOOR BRANCHES
        node.start_address = str(self.branch_counter.incr())
        self.addInstruction()
        self.addInstruction(f"$L{node.start_address}:", "", False)
        self.addInstruction("# BEGIN WHILE CONDITION")

    def enterIf(self, node):
        self.addInstruction("# BEGIN IF CONDITION")

    def enterScope(self, node):
        self.symbol_table.enter_scope()
        if isinstance(node.parent, WhileNode):
            # TODO: Ik denk/hoop dat deze condiition alle gevallen oplost
            self.addInstruction("beq", "$" + node.parent.children[0].temp_address + ", $0, {LABEL}")
            self.loop_stack.append(len(self.MIPS) - 1)
            self.addInstruction("nop")
            self.addInstruction("# END WHILE CONDITION")
            self.addInstruction()
            self.addInstruction("# BEGIN WHILE BODY")
            # self.addInstruction("$L" + self.branch_counter.incr() + ":", "", False)
        if isinstance(node.parent, IfNode):
            self.addInstruction("beq", "REGISTER,$0, {LABEL}")
            self.loop_stack.append(len(self.MIPS) - 1)
            self.addInstruction("nop")
            self.addInstruction("# END IF CONDITION")
            self.addInstruction()
            self.addInstruction("# BEGIN IF BODY")

    def exitWhile(self, node):
        self.symbol_table.exit_scope()
        self.addInstruction("j", f"$L{node.start_address}")
        self.addInstruction("# END WHILE BODY")
        self.addInstruction()
        index = self.loop_stack.pop()
        self.MIPS[index] = self.MIPS[index].replace("{LABEL}", "$L" + str(self.branch_counter.counter))
        self.addInstruction("$L" + self.branch_counter.incr() + ":", "", False)

    def exitIf(self, node):
        self.addInstruction("# END IF BODY")

    def enterElse(self, node):
        self.addInstruction("b", "{LABEL}")
        to_be_added = len(self.MIPS) - 1
        self.addInstruction("nop")

        # First pop from the stack for the branch instruction in the If statement
        index = self.loop_stack.pop()
        self.MIPS[index] = self.MIPS[index].replace("{LABEL}", "$L" + str(self.branch_counter.counter))
        self.addInstruction("$L" + str(self.branch_counter.incr()) + ":", "", False)

        # Then append the new branch instruction such that there are no faulty branches
        self.loop_stack.append(to_be_added)

        self.addInstruction("# BEGIN ELSE BODY")

    def exitElse(self, node):
        self.addInstruction("# END ELSE BODY")

    def exitBranch(self, node):
        # If only if then this is already good, when there is also an else the first branch is solved to go to else and then
        # the second is solved here
        index = self.loop_stack.pop()
        self.MIPS[index] = self.MIPS[index].replace("{LABEL}", "$L" + str(self.branch_counter.counter))
        self.addInstruction("$L" + str(self.branch_counter.incr()) + ":", "", False)
