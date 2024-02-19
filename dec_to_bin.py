def check_selection(numbers):
    dec_list = ["0","1","2","3","4","5","6","7","8","9"]
    for number in numbers:
        if number.upper() not in dec_list:
            print("Not a decimal number!")
            return(False)
    return(True)

def decimal_to_binary(number):
    result = ""
    number = int(number)
    while number > 0 : #keep dividing until at 0
        remainder = number % 2
        number = number // 2
        result = str(remainder) + result #place string in reverse order
    return result

def main():
    num = input("Enter Decimal Number: ")
    good_selection = False
    while not good_selection:
        try:
            try_again = input("Try Again! Enter a valid decimal number: ")
            #selection = input("Provide a decimal number: ")
            good_selection = check_selection(num)
            print("Good Job!", num, " is a decimal number!")
    #if ((int(num)>=0) and (int(num)<=15)):
        #print("Cool Decimal Number!")
    #else:
        #print("Invalid Input!")
        #try_again = input("Try Again? ")
        print("Decimal {} to Binary: {}".format(num,decimal_to_binary(num)))

if __name__ == "__main__":
    main()
