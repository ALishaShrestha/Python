# asinput.py module is created to ask user input and display the output of binary and decimal additon
# it imports forconversion.py, validaiton.py and foradder.py module to complete the program
# Auther: Alisha Shrestha, 10 September, 2020

from forconversion import *
from validation import *
from foradder import *

# Creating function to ask user input and it display the output of binary and decimal addition.
def binary_decimal_input():
    main = False
    input_check = False
    check_input_no1 = False
    check_input_no2 = False
    
    # while loop is created to check the condition untill user input correct value        
    while (not main):
        # it ask user to input value
        input_option = input("Enter [B/b] for binary number and [D/d] for decimal number : ")
        print()
        # lower() method is used to return the lowercased string 
        # it converts all uppercase character to lower case 
        if (input_option.lower() == "b"):
            while (not input_check):
                while (not check_input_no1):
                    # it ask user to input value
                    first_bin = input("Enter first binary number : ")
                    if (binary_validation(first_bin)[0]): # [0] value check the index
                        print()
                        print(binary_validation(first_bin)[1]) # [1] value check the index 
                        print()
                    else:
                        print()
                        check_input_no1 = True
                        n = 8 - len(first_bin) # check the length of input value
                        first_bin = ("0"*n+first_bin) 
                                
                while (not check_input_no2):
                    # it ask user to input value
                    second_bin = input("Enter second binary number : ")
                    if (binary_validation(second_bin)[0]):# [0] value check the index
                        print()
                        print(binary_validation(second_bin)[1])# [1] value check the index
                        print()
                    else:
                        print()
                        check_input_no2 = True
                        n = 8 - len(second_bin) # check the length of input value
                        second_bin = ("0"*n+second_bin)
                                
                a = bin_to_dec(int(first_bin))
                b = bin_to_dec(int(second_bin))
                # it check the value whether it is not more than 255
                if (a + b > 255):
                    print("Error !!! Exceeded the limits of 11111111.")
                    check_input_no1 = False
                    check_input_no2 = False
                else:
                    input_check =True
                    main = True
            
            c = first_bin
            d = second_bin
            print("             Binary Addition")
            print("              ---------------------")
            print("1st  no      ",c.zfill(8)) # z.fill() method is used to fill 0 value 
            print("2nd no      ",d.zfill(8))
            print("              ---------------------")
            print("Output      ",adder_gate(c,d)) # it add two binary number
            print()

            e = bin_to_dec(int(first_bin)) # it convert binary no into decimal no
            f = bin_to_dec(int(second_bin)) # it convert binary no into decimal no
            print("             Decimal Addition")
            print("              -----------------------")
            print("1st no              ",e)
            print("2nd no             ",f)
            print("              -----------------------")
            print("Output             ",e + f)
                
        # lower() method is used to return the lowercased string 
        # it converts all uppercase character to lower case  
        elif (input_option.lower() == "d"):
            # while loop is created to check the condition untill user input correct value        
            while (not input_check):
                while (not check_input_no1):
                    # it ask user to input value
                    first_dec = input("Enter first decimal number : ")
                    if (decimal_validation(first_dec)[0]): # [0] value check the index
                        print()
                        print(decimal_validation(first_dec)[1]) # [1] value check the index
                        print()
                    else:
                        print()
                        check_input_no1 = True

                while (not check_input_no2):
                    # it ask user to input value
                    second_dec = input("Enter second decimal number : ")
                    if (decimal_validation(second_dec)[0]): # [0] value check the index
                        print()
                        print(decimal_validation(second_dec)[1]) # [1] value check the index
                        print()
                    else:
                        print()
                        check_input_no2 = True
                                        
                a = int(first_dec)
                b = int(second_dec)
                if (a + b > 255):
                    # it check the value whether it is and not more than 255
                    print("Error !!! Exceeded the limits of 255.")
                    check_input_no1 = False
                    check_input_no2 = False     
                else:
                    input_check = True
                    main = True
            
            c = int(first_dec)
            d = int(second_dec)
            print("             Decimal Addition")
            print("              -----------------------")
            print("1st no              ",c)
            print("2nd no             ",d)
            print("              -----------------------")
            print("Output             ",c + d)
            print()
            
            e = dec_to_bin(int(first_dec)) # it convert decimal no into binary no
            f = dec_to_bin(int(second_dec)) # it convert decimal no into binary no
            print("             Binary Addition")
            print("              ---------------------")
            print("1st  no      ",e)
            print("2nd no      ",f)
            print("              ---------------------")
            print("Output      ",adder_gate(e,f)) # it add two binary number
                    
        else:
            print("Invalid Input.")
            print("Enter Either [B/b] or [D/d].")
            print()
            
##binary_decimal_input()

        
        
