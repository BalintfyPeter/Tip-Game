# My first game ever (=
# Made by VargTheVikernes

def main():
    import random
    import time

    guesses = []

    # Main menu
    def menu():
        print("[------------Main Menu------------]")
        print("[1] New Game")
        print("[2] Stats")
        print("[3] Settings")
        print("[4] Credits & How to Play")
        print("[5] Exit")

    # Back Button
    def back():
        print()
        print()
        print("[1] Back")
        back0 = int(input())

        while back0 != 1:
            int(input("Invalid input!"))

            if back0 == 1:
                break
            main()

    menu()
    menuOption = int(input("Choose an option:"))

    if menuOption == 1:

        print("Give a number range to set the highest and lowes point")

        qna = str(input("Do you need higher and lower marks Y/N:"))

        while qna != "y" or qna != "Y" or qna != "n" or qna != "N":
            if qna == "Y" or qna == "y" or qna == "n" or qna == "N":
                break

            else:
                print("Invalid input!")
                qna = str(input("Do you need higher and lower marks Y/N:"))

        numMin = int(input("Please enter the lowest point:"))
        numMax = int(input("Please enter the highest point:"))

        while numMax <= numMin or numMin >= numMax:

            print("Error: The highest number is lower than the lowest number!")
            time.sleep(1.5)
            numMax = int(input("Please enter the highest point:"))

            if numMax >= numMin or numMin <= numMax:
                break

        randomNumber = random.randint(numMin, numMax)

        # Start
        mainInput = int(input("Take a Guess:"))
        guesses.append(mainInput)

        # Bugfix (1 = 0)
        if mainInput == randomNumber:
            guesses.append(mainInput)
            print("You won!")

            print("[------------Stats------------]")
            print("The right number:", guesses[0])
            print("Number of guesses:", 1)
            print("All of your numbers:", guesses[0])

            if qna == "Y" or qna == "y":
                print("Helper status: ON")
            else:
                print("Helper status: OFF")
            exit()

        # Check helper status
        if qna == "Y" or qna == "y":
            if mainInput > randomNumber:
                print("Lower!")
            elif mainInput < randomNumber:
                print("Higher!")

        while mainInput != randomNumber or mainInput != "/sho":
            guesses.append(mainInput)
            mainInput = int(input("It's not the right number, try again:"))

            if qna == "Y" or qna == "y":
                if mainInput > randomNumber:
                    print("Lower!")
                elif mainInput < randomNumber:
                    print("Higher!")

            elif mainInput < numMin or mainInput > numMax:
                print("Number is out of range")

            elif mainInput == randomNumber:
                print("You won!")
                guesses.append(mainInput)

        # Game Over
        print("[------------Stats------------]")
        print("The right number:", guesses[-1])
        print("Number of guesses:", len(guesses) - 1)
        guesses.remove(guesses[0])
        print("All of your numbers:", guesses[0:])

        if qna == "Y" or qna == "y":
            print("Helper status: ON")
        else:
            print("Helper status: OFF")

        print()
        print()
        print("[1] Main Menu")
        print("[2] Exit")

        # Restart or Exit
        end = int(input())
        if end == 1:
            main()

        elif end == 2:
            exit()

    # Stats
    elif menuOption == 2:
        print("[------------Stats------------]")
        back()

    # Settings
    elif menuOption == 3:
        print("[------------Settings------------]")
        str(input("Do you need higher and lower marks Y/N:"))
        back()

    # Credit & How to Play
    elif menuOption == 4:
        print("[------------How to Play------------]")
        print("- This is a game where you need to guesses a number.")
        print("- You need to give a lowest and a highest point to set the range.")
        print()
        time.sleep(2)
        print("[------------Credits------------]")
        print("- Game was made by Peter Balintfy")

        back()

    # Exit
    elif menuOption == 5:
        print("Thanks for playing!")
        time.sleep(2)
        exit()


# Call Main
main()


# Logo
'''
I----------I    II    I-----\
I----II----I    II    I     I
     II         II    I-----/ 
     II         II    I     
     II         II    I 
'''