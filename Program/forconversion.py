# forconversion.py mpdule is created to covert binary and decimal number
# Auther: Alisha Shrestha, 10 September, 2020

# Creating function to convert binary into decimal
def bin_to_dec(value):
    dec_no = 0
    i = 0
    while (value > 0):
        last_no = value % 10
        dec_no += last_no * (2 ** i)
        i += 1
        value = int(value/10)
    return dec_no
##print(bin_to_dec(11111111))

# Creating function to convert decimal into binary
def dec_to_bin(value):
    list_of_eightbit = ["0","0","0","0","0","0","0","0"]
    index_ = 7
    while (value > 0):
        b = value % 2
        list_of_eightbit[index_] = str(b)
        index_ -= 1
        value = int(value/2)
    return "".join(list_of_eightbit)
##print(dec_to_bin(12))
##print(dec_to_bin(176))
    
