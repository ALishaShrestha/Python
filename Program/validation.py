# validaiton.py module is created for validation of binary and decimal number.
# Auther: Alisha Shrestha, 10 September, 2020

# creating funcition for binary validation.
def binary_validation(input_bin):
    if (input_bin == ""): # it check empty value
        return [True,"Error !!! Please enter the value."]

    # try and except is used to handle the exception
    try:
        check = int(input_bin) # it check whether the value is integer type or not
    except:
        return [True,"Error !!! Accepts integer value only."]

    if (int(input_bin) < 0): # it check whether the value is less than zero or not
        return [True, "Please enter positive value."]
    else:
        for a in input_bin: 
            if (int(a) not in [0,1]): # it check the input value is 0 and 1 only
                return [True,"Invalid input!!! Enter either 0 or 1."]
    
    if (len(input_bin)> 8): # it check the length of the input value
        return[True, "Invalid input!!! Enter 8 bit binary number"]
    return [False]
        
def decimal_validation(input_dec):
    if (input_dec == ""): # it check empty value
        return[True,"Error !!! Please enter the value."]
    
    # try and except is used to handle the exception
    try:
        check = int(input_dec) # it check whether the value is integer type or not
    except:
        return [True,"Error !!! Accepts integer value only."]

    # it check the value whether it is not less than 0 and not more than 255
    if (int(input_dec) < 0 or int(input_dec) > 255):
        return [True, "Please enter value more than zero and less than 255"]
    return [False]
