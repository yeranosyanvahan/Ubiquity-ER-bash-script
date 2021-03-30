def TARIFF_check(Tariff):
    return (Tariff and not Tariff.isspace())
def UP_check(UP):
    try:
        int(UP)
        return True
    except:
        return False
def DOWN_check(DOWN):
    try:
        int(DOWN)
        return True
    except:
        return False
def IP_check(IP):
    Bytes = IP.split('.')
    if len(Bytes) != 4:
        return False
    for Byte in Bytes:
        if not Byte.isdigit():
            return False
        Byte = int(Byte)
        if Byte < 0 or Byte > 255:
            return False
    return True


def Checker(Arguments,Script,Dynamic_Argument):
    Arguments=Arguments[1:]
    if(len(Arguments) != len(Script)):
        return False
    for Some in zip(Arguments,Script):
        if(Some[1] in Dynamic_Argument):
            if (not eval(f"""{Some[1]}_check("{Some[0]}")""")):
                return False
        elif(Some[0]!=Some[1]):
            return False
    return True
