#Vejay Persaud
#Notes: 
#add 3 to the element, then use the modulo operator to find the proper shifted value. 
#For example, if our original element is 9 and we add 3, 12 can not be properly encoded. 12 will then be encoded as 3 using the modulo operator.
#Thus 9 shift +3 is 3.
        
def encode(password):
    #Creates the empty encoded password
    encoded_pass = ''
    
    #Takes the uncoded password from the function parameter and forces it to be a string no matter the input
    string_password = str(password)
    
     
    
    for element in string_password:
        
        #force each string number of the password to be an integer type.
        #Then use the addition and modulo to implement the shift and encode operations respectively.
        temp = str((int(element) + 3) % 9)
        
        #tack on the coded numbers to the string
        encoded_pass += temp
        
    print(encoded_pass)