# Vejay Persaud
# Notes: 
# add 3 to the element, then use the modulo operator to find the proper shifted value. 
# For example, if our original element is 9 and we add 3, 12 can not be properly encoded. 12 will then be encoded as 3 using the modulo operator.
# Thus 9 shift +3 is 3.
        
def encode(password):
    # Creates the empty encoded password
    encoded_pass = ''
    
    # Takes the uncoded password from the function parameter and forces it to be a string no matter the input
    string_password = str(password)
    
    for element in string_password:
        
        # force each string number of the password to be an integer type.
        # Then use the addition and modulo to implement the shift and encode operations respectively.
        temp = str((int(element) + 3) % 9)
        
        # tack on the coded numbers to the string
        encoded_pass += temp
        
    return encoded_pass
    
def decode(encoded_password):
    # Creates the empty decoded password
    decoded_password = ''
    
    for element in encoded_password:
        # force each string number of the encoded password to be an integer type.
        # Then use the subtraction and modulo to implement the shift and decode operations respectively.
        temp = str((int(element) - 3) % 10)
        
        # tack on the decoded numbers to the string
        decoded_password += temp
        
    return decoded_password


def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    option = int(input("Please enter an option: "))
    return option
 
# loop will keep asking user for passwords to encode and decode until option 3 is chosen    
while True:
    # saves the option chosen when the menu function is called and the menu prints are displayed
    option = menu() 
    
    # encode the user's password
    if option == 1:
        user_password = input("Please enter your password to encode: ")
        encoded_password = encode(user_password)
        print("Your password has been encoded and stored!")
    
    # decodes the user's password
    if option == 2:
        decoded_password = decode(encoded_password)
        print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.')
        
    # breaks out of the while loop and reaches the end of the file    
    if option == 3:
        break
