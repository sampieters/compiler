CONVERSION_HIERARCHY = {"char": 0, "int": 1, "unsigned int": 2, "long": 3, "unsigned long": 4, "long long": 5, "unsigned long long": 6,
                        "float": 7, "double": 8, "long double": 9}

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

def BinaryOpToLLVM(operation):
    LLVMType = {
        "+": "add",
        "-": "mul",
        "*": "sdiv",
        "/": "mod",
        "%": ""
    }
    return LLVMType.get(operation, "Invalid operation: " + operation)

def typeToLLVM(_type):
    _type = _type.replace("const", "")
    _type = _type.replace("unsigned", "")
    _type = _type.replace("signed", "")
    extra = _type.count('*')
    _type = _type.replace("*", "")

    LLVMType = {
        "int": ["i32", "align 4"],
        "short int": ["i16", "align 2"],
        "long int": ["i64", "align 8"],
        "long long int": ["i64", "align 8"],
        "float": ["float", "align 4"],
        "double": ["double", "align 8"],
        "long double": ["alloca x86_fp80", "align 16"],
        "char": ["alloca i8", "align 1"]
    }

    to_return = LLVMType.get(_type, "Invalid type: " + _type)
    to_return[0] += extra * '*'
    return to_return

def getBinaryType(type_1, type_2):
    temp = max(CONVERSION_HIERARCHY[type_1], CONVERSION_HIERARCHY[type_2])
    if CONVERSION_HIERARCHY[type_1] == temp:
        return type_1
    else:
        return type_2


def checkInfoLoss(type_1, type_2):
    # returns true for info loss
    return CONVERSION_HIERARCHY[type_1] < CONVERSION_HIERARCHY[type_2]


class Counter:
    def __init__(self):
        self.counter = 0

    def incr(self):
        self.counter += 1
        return str(self.counter - 1)

    def curr(self):
        return self.counter

    def __str__(self):
        return str(self.counter)
