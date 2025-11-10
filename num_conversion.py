def main():
    num = get_input()
    bin = binary(num)
    oct = octal(bin)
    hex = hexadecimal(bin)
    display(num, bin, oct, hex)

def get_input():
    #Promt user for a value to be converted.
    Done = False
    while Done != True:
        try:
            value = int(input("What value would you like to convert? "))
            if value >= 0:
                Done = True
            else:
                raise ValueError
        except ValueError:
            print("Please enter a valid value. ")
        except KeyboardInterrupt:
            print("Please enter a valide value. ")
    return value

def binary(num):
    #Determin closest 2^x to determin how many binary digits it is.
    #Start at end and subtract largest 2^x value you can from num.
    digits_bi = 0
    while num >= 1:
        num /= 2
        digits_bi += 1
    bin = 0
    return bin

def octal(bin):
    #Use binary, segment by three digits starting on the right determin value.
    return 366

def hexadecimal(bin):
    #Use binary, segment by four digits starting on right determin value.
    return "F6"

def display(num, bin, oct, hex):
    print(f"Your number, {num}, is: {bin} in binary, {oct} in octal, and {hex} in hexadecimal")

main()