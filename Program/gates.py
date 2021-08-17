# gates.py module is created for adding two gates value i.e. upper and lower gates
# In this module "x" is consider as upper gates and "y" as lower gates which use
# bitwise operators
# Auther: Alisha Shrestha, 10 September, 2020

# Creating and gate using bitwise operators
def and_gate(x, y):
    return x&y  # return keyword is used return the given value

# Creating or gate using bitwise operators
def or_gate(x, y):
    return x|y

# Creating xor gate using bitwise operator
def xor_gate(x, y):
    return x^y

# Creating not gate using bitwise operator
def not_gate(x):
    return (~x) + 2

# Creating nand gate
def nand_gate(x,y):
    return not_gate(and_gate(x,y))

#Creating nor gate
def nor_gate(x,y):
    return not_gate(or_gate(x,y))
