# foradder.py module is created to add the two binary number
# It import gates module to operate logical gates

from gates import *

# Creating adder gate function to add two number
def adder_gate(bin_no1,bin_no2):
    carry = 0 # initial carry is 0 
    list_of_eightbit = ["0","0","0","0","0","0","0","0"] # Creating the list of 8 bits

    # Creating the iterator of range start, stop and step
    for a in range (7,-1,-1):
        upper_bit =int(bin_no1[a]) # upper bit value going through iteration
        lower_bit = int(bin_no2[a]) # lower bit value going through iteration     

        xor_ = xor_gate(upper_bit, lower_bit) # call xor_gate function
        nand_ = nand_gate(xor_,carry) # call nand_gate function
        or_ = or_gate(xor_,carry) # call or_gate function
        sum_of_bit = and_gate(or_,nand_) # call and_gate function
        
        list_of_eightbit[a] = str(sum_of_bit)

        and_no1 = and_gate(upper_bit, lower_bit) 
        and_no2 = and_gate(xor_, carry)
        carry = not_gate(nor_gate(and_no1, and_no2))

    # return 8 bit binary number after going through logical circuit     
    return "".join(list_of_eightbit) 

##print(adder_gate("00000001","00000001"))
        
        

        
    
