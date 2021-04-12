CONVERSION_HIERARCHY = {"i1": 0, "i8": 1, "i16": 2, "i32": 3, "i64": 4, "float": 5, "double": 6, "x86_fp80": 7}
ALIGNMENT = {"float": 4, "double": 8, "long double": 16}

BOOLEAN_OPS = ["!", "!=", "==", "<", "<=", ">", ">=", "&&", "||"]
POINTER_OPS = ["*", "&"]
INTEGER_TYPES = ["i1", "i8", "i16", "i32", "i64"]
DECIMAL_TYPES = ["float", "double", "x86_fp80"]

UNARY_OPS_LLVM = {
            "+": ["", ""],
            "-": ["sub", "0"],
            "x++": ["add", "1"],
            "++x": ["add", "1"],
            "x--": ["add", "-1"],
            "--x": ["add", "-1"],
            "!": ["not", ""]
        }

BINARY_OPS_LLVM = {
            "+": ["add"],
            "-": ["sub"],
            "*": ["mul"],
            "/": ["div"],
            "%": ["rem"],
            "!=": ["cmp", "ne"],
            "==": ["cmp", "eq"],
            "<=": ["cmp", "le"],
            ">=": ["cmp", "ge"],
            ">": ["cmp", "gt"],
            "<": ["cmp",  "lt"]
        }

def getParent(node, parentClass):
    "Get the closest parent of a certain class, returns None if no such parent is found"
    parent = node.parent
    while parent and not isinstance(parent, parentClass):
        parent = parent.parent
    return parent

def getTypeLLVM(_type):
    ret_val = ["", []]

    for keyword in ["const", "unsigned", "signed"]:
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
        "long double": "x86_fp80",
        "void": "void"
    }

    try:
        ret_val[0] = LLVMType[_type]
    except KeyError:
        raise Exception(f"Invalid type: '{_type}'")
    ret_val[0] += extra
    return ret_val

def getAlignment(node):
    if node.type.endswith("*"):
        return 8
    elif node.type.startswith("i"):
        return int(node.type[1:]) / 8
    else:
        return ALIGNMENT[node.type]

def getConversionFunction(node1, node2):
    # Get conversion function when converting node1 type to node2 type
    ret_val = ""
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
    # returns true if an information loss occurs when converting type 1 to type 2
    try:
        return CONVERSION_HIERARCHY[type_1] > CONVERSION_HIERARCHY[type_2]
    except KeyError:
        return False


def LiteralToLLVM(literal, type):
    new_literal = ""
    if type == "i8":
        new_literal = ord(literal)
    elif type == "float" or type == "double":
        pass
    return new_literal

def predsspaces(address):
    lenght = len(str(address))
    ret_val = "                                                 "
    ret_val = ret_val[lenght:]
    ret_val += "; preds = "
    return ret_val


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
