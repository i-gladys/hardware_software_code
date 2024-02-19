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
        '1': 'Binary_to_Decimal',
        '2': 'Decimal_to_Binary',
        'X': 'Exit_Program'
    }
    return menu_dict

def execute_display(menu_dict): #This function displays the menu above and ensures that users enter a valid answer.
    for key, value in menu_dict.items():
        print("{}. {}".format(key, value.replace('_', ' ').title()))
    menu_selection = menu_dict.keys()
    selection = "#"
    while selection not in menu_selection:
        print()
        selection = input("Enter: ").upper()
        if selection not in menu_selection:
            print("Invalid Entry!")
    return selection, menu_dict[selection]

def binary_to_decimal(binary_number): #This function calculates the binary to decimal conversion.
    decimal_result = 0
    power = len(binary_number) - 1
    for digit in binary_number:
        decimal_result += int(digit) * 2 ** power
        power -= 1
    return decimal_result

def decimal_to_binary(decimal_number): #This function calculates the decimal to binary conversion.
    binary_result = ""
    number = int(decimal_number)
    while number > 0:
        remainder = number % 2
        number //= 2
        binary_result = str(remainder) + binary_result
    return binary_result

def menu_options(): #This function allow users to interact with the menu options.
    print("Select one of the following:")
    sel, choice = execute_display(menu_display())
    print()
    print("You selected {} and want to convert {}!".format(sel, choice))
    if sel == '1':
        binary_input = input_bin()
        print("The Binary number {} is equal to the Decimal number {}.".format(binary_input, binary_to_decimal(binary_input)))
    elif sel == '2':
        decimal_input = input_dec()
        print("The Decimal number {} is equal to the Binary number {}.".format(decimal_input, decimal_to_binary(decimal_input)))
    elif sel == 'X':
        print("Leaving the program...")
        print("Bye! I hope to see you again :)")
        exit()

def input_bin(): #This function ensures that the user correctly enters a binary number.
    bin_list = set("01")
    num = ""
    while not num.isdigit():
        print()
        num = input("Write your BINARY number: ")
        if not num.isdigit():
            print("[ERROR] Invalid Binary number! Please enter a valid Binary number.")
    return num

def input_dec(): #This function ensures that the user correctly enters a decimal number.
    dec_list = set("0123456789")
    num = ""
    while not num.isdigit():
        print()
        num = input("Write your DECIMAL number: ")
        if not num.isdigit():
            print("[ERROR] Invalid Decimal number! Please enter a valid Decimal number.")
    return num

def main(): #This is the "main" function that organizes the above functions so they can run properly.
    introduction()
    while True:
        print()
        menu_options()
        answer = input("Enter Q to QUIT or any other key to CONTINUE: ").upper()
        if answer == "Q":
            print("Goodbye!")
            exit()
        else:
            print("Invalid entry. Try Again!")

if __name__ == "__main__": #This function calls for the main() function. 
    main()
