answer = input("\t Do you know what binary numbers are? ¿Si o No? ").strip()
print("\t You said {} ?".format(answer))
if answer.lower() == ("si"):
    print("\t Awesome!")
elif answer.lower() == ("no"):
    print("\t That's okay! Binary numbers are 0s and 1s.")
else:
    print(input("\t Invalid answer, try again ! ")).lower().strip() #can you loop this so the user answers agai



def main():
    introduction()
    print()
    print("Select one of the following:")
    sel, choice = execute_display(menu_display())
    print()
    print("You selected {} and want to convert {} !".format(sel,choice))
    while sel != 'X':
        if sel == '1':
            num = input ("Enter Binary Number: ")
            right_selection = bin_selection(num)
            right_selection = True
            while not right_selection:
                otra_vez = input("Try Again! Enter a valid BINARY number: ")
            else:
                print("Great!", num, " is a BINARY numer!")
                print("The BINARY number: {0} is equal to the DECIMAL number: {1}.".format(num,(binary_to_decimal(num))))
        elif sel == '2':
            num = input("Enter Decimal Number: ")
            good_selection = dec_selection(num)
            good_selection = False
            while not good_selection:
                try_again = input("Try Again! Enter a valid DECIMAL number: ")
                return False
            else:
                print("Great!", num, " is a DECIMAL number!")
                print("The DECIMAL number: {0} is equal to the BINARY number: {1}".format(num,decimal_to_binary(num)))
        else:
            print("INVALID OPTION")
        print("Bye! Leaving the program.")
        exit()


def menu_dis():
    print("Select one of the following:")
    sel, choice = execute_display(menu_display())
    print()
    print("You selected {} and want to convert {} !".format(sel,choice))
    if sel == '1':
        num = int(input("Provide a BINARY number: "))
        while num >=1:
            print(input("Not a binary number, try again: "))
            return sel, choice
            print("The BINARY number: {0} is equal to the DECIMAL number: {1}.".format(num,(binary_to_decimal(num))))
            print()
    elif sel == '2':
        selection = input("Provide a DECIMAL number: ")
        for number in (dec_selection(numbers)):
            if number.upper() not in dec_list():
                print("Not a decimal number!")
                return(False)
            return(True)
        else:
                print("The DECIMAL number: {0} is equal to the BINARY number: {1}".format(selection,decimal_to_binary(selection)))
                print()
