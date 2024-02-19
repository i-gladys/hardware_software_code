def introduction(): #This function introduces my conversion calculator program!
    print("\t\t\t Conversion Calculator \t\t\t")
    print("Hello World! I am a program that converts binary numbers.")
    answer = input("Do you know what binary numbers are? ¿yes or no? ").strip().lower()
    print()
    print("You said {} ?".format(answer))
    if answer.lower() == "yes":
        print("Awesome! No need to further explain, let's convert numbers.")
    elif answer.lower() == "no":
        print("That's okay! Binary numbers are 0s and 1s. The heart of the computer (aka the CPU) operates with only binary numbers. Now that you know what binary numbers are let's start converting numbers! ")
    else:
        print(input("Invalid answer, try again ! "))

def menu_display(): #This function is a dictionary for the menu with key values pairs as the options.
    menu_dict = {
    '1':'Binary_to_Decimal',
    '2':'Decimal_to_Binary',
    'X':'Exit_Program'
    }
    return menu_dict

def execute_display(menu_dict): #This function displays the menu above and ensures that users enter a valid answer.
    for items, values in menu_dict.items():
        print("{}. {}".format(items, values.capitalize()))
    menu_selection = list(menu_dict.keys())
    selection = "#"
    while selection not in menu_selection:
        print()
        selection = input("Enter: ")
        if selection not in menu_selection:
            print("Invalid Entry!")
    return selection, menu_dict[selection]

def input_bin():
    bin_list = ["0","1"]
    num = ""
    while num not in bin_list:
        print()
        num = input("Write your BINARY number: ")
        if num not in bin_list:
            print("[ERROR]")
    return num

def binary_to_decimal(number): #This function calculates the binary to decimal conversion.
    result = 0
    if len(number) > 0 :
        power = len(str(number)) - 1 #determine the greatest power #
        for num in str(number): #
            result += int(num) * 2 ** power # this ** means to the power
            power -= 1 #decrease by 1
        return result

def dec_selection(numbers):
    dec_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for number in numbers:
        if number.upper() not in dec_list:
            print("Not a decimal number!")
            return False
    return True

def decimal_to_binary(number): #This function calculates the decimal to binary conversion.
    result = ""
    number = int(number)
    while number > 0 : #keep dividing until at 0
        remainder = number % 2
        number = number // 2
        result = str(remainder) + result #place string in reverse order
    return result

def menu_options():
    print("Select one of the following:")
    sel, choice = execute_display(menu_display())
    print()
    print("You selected {} and want to convert {} !".format(sel,choice))
    if sel == '1':
        answer = input("Provide a BINARY number:")
        for number in (bin_selection(numbers)):
            for number in numbers:
                if number not in bin_list():
                    print("Not a binary number!")
                    return(False)
            return(True)
        else:
            print("The BINARY number: {0} is equal to the DECIMAL number: {1}".format(answer,binary_to_decimal(answer)))
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
    elif sel == 'X':
        print("Leaving the program...")
        print("Bye! I hope to see you again:)")
        print()
        exit()

def main():
    introduction()
    print()
    menu_dis()
    answer = input("Enter Q to QUIT or C to CONTINUE: ").upper()
    if answer == "Q":
        print("Bye quitter!")
        exit()
    elif answer == "C":
        return menu_dis()
    else:
        print("Try Again! Enter Q or C: ")

if __name__ == "__main__":
    main()
