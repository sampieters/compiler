CONVERSION_HIERARCHY = {"int": 1,"unsigned int": 2, "long": 3, "unsigned long": 4, "long long": 5, "unsigned long long": 6,
                        "float": 7, "double": 8, "long double": 9}


def typeToLLVM(type):
    LLVMType = {
        "void": "idk",
        "int": "i32",
        "float": 'float',
        "double": 'Tuesday',
        "char": 'Wednesday',
    }
    return LLVMType.get(type, "Invalid day of week")


def getAccType(type_1, type_2):
    temp = max(CONVERSION_HIERARCHY[type_1], CONVERSION_HIERARCHY[type_2])
    if CONVERSION_HIERARCHY[type_1] == temp:
        return type_1
    else:
        return type_2


def idk(type):
    print("lol")


def checkInfoLoss(type_1, type_2):
    # returns true for info loss
    return CONVERSION_HIERARCHY[type_1] < CONVERSION_HIERARCHY[type_2]


class Counter:
    def __init__(self):
        self.counter = 0

    def incr(self):
        self.counter += 1
        return self.counter - 1

    def curr(self):
        return self.counter

    def __str__(self):
        return str(self.counter)
