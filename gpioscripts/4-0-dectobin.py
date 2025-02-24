def dectobin(a):
    return ([int(i) for i in bin(a)[2:].zfill(8)])