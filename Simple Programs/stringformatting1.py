def print_formatted(number):
    #since binary,octal and hexadecimal numbers contain their prefixes i.e,0b,0o,0x, we use [2:] to print from the third character
    width = len(bin(number)[2:]) #bin() returns the binary format of the number
    for i in range(1, number+1):
        deci = str(i)[2:]
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]
        print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width))
n = int(input())
print_formatted(n)
