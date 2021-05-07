from ASTVisitor import *
from ASTNode import *
from utils import *
from SymbolTable import *


class MIPSVisitor(ASTVisitor):
    def __init__(self):
        self.before_MIPS = [".data"]
        self.MIPS = [".text"]
        self.after_MIPS = []
        self.counter = Counter()
        self.spacing = '        '

    def loadVariable(self, node):
        # Every time a  variable is used it has to be loaded in
        if isinstance(node, LiteralNode):
            # Variables with type float or double are loaded differently than int type (loads from the .data segment)
            if node.type in INTEGER_TYPES:
                self.MIPS.append(self.spacing + "li      $2," + str(node.value))
            elif node.type == "float":
                self.MIPS.append(self.spacing + "l.s     $2," + "LITERALNAME")
            elif node.type == "double":
                self.MIPS.append(self.spacing + "l.d     $2," + "LITERALNAME")

        align = node.children[0].children[0].alignment()
        node.children[0].children[0].temp_address = self.counter.incr_amount(align)

    def storeVariable(self, node):
        # TODO: ALs identifier gedefinieerd is weer in table kijken want type en tempaddres is altijd none anders
        self.MIPS.append(self.spacing + "sw      $2," + str(node.temp_address) + "($fp)")

    def binaryOpToLLVM(self, node):
        child1 = self.getSymbol(node.children[0])
        child2 = self.getSymbol(node.children[1])

        the_type = getBinaryType(child1.type, child2.type)

        ret_val = ""
        try:
            operation = BINARY_OPS_MIPS[node.operation]
        except KeyError:
            raise Exception(f"Invalid binary operation '{node.operation}'")

        # STEP 1: The actual operation
        ret_val += operation[0]

        # STEP 2:

        extra = ""
        # STEP 3: Check if signed or unsigned
        if operation[0] != "div" and operation[0] != "rem":
            if "unsigned" in child1.type_semantics or "unsigned" in child2.type_semantics:
                if the_type.startswith("i"):
                    if not operation[0] == "cmp":
                        extra += "nuw"
                    elif operation[1] != "eq" and operation[1] != "ne":
                        extra += "u"
                else:
                    if operation[0] == "cmp":
                        if operation[1] != "ne":
                            extra += "o"
                        else:
                            extra += "u"
            else:
                if the_type.startswith("i"):
                    if not operation[0] == "cmp":
                        extra += "nsw"
                    elif operation[1] != "eq" and operation[1] != "ne":
                        extra += "s"
                else:
                    if operation[0] == "cmp":
                        if operation[1] != "ne":
                            extra += "o"
                        else:
                            extra += "u"
        # If the operation exist of multiple parts (icmp ne)
        if len(operation) == 2:
            extra += operation[1]

        if extra:
            ret_val += " " + extra

        return ret_val


    def enterLiteral(self, node):
        # if type is float or double, then the literals are saved in the .data segment
        if node.type in ["float", "double"]:
            self.before_MIPS.append(node.type + "COUNTER" + ": ." + node.type + " " + node.value)
        # tODO: fiks counter en slaag naam ergens op (in dict)

    def enterFunctionDefinition(self, node):
        # Define a function in MIPS starting with the name of the function and allocating eenough space on the stack
        self.MIPS.append("")
        function = node.children[0].children[0]
        self.MIPS.append(function.name + ':')
        #TODO: TBA moet nog gealloceerde plaats zijn
        self.MIPS.append(self.spacing + "daddiu  $sp,$sp, -TBA")
        self.MIPS.append(self.spacing + "sd      $fp,TBA($sp)")
        self.MIPS.append(self.spacing + "move    $fp,$sp")

    def exitScope(self, node):
        if isinstance(node.parent, FunctionDefinitionNode):
            # TODO: If void, then do here a 'nop'.
            # allocate space on the stack for everything inside the function scope
            self.MIPS.append(self.spacing + "move    $sp,$fp")
            self.MIPS.append(self.spacing + "ld      $fp,TBA($sp)")
            self.MIPS.append(self.spacing + "daddiu  $sp,$sp,TBA")
            self.MIPS.append(self.spacing + "j       $31")
            self.MIPS.append(self.spacing + "nop")

    def exitReturn(self, node):
        # TODO: Return wordt automatisch aangemaakt wanneer er geen return is, mag opzich wel denk ik zou geen probleem moeten vormen in MIPS
        # TODO: niet altijd nop enkel bij void
        self.MIPS.append(self.spacing + "nop")

    def exitDefinition(self, node):
        # When there is a definition, do a store word
        self.loadVariable(node.children[1])
        self.storeVariable(node.children[0].children[0])

    def exitAssignment(self, node):
        # When there is an assignement, check if it's already stored. If not then store
        self.loadVariable(node.children[1])
        # if the identifier is not stored somewhere then store in a new address else store in previous address
        self.storeVariable(node.children[0])

# TODO: laatste doet een move waarom? -> als 2 gebruikt wordt 0 worden voor andere functies???
#self.MIPS.append(self.spacing + "move    $2,$0")











