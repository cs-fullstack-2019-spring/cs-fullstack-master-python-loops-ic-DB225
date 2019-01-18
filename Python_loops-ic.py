def main():
#EXERCISE0
#Print Loop
    print("Loop")

#######################################################################
#EXERCISE1
#Create a program that takes user input.
# Print Loop. Nothing is done with the user input yet.

    quest = input("Put a user input: ")
    print("LOOP")

#######################################################################
#EXERCISE2
#Create a program that takes user input and prints the user input.
    quest1 = input("Put a user input: ")
    print(quest1)

#######################################################################
#EXERCISE3
#Create a program that takes user input in a while loop.
# If they enter ‘q’ or 0 (your choice), quit.
# Inside the loop print LOOP
    quest2 = input("Put a user input: ")
    while(quest2 != "q" or quest2 != 0):
        print("PRINT LOOP")
        break
#######################################################################
#EXERCISE4
#Create a program that takes user input in a while loop.
# If they enter 1, print ONE.
# If they enter 2, print TWO.
# If they enter 3 print 3. If they enter ‘q’ or 0 (your choice), quit.
# Else, print ERROR.
    numbers = int(input("Put a number from 1 through 3: "))
    while(numbers != 0 or numbers != "q"):
        if(numbers == 1):
             print("ONE")
        elif(numbers == 2):
            print("TWO")
        elif(numbers == 3):
            print("3")
        else:
            print("ERROR")
        break
#######################################################################
#EXERCISE5
#Create a program that takes user input.
# If they enter 1, call a function that prints IN FUNCTION 1.
# If they press 2, call a function that prints IN FUNCTION 2.
# If they press 3, call a function that prints IN FUNCTION 3.
# If they enter ‘q’ or 0 (your choice), quit.
# Else, print ERROR.
    quest3 = int(input("Put a user input: "))
    while(quest3 != "q" or quest3 != 0):
        if(quest3 == 1):
            print("IN FUNCTION 1")
        elif(quest3 == 2):
            print("IN FUNCTION 2")
        elif(quest3 == 3):
            print("IN FUNCTION 3")
        else:
            print("ERROR")
        break
#######################################################################
if __name__ == '__main__':
    main()