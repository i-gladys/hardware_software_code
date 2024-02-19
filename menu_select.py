def execute_display(menu_dict):
    for items, values in menu_dict.items():
        print("{}. {}".format(items, values.capitalize()))
    menu_selection = list(menu_dict.keys())
    selection = "#"
    #print(menu_selection)

    while selection not in menu_selection:
        selection = input("Enter: ")
        if selection not in menu_selection:
            print("Invalid Entry!")

    return selection, menu_dict[selection]

def menu_display():
    menu_dict = { #this is a dictionary, there are key values pair.
        '1':'decimal_to_binary',
        '2':'binary_to_decimal',
        'X':'exit_program'
    }
    #menu_dict_en = menu_dict.encode('ascii')
    return menu_dict #.decode()

def main():
    sel, choice = execute_display(menu_display())
    print("You selected {} and want to convert {} !".format(sel,choice))

if __name__ == "__main__":
    main()
