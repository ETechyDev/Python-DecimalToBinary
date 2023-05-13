def Convert(num):
    binary = ''
    while num > 0:
        bit = num % 2
        num = num // 2
        binary = str(bit) + binary
    return binary
