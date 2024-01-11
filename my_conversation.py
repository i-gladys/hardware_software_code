def conversation():
    print("Do you like coding in python? Answer yes or no !")
    answer = input()
    x = answer.strip()
    if x.lower() == "yes":
        print("That's good - the United States needs more coders !!")
    elif x.lower() == "no":
        print("Perhaps you will change your mind .")
    else:
        print("I do not understand.")
    print("Goodbye !")

def main():
    print("Welcome to my conversation program .")
    conversation()
    print("Thanks for chatting with me !")

if __name__ == "__main__":
    main()
