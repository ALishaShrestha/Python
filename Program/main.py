# main.py module controls all the module to complete the conversion of binary and decimal number
# It import the asInput module to perform user interaction.
# Auther: Alisha Shrestha, 10 September, 2020

from asinput import *

# Creating the function to make its user experience better
def main_function():
    # Making a design of 8 bit adder
    print( "________________________________~ Python ~  ___________________________________")
    print(":                                                                                                                                                                      :")
    print(":     ___          ____      ______   ______                _             ____          ____         _____    ____         :")
    print(":   /        \        ||        \         ||              ||                    /   \           |         \       |         \        |             |         \        :")
    print(":  |          |       ||         |       ||              ||                   /      \         |           \      |           \      |            |           |      :")
    print(":   \         /       ||         /        ||              ||                 /         \        |            \     |            \    |             |           |     :")
    print(":     ------         ||-------         ||              ||                /_ ____\       |             )   |             )   |--------    | ___  /      :")
    print(":   /         \       ||         \        ||             ||               /               \      |            /    |            /    |             |          \      :")
    print(":   |          |      ||         |       ||              ||             /                  \    |           /      |           /     |             |           \     :")
    print(":    \ ___ /       ||____/   __||__          ||           /                      \  |____ /       |____ /      |____    |            \    :" )
    print(":                                                                                                                                                                       :")
    print(" _____________________________~~Alisha Shrestha ~~_______________________________")
    print()
    binary_decimal_input() # calling funciton 
    check = False   # initializing False boolean value
    # while loop is created to check the condition untill user input correct value
    while(not check): 
        print()
        # it ask user to input value
        exit_input = input("Do you want to continue [Yes/No] : ")
        print()
        # lower() method is used to return the lowercased string 
        # it converts all uppercase character to lower case 
        if (exit_input.lower() == "yes"): 
            binary_decimal_input()
        elif (exit_input.lower() == "no"):
            print()
            print("Thank you for using this program.")
            print()
            check = True
        else:
            print("Error !!! , Please enter Yes to run the program or No to exit program.")

main_function()
            
        
    
