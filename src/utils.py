CONVERSION_HIERARCHY = {"i8": 0, "i16": 1, "i32": 2, "i64": 3, "float": 4, "double": 5, "x86_fp80": 6}
ALIGNMENT = {"float": 4, "double": 8, "long double": 16}

BOOLEAN_OPS = {"!", "!=", "==", "<", "<=", ">", ">=", "&&", "||"}
POINTER_OPS = {"*", "&"}

def unaryOpToLLVM(operation):
    LLVMType = {
        "+": ["", ""],
        "-": ["sub", "0"],
        "++": ["add", "1"],
        "--": ["add", "-1"],
        "!": ["not", ""]
    }
    return LLVMType.get(operation, "Invalid operation: " + operation)

def BinaryOpToLLVM(node):
    LLVMType = {
        "+": ["add"],
        "-": ["sub"],
        "*": ["mul"],
        "/": ["div"],
        "%": ["mod"],
        "!=": ["cmp", "ne"],
        "==": ["cmp", "eq"],
        "<=": ["cmp", "le"],
        ">=": ["cmp", "ge"],
        ">": ["cmp", "gt"],
        "<": ["cmp",  "lt"]
    }
    ret_val = ""
    operation = LLVMType.get(node.operation, "Invalid operation: " + node.operation)
    the_type = getBinaryType(node.children[0].type, node.children[1].type)
    # STEP 1: check f or i (example: icmp or fcmp || add or fadd
    if the_type.startswith("i"):
        if operation[0].startswith("cmp"):
            ret_val += "i"
    else:
        ret_val += "f"
    # STEP 2: The actual operation
    ret_val += operation[0] + " "
    # STEP 3: Check if signed or unsigned
    if "unsigned" in node.children[0].type_semantics or "unsigned" in node.children[1].type_semantics:
        if not operation[0].startswith("cmp"):
            ret_val += "nuw"
        elif operation[1] != "eq" and operation[1] != "ne":
            ret_val += "u"
    else:
        if not operation[0].startswith("cmp"):
            ret_val += "nsw"
        elif operation[1] != "eq" and operation[1] != "ne":
            ret_val += "s"

    if len(operation) == 2:
        ret_val += operation[1]
    return ret_val


def getTypeLLVM(_type):
    ret_val = ["", []]

    for keyword in ["const", "unsigned"]:
        if keyword in _type:
            ret_val[1].append(keyword)
            _type = _type.replace(keyword, "")
        
    extra = _type.count('*') * '*'
    _type = _type.replace("*", "").strip()

    LLVMType = {
        "char": "i8",
        "short int": "i16",
        "int": "i32",
        "long int": "i64",
        "long long int": "i64",
        "float": "float",
        "double": "double",
        "long double": "x86_fp80"
    }

    try:
        ret_val[0] = LLVMType[_type]
    except KeyError:
        raise Exception(f"Invalid type: '{_type}'")
    ret_val[0] += extra
    print(ret_val)
    return ret_val

def getAlignment(node):
    if node.type.endswith("*"):
        return 8
    elif node.type.startswith("i"):
        return int(node.type[1:]) / 8
    else:
        return ALIGNMENT[node.type]

def getConversionFunction(node1, node2):
    ret_val = ""
    print(node1.type, node2.type)
    if node1.type == node2.type:
        return None
    if node1.type.startswith("i"):
        if "unsigned" in node1.type_semantics:
            ret_val += "u"
        else:
            ret_val += "s"
        if node2.type in ["float", "double", "long double"]:
            ret_val += "itofp"
        elif getAlignment(node2) > getAlignment(node1):
            ret_val += "ext"
        else:
            ret_val = "trunc"
    elif node2.type.startswith("i"):
        ret_val += "fpto"
        if "unsigned" in node2.type_semantics:
            ret_val += "ui"
        else:
            ret_val += "si"
    elif getAlignment(node2) > getAlignment(node1):
        ret_val = "fpext"
    else:
        ret_val = "fptrunc"

    return ret_val
        

def getBinaryType(type_1, type_2):
    temp = max(CONVERSION_HIERARCHY[type_1], CONVERSION_HIERARCHY[type_2])
    if CONVERSION_HIERARCHY[type_1] == temp:
        return type_1
    else:
        return type_2


def checkInfoLoss(type_1, type_2):
    # returns true for info loss
    print(type_1, type_2)
    return CONVERSION_HIERARCHY[type_1] < CONVERSION_HIERARCHY[type_2]
    

class Counter:
    def __init__(self):
        self.counter = 1

    def incr(self):
        self.counter += 1
        return str(self.counter - 1)

    def curr(self):
        return self.counter

    def __str__(self):
        return str(self.counter)
