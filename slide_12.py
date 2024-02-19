def check_selection(numbers):
    hex_list = ["A","B","C","D","E","F","0","1","2","3","4","5", "6", "7","8","9"]
    for number in numbers:
        if number.upper() not in hex_list:
            print("Not a hexadecimal number!")
            return(False)
    return(True)

def main():
    good_selection = False
    while not good_selection:
        selection = input("Provide a hexadecimal number: ")
        good_selection = check_selection(selection)
    print("Good Job!", selection, "is definitely a hexadecimal number.")

if __name__ == "__main__":
    main()

def menu_dis():
    print("Select one of the following:")
    sel, choice = execute_display(menu_display())
    print()
    print("You selected {} and want to convert {} !".format(sel,choice))
    if sel == '1':
        right_selection = False
        while not right_selection:
            num = input("Provide a BINARY number: ")
            right_selection = bin_selection(num)
            print("The BINARY number: {0} is equal to the DECIMAL number: {1}.".format(num,(binary_to_decimal(num))))
            print()

    elif sel == '2':
            good_selection = False
            while not good_selection:
                selection = input("Provide a DECIMAL number: ")
                good_selection = dec_selection(selection)
                print("The DECIMAL number: {0} is equal to the BINARY number: {1}".format(selection,decimal_to_binary(selection)))
                print()

    elif sel == 'X':
        print("Leaving the program...")
        print("Bye! I hope to see you again:)")
        print()
        exit()
