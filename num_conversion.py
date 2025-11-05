def main():
    num = get_input()
    bin = binary(num)
    oct = octal(bin)
    hex = hexadecimal(bin)
    display(num, bin, oct, hex)

def get_input():
    #promt user for a value to be converted.
    return 238

def binary(num):
    #if odd -1 and put 1 at begining, determin closest 2^x to determin how many binary digits it is.
    #Start at end and subtract largest value you can from 2^x
    return 11110110

def octal(bin):
    #Use binary, segment by three digits starting on the right determin value
    return 366

def hexadecimal(bin):
    #Use binary, segment by four digits starting on right determin value
    return "F6"

def display(num, bin, oct, hex):
    print(num, bin, oct, hex)

main()