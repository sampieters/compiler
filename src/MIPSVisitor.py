from ASTVisitor import *
from ASTNode import *
from utils import *
from SymbolTable import *
from collections import Counter as Ctr
import re
from copy import copy


class Function_Stack():
    def __init__(self):
        self.data_count = 0
        self.return_aanwezig = None
        self.parameter_count = None
        self.MIPS_index = None

    def stack_next(self, variable=4):
        ret_val = self.data_count
        # An extra 4 bytes to hold the frame pointer
        if isinstance(variable, int):
            self.data_count += variable
        elif variable.type.endswith("]"):
            self.data_count += max(4, int(variable.alignment())) * int(variable.type.split()[0].replace("[",""))
        else:
            self.data_count += max(4, int(variable.alignment()))
        return ret_val

    def stack_curr(self):
        return self.data_count

    def reset(self):
        self.data_in_stack.counter = 4
        self.return_aanwezig = None
        self.parameter_count = None


class Registers():
    # There are 64 registers
    # $0     : $zero      : Hard-wired to 0
    # $1     : $at        : Reserved for pseudo-instructions
    # $2 - $3: $v0 - $v1  : Return values from functions
    def __init__(self):
        self.registers = [False] * 64

    def FreeRegister(self, register):
        if not register:
            return
        if register.startswith("f"):
            register = register[1:]
        self.registers[int(register)] = False


    def UseParam(self, type):
        # if not a double than can be loaded in a0-a3
        if type not in ["float", "double"]:
            for i in range(4, 8):
                if self.registers[i] is False:
                    self.registers[i] = True
                    return str(i)
        # Otherwise it has to be loaded in the parameter registers for floats
        else:
            for i in range(44, 47):
                if self.registers[i] is False:
                    # If double, the first register needs to be an even register such that an uneven is the second register
                    if i % 2 == 0 and type == "double":
                        # This is to check if there is one register in between that is used as a float
                        if self.registers[i + 1]:
                            continue
                        # Else load the double in two registers
                        else:
                            self.registers[i] = True
                            self.registers[i + 1] = True
                    # If it is a double but the register checked is odd, then chck the following register
                    elif type == "double":
                        continue
                    # Else if it is a float, it can be loaded in an even or uneven register
                    else:
                        self.registers[i] = True
                    return "f" + str(i - 32)

    def FreeParam(self, register, double=False):
        if register.startswith("f"):
            register = int(register[1:]) + 32
        self.registers[int(register)] = False
        if double:
            self.registers[register+1] = False


    def UseTemporary(self):
        for i in range(8, 16):
            if self.registers[i] is False:
                self.registers[i] = True
                return str(i)
        for i in range(24, 26):
            if self.registers[i] is False:
                self.registers[i] = True
                return str(i)

    def FreeTemporary(self, register):
        if register in range(8, 16) or register in range(24, 26):
            self.registers[register] = False

    def UseFloatTemporary(self, double=False):
        for i in range(36, 43):
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
                # If it is a double but the register checked is odd, then chck the following register
                elif double:
                    continue
                # Else if it is a float, it can be loaded in an even or uneven register
                else:
                    self.registers[i] = True
                return "f" + str(i - 32)
        for i in range(46, 49):
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
        self.stat_stack = []
        self.funct_stack = Function_Stack()
        self.temp_counter = Counter()
        self.symbol_table = SymbolTable()
        self.literal_table = dict()
        self.zero = LiteralNode(0, "i8", -1)
        self.registers = Registers()

    def exitProg(self, node):
        self.before_MIPS.extend(self.MIPS)
        self.before_MIPS.extend(self.after_MIPS)
        self.MIPS = self.before_MIPS

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

    def convertType(self, node1, node2):
        # type1 identifier_1 = something;
        # type2 identifier_2 = identifier_1; <-- This in this function is converted to llvm
        # node parameter needs to have type 1 in it
        # Convert node1 type to node2 type
        node1 = self.getSymbol(node1)
        node2 = self.getSymbol(node2)

        if isinstance(node1, LiteralNode):
            if node2.type == "float":
                if node1.type.startswith("i"):
                    self.data_counter.update({"float": 1})
                    self.addInstruction("float" + str(self.data_counter["float"]), ".float " + str(node1.value), True, True)
                    node1.value = "float" + str(self.data_counter["float"])
                    node1.type = "float"
                elif node1.type == "double":
                    for i in range(0, len(self.before_MIPS)):
                        if node1.value in self.before_MIPS[i]:
                            self.before_MIPS[i] = self.before_MIPS[i].replace(".double", ".float")
                            node1.value.replace(".double", ".float")
                    node1.type = "float"
            elif node2.type == "double":
                if node1.type.startswith("i"):
                    self.data_counter.update({"double": 1})
                    self.addInstruction("double" + str(self.data_counter["double"]), ".double " + str(node1.value), True, True)
                    node1.value = "double" + str(self.data_counter["double"])
                    node1.type = "double"
            elif node2.type == "i32":
                if node1.type == "double":
                    for i in range(0, len(self.before_MIPS)):
                        if node1.value in self.before_MIPS[i]:
                            start = self.before_MIPS[i].find(".double")
                            substr = self.before_MIPS[i][start:]
                            substr = substr.replace(".double", "")
                            end = substr.find(".")
                            substr = substr[:end]
                            node1.value = int(substr)
                    node1.type = "i32"
            return

        if node1.type.startswith("i") and node2.type in DECIMAL_TYPES:
            node1.temp_address = self.registers.UseFloatTemporary()
            self.addInstruction("l.s", "$" + node1.temp_address + ", " + str(node1.original_address) + "($fp)")

        # if both types are the same, no problem
        if node1.type == node2.type:
            return
        # a convert instruction always begins with cvt
        instruction = "cvt"
        if node2.type == "float":
            instruction += ".s"
        elif node2.type == "double":
            instruction += ".d"
        else:
            instruction += ".w"

        if node1.type == "float":
            instruction += ".s"
        elif node1.type == "double":
            instruction += ".d"
        else:
            instruction += ".w"

        if instruction == "cvt.w.w":
            return

        # The result of a conversion is always stored in a float/double register
        stored = self.registers.UseFloatTemporary(node2.type == "double")


        self.addInstruction(instruction, "$" + stored + "," + "$" + node1.temp_address)
        node1.temp_address = stored
        if node2.type.startswith("i"):
            node1.temp_address = self.registers.UseTemporary()
            self.addInstruction("mfc1", "$" + node1.temp_address + ", $" + stored)
        node1.type = node2.type
        self.storeVariable(node1)

    def loadVariable(self, node, load_as_arg=False, load_as_return=False):
        # Every time a  variable is used it has to be loaded in
        instr = ""
        params = ""
        # If it's needed to load as argument for a syscall, than load it in $a0 (or $a1) or for float and doubles in $f12
        if load_as_arg:
            temp = self.registers.UseParam(node.type)
        # Else load in temporary for int and f registers for float and double
        elif load_as_return:
            if node.type in ["float", "double"]:
                temp = "f0"
            else:
                temp = "v0"
        elif node.type == "float" or node.type == "double":
            temp = self.registers.UseFloatTemporary(node.type == "double")
        else:
            temp = self.registers.UseTemporary()
        if isinstance(node, LiteralNode):
            # Variables with type float or double are loaded differently than int type (loads from the .data segment)
            # TODO: bij stirngs lijkt het dat in .data moet geladen worden, dan het adres geladen wordt. ALs een char wil van deze string dan lb van STIRNG ADRES)
            if node.type == "i8*" or "string" in node.type_semantics or node.type.endswith("i8]"):
                instr = "la"
            elif node.type in INTEGER_TYPES:
                instr = "li"
            elif node.type == "float":
                instr = "l.s"
            elif node.type == "double":
                instr = "l.d"
            params = "$" + str(temp) + ", " + str(node.value)

        elif isinstance(node, IdentifierNode) or isinstance(node, UnaryOperationNode) or isinstance(node, BinaryOperationNode) or isinstance(node, FunctionCallNode):
            #################################
            # TEST
            #################################
            if node.type == "i8*" or "string" in node.type_semantics or node.type.endswith("i8]"):
                instr = "la"
            elif node.type == "i8":
                instr = "lb"
            elif node.type == "float":
                instr = "l.s"
            elif node.type == "double":
                instr = "l.d"
            else:
                instr = "lw"
            if (isinstance(node, UnaryOperationNode) or isinstance(node, BinaryOperationNode)) and node.operation not in ["[]", "&", "*"]:
                self.storeVariable(node)
            if "global" in node.type_semantics:
                name = node.name
            elif isinstance(node, UnaryOperationNode) and node.operation == "*":
                name = str(self.getSymbol(getChild(node, IdentifierNode)).original_address) + "($fp)"
            elif isinstance(node, UnaryOperationNode) and node.operation == "&":
                instr = "move"
                name = "$" + str(node.temp_address)
            elif isinstance(node, UnaryOperationNode) and node.operation == "[]" and node.temp_address:
                name = "0($" + str(node.temp_address) + ")"
            else:
                name = str(node.original_address) + "($fp)"
            params = "$" + str(temp) + ", " + name
        node.temp_address = temp
        self.addInstruction(instr, params)
        curr = node
        while (isinstance(curr, UnaryOperationNode) and curr.operation == "*"):
            self.addInstruction("lw", "$" + str(temp) + ", 0($" + str(temp) + ")")
            curr = curr.children[0]
        return temp

    def storeVariable(self, node, location=None):
        op = None
        if node.type == "float":
            op = "s.s"
        elif node.type == "double":
            op = "s.d"
        elif node.type == "i8":
            op = "sb"
        else:
            op = "sw"

        if location is None:
            node.original_address = self.funct_stack.stack_next(node)
            address = str(node.original_address) + "($fp)"
        elif isinstance(location, str):
            address = location
            node.original_address = location
        else:
            node.original_address = location.original_address
            address = str(node.original_address) + "($fp)"
        self.addInstruction(op, "$" + str(node.temp_address) + ", " + address)
        self.registers.FreeRegister(str(node.temp_address))

    def unaryOpToMIPS(self, node):
        child = self.getSymbol(node.children[0])
        self.binaryOpToMIPS(child, LiteralNode(0, child.type, -1))

    def binaryOpToMIPS(self, node):
        child1 = self.getSymbol(node.children[0])
        child2 = self.getSymbol(node.children[1])

        the_type = getBinaryType(child1.type, child2.type)

        ret_val = ""
        try:
            operation = BINARY_OPS_MIPS[node.operation]
        except KeyError:
            raise Exception(f"Invalid binary operation '{node.operation}'")

        # STEP 0: if cmp set
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
            if (isinstance(child1, LiteralNode) or isinstance(child2, LiteralNode)) and operation in ["add", "sub", "lt"]:
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
            a = re.findall(r"%\d+s", node.value)
            if a:
                node.type_semantics.append(int(a[0][1:-1]))

            for idx, elem in enumerate(re.split(r'%d|%i|%s|%c|%f|%\d*s', node.value)):
                elem = elem.replace("\\0A", "\\n").replace("\\09", "\\t")
                name = "string" + str(self.data_counter["string"]) + "_" + str(idx + 1)
                self.addInstruction(name, f".asciiz \"{elem}\"", before=True)
            node.value = "string" + str(self.data_counter["string"])

    def exitBinaryOperation(self, node):
        # Convert binary operation node to MIPS
        child1 = self.getSymbol(node.children[0])
        child2 = self.getSymbol(node.children[1])
        # For each child that is a variable, load the variable into a new temporary address
        for child in [child1, child2]:
            if (isinstance(child, UnaryOperationNode) and child.operation == "[]") or isinstance(child, FunctionCallNode):
                self.loadVariable(child)

        # Both child's registers can be freed because not necessary after binary operation
        for child in [child1, child2]:
            if isinstance(child, IdentifierNode):
                self.loadVariable(child)
        for child in [child1, child2]:
            if isinstance(child, IdentifierNode) or isinstance(child, BinaryOperationNode) or isinstance(child,
                                                                                                         UnaryOperationNode):
                self.registers.FreeRegister(child.temp_address)

        # Store the result of the binary operation in a new address (mostly the adres from the 1st or 2nd child)
        node.temp_address = self.registers.UseTemporary()

        # Convert the children to MIPS, depending on their node types
        children_MIPS = []
        the_type = getBinaryType(child1.type, child2.type)
        node.type = the_type
        for child in [child1, child2]:
            # Convert the child to the binary operation type, so that both children have the same type
            if child == child1:
                if child1.type == the_type:
                    self.convertType(child2, child1)
                else:
                    self.convertType(child1, child2)
            if isinstance(child, LiteralNode):
                children_MIPS.append(str(child.value))
            else:
                children_MIPS.append("$" + str(child.temp_address))
        # Construct the LLVM instruction         
        param = ""
        if node.operation != "%":
            param += f"${str(node.temp_address)}, "
        param += ', '.join(children_MIPS)
        
        self.addInstruction(self.binaryOpToMIPS(node), param)
        if node.operation == "%":
            self.addInstruction("mfhi", f"${str(node.temp_address)}")

        # If this is the last binary or unary operation from the sequence of operations, then free
        if not getParent(node, BinaryOperationNode) or not getParent(node, UnaryOperationNode):
            self.registers.FreeRegister(node.temp_address)

    def exitUnaryOperation(self, node):
        # Get the identifier or literal
        child = self.getSymbol(node.children[0])
        # If child is an identifier, then load into a register
        if isinstance(child, IdentifierNode) and node.operation not in ["[]", "&"]:
            self.loadVariable(child)
            # Free register of the identifier to load the result in the same register
            self.registers.FreeRegister(child.temp_address)
        # Store the result of the unary operation in a new address
        node.temp_address = str(self.registers.UseTemporary())

        children_MIPS = []
        op = None
        if node.operation == "-":
            op = "subu"
            children_MIPS.append("$zero")
            children_MIPS.append("$" + str(node.temp_address))
        if node.operation == "*":
            op = "lw"
            children_MIPS.append(f"0(${str(node.temp_address)})")
            if (isinstance(node.parent, AssignmentNode) and node.parent.children[0].operation == "*") or getParent(node, FunctionCallNode):
                return
        elif node.operation == "&":
            node.original_address = child.original_address
            op = "addiu"
            children_MIPS.append("$fp")
            children_MIPS.append(str(child.original_address))
        elif node.operation == "[]":
            if getParent(node, DeclarationNode):
                return
            identifier = self.getSymbol(node.children[0])
            index = self.getSymbol(node.children[1])
            if not isinstance(index, LiteralNode):
                self.addInstruction("sll", f"${index.temp_address}, ${index.temp_address}, 2")
                self.addInstruction("add", f"${index.temp_address}, ${index.temp_address}, {identifier.original_address}")
                self.addInstruction("add", f"${index.temp_address}, ${index.temp_address}, $fp")
                node.temp_address = node.children[1].temp_address
            else:
                node.temp_address = None
                node.original_address = identifier.original_address + node.children[1].value * int(identifier.alignment())
            node.type = "".join(identifier.type.split()[2:])[:-1]
            return
        elif node.operation == "x++" or node.operation == "++x":
            op = "addiu"
            children_MIPS.append("$" + str(child.temp_address))
            children_MIPS.append("1")
        elif node.operation == "x--" or node.operation == "--x":
            op = "addiu"
            children_MIPS.append("$" + str(node.temp_address))
            children_MIPS.append("-1")

        param = f"${node.temp_address}, {', '.join(children_MIPS)}"
        self.addInstruction(op, param)

        # If this is the last binary or unary operation from the sequence of operations, then free
        if (not getParent(node, BinaryOperationNode) or not getParent(node, UnaryOperationNode)) and not node.operation == "*":
            self.registers.FreeRegister(node.temp_address)
        if node.operation in ["x++", "++x", "x--", "--x"]:
            self.storeVariable(child, child)

    def exitFunctionDeclaration(self, node):
        function = node.children[0]
        self.symbol_table.add_symbol(function)

    def enterFunctionDefinition(self, node):
        # Define a function in MIPS starting with the name of the function and allocating eenough space on the stack
        self.addInstruction("")
        function = node.children[0].children[0]
        self.addInstruction(function.name + ":", spacing=False)
        self.funct_stack.MIPS_index = len(self.MIPS)
        self.addInstruction("addiu", "$sp, $sp, -{LABEL}")
        self.addInstruction("sw", "$fp, {LABEL}($sp)")
        self.addInstruction("sw",   "$ra, {LABEL}($sp)")
        self.addInstruction("sw", "$4, {LABEL}($sp)")
        self.addInstruction("move", "$fp, $sp")

    def exitFunctionDefinition(self, node):
        # stack size
        l1 = self.funct_stack.stack_next() + 12
        l1 = str(l1 + l1 % 8)
        self.MIPS[self.funct_stack.MIPS_index] = self.MIPS[self.funct_stack.MIPS_index].replace("{LABEL}", l1)
        # frame pointer place
        l2 = str(self.funct_stack.stack_curr() + 4)
        self.MIPS[self.funct_stack.MIPS_index + 1] = self.MIPS[self.funct_stack.MIPS_index + 1].replace("{LABEL}", l2)
        # return address
        l3 = str(self.funct_stack.stack_curr())
        self.MIPS[self.funct_stack.MIPS_index + 2] = self.MIPS[self.funct_stack.MIPS_index + 2].replace("{LABEL}", l3)
        l4 = str(self.funct_stack.stack_curr() - 4)
        self.MIPS[self.funct_stack.MIPS_index + 3] = self.MIPS[self.funct_stack.MIPS_index + 3].replace("{LABEL}", l4)

        self.addInstruction("$FUNC_" + node.children[0].children[0].name + ":", spacing=False)
        # allocate space on the stack for everything inside the function scope
        self.addInstruction("move", "$sp, $fp")
        self.addInstruction("lw", "$4, " + l4 + "($sp)")
        self.addInstruction("lw", "$ra, " + l3 + "($sp)")
        self.addInstruction("lw", "$fp, " + l2 + "($sp)")
        self.addInstruction("addiu", "$sp, $sp, " + l1)

        # If main function, close the program correctly
        if node.children[0].children[0].name == "main":
            self.addInstruction("li", "$2, 10")
            self.addInstruction("syscall")
        else:
            self.addInstruction("jr", "$ra")

    def exitReturn(self, node):
        if node.children:
            child = self.getSymbol(node.children[0])
            self.loadVariable(child, False, True)
            self.addInstruction("j", "$FUNC_" + getParent(node, FunctionDefinitionNode).children[0].children[0].name)

    def exitDeclaration(self, node):
        identifier = node.children[0]
        if not isinstance(node.parent.parent, ArgListNode):
            self.symbol_table.add_symbol(identifier)

            # if only a declaration, store $0 in the original address of the node (example: int y;)
        if not isinstance(node.parent, DefinitionNode):
            identifier.original_address = self.funct_stack.stack_next(identifier)

    def exitDefinition(self, node):
        # When there is a definition, do a store word
        identifier = self.getSymbol(node.children[0].children[0])
        value = self.getSymbol(node.children[1])

        if isinstance(value, LiteralNode) and value.type == "double":
            self.convertType(value, identifier)

        temp = LiteralNode(0, identifier.type, -1)
        identifier.type = value.type

        if "global" in identifier.type_semantics:
            if identifier.type.startswith("i"):
                if identifier.type == "i8":
                    the_type = ".byte"
                else:
                    the_type = ".word"
            else:
                the_type = "." + identifier.type
            self.addInstruction(identifier.name, the_type + "  " + str(value.value), True, True)
        elif isinstance(value, UnaryOperationNode) and value.operation == "&":
            identifier.temp_address = value.temp_address
            self.storeVariable(identifier)
            self.registers.FreeRegister(identifier.temp_address)
        elif isinstance(identifier, UnaryOperationNode) and identifier.operation == "*":
            self.storeVariable(value, "0($" + identifier.temp_address + ")")
        else:
            # Get the node for the assignement
            # load the right side in to store it in the left side (identifier)
            # Check if it's already stored. If not then store
            identifier.temp_address = self.loadVariable(value)
            # if the identifier is not stored somewhere then store in a new address else store in previous address
            self.storeVariable(identifier)
            self.registers.FreeRegister(identifier.temp_address)
        self.convertType(identifier, temp)

    def exitAssignment(self, node):
        # Get the node for the assignement
        identifier = self.getSymbol(node.children[0])
        value = self.getSymbol(node.children[1])

        # convert the type of the right side to the type of the left side if necessary
        self.convertType(value, identifier)

        # load the right side in to store it in the left side (identifier)
        self.loadVariable(value)

        # if the identifier is not stored somewhere then store in a new address else store in previous address
        if isinstance(identifier, UnaryOperationNode) and identifier.operation == "*":
            self.storeVariable(value, f"0(${identifier.temp_address})")
        else:
            # if the identifier is not stored somewhere then store in a new address else store in previous address
            self.storeVariable(value, identifier)
        self.registers.FreeRegister(value.temp_address)

    def type_fprint(self, function_type):
        opcode = None
        # Different opcodes for different types
        if function_type.endswith("i8]") or function_type == "i8*":
            opcode = 4
        elif function_type == "i8":
            opcode = 11
        elif function_type.startswith("i"):
            opcode = 1
        elif function_type == "float":
            opcode = 2
        elif function_type == "double":
            opcode = 3
        self.addInstruction("li", f"$2, {opcode}")
        # syscall does the actual print
        self.addInstruction("syscall")

    def type_scanf(self, function_type, identifier, length=None):
        opcode = None
        VorF = None
        if function_type.startswith("i"):
            opcode = 5
            VorF = "v0"
        elif function_type == "float":
            opcode = 6
            VorF = "f0"
        elif function_type == "double":
            opcode = 7
            VorF = "f0"
        elif function_type.endswith("i8]"):
            VorF = "v0"
            opcode = 8
            self.addInstruction("li", f"$5, {length+1}")
        elif function_type == "i8":
            opcode = 12
            VorF = "v0"
        # syscall does the actual print
        self.addInstruction("li", f"$2, {opcode}")
        self.addInstruction("syscall")
        if opcode != 8:
            self.addInstruction("sw", f"${VorF}, {identifier.original_address}($fp)")

    def exitFunctionCall(self, node):
        # Get the function with the right addresses from the table
        function = self.getSymbol(node.children[0])

        if function.name in ["printf", "scanf"]:
            str_len = None
            for elem in self.getSymbol(node.children[1].children[0]).type_semantics:
                print(elem)
                if isinstance(elem, int):
                    str_len = elem
            for idx, child in enumerate(node.children[1].children):
                if isinstance(child, IdentifierNode):
                    child = self.getSymbol(child)

                if idx > 0:
                    if "string" in child.type_semantics:
                        child.value += "_1"
                    index = self.loadVariable(child, True)
                    if function.name == "printf":
                        self.type_fprint(child.type)
                    else:
                        #self.loadVariable(child, load_as_arg=True)

                        self.type_scanf(self.getSymbol(child.children[0]).type, self.getSymbol(child), str_len)
                    self.registers.FreeParam(index, child.type == "double")

                tmp = copy(node.children[1].children[0])
                tmp.value += "_" + str(idx+1)
                index = self.loadVariable(tmp, True)
                self.type_fprint(tmp.type)
                self.registers.FreeParam(index, tmp.type == "double")
            return

        # load the function parameters in a0-a4 if there are any
        for child in node.children[1].children:
            if isinstance(child, IdentifierNode):
                child = self.getSymbol(child)
                # load the to print variable in an argument register
            index = self.loadVariable(child, True)
            # if printf or scanf than opcode loaden and syscall

        # Clear all registers for parameters
        for i in range(4, 8):
            self.registers.FreeParam(str(i))
        for i in range(44, 47):
            self.registers.FreeParam(str(i))

        self.addInstruction("jal", node.children[0].name)
        node.temp_address = 2
        node.type = self.getSymbol(node.children[0]).type
        self.storeVariable(node)

    def enterWhile(self, node):
        node.start_address = str(self.branch_counter.incr())
        self.addInstruction()
        self.addInstruction(f"$L{node.start_address}:", "", False)
        self.addInstruction("# BEGIN WHILE CONDITION")

    def enterIf(self, node):
        self.addInstruction("# BEGIN IF CONDITION")

    def enterScope(self, node):
        self.symbol_table.enter_scope()
        if isinstance(node.parent, FunctionDefinitionNode):
            function = node.parent.children[0].children[0]
            for idx, child in enumerate(function.children[0].children):
                child = self.getSymbol(child.children[0])
                child.temp_address = str(4 + idx)
                self.storeVariable(child)
        elif isinstance(node.parent, WhileNode):
            child = self.getSymbol(node.parent.children[0])
            if not isinstance(child, UnaryOperationNode) or not isinstance(child, BinaryOperationNode):
                self.loadVariable(child)
            self.addInstruction("beq", "$" + child.temp_address + ", $0, {LABEL}")
            self.loop_stack.append(len(self.MIPS) - 1)
            self.addInstruction("nop")
            self.addInstruction("# END WHILE CONDITION")
            self.addInstruction()
            self.addInstruction("# BEGIN WHILE BODY")
        elif isinstance(node.parent, IfNode):
            child = self.getSymbol(node.parent.children[0])
            if not isinstance(child, UnaryOperationNode) or not isinstance(child, BinaryOperationNode):
                self.loadVariable(child)
            self.addInstruction("beq", "$" + child.temp_address + ", $0, {LABEL}")
            self.stat_stack.append(len(self.MIPS) - 1)
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
        while "{BREAK}" in self.MIPS[index]:
            self.MIPS[index] = self.MIPS[index].replace("{BREAK}", "L" + str(self.branch_counter.counter))
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
        index = self.stat_stack.pop()
        self.MIPS[index] = self.MIPS[index].replace("{LABEL}", "$L" + str(self.branch_counter.counter))
        self.addInstruction("$L" + str(self.branch_counter.incr()) + ":", "", False)

        # Then append the new branch instruction such that there are no faulty branches
        self.stat_stack.append(to_be_added)

        self.addInstruction("# BEGIN ELSE BODY")

    def exitElse(self, node):
        self.addInstruction("# END ELSE BODY")

    def exitBranch(self, node):
        # If only if then this is already good, when there is also an else the first branch is solved to go to else and then
        # the second is solved here
        index = self.stat_stack.pop()
        self.MIPS[index] = self.MIPS[index].replace("{LABEL}", "$L" + str(self.branch_counter.counter))
        self.addInstruction("$L" + str(self.branch_counter.incr()) + ":", "", False)

    def enterContinue(self, node):
        # Continue works only on while or for loop so when continue, go to the statement of the while or for loop
        first_while = getParent(node, WhileNode)
        self.addInstruction("j", "$L" + first_while.start_address)

    def enterBreak(self, node):
        self.addInstruction("j", "${BREAK}")
        self.loop_stack.append(len(self.MIPS) - 1)