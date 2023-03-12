
@authors: Jorge Roa | Carmen Garro


def caesar_cipher(message, position, action='encrypted'):
    #Define the alphabet to be used
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    #Initialize empty lists for the encrypted and decrypted message
    encrypt, decrypt = [], []
    
    #Loop through each character in the message
    for letter in message:
        #Check if the character is in the alphabet
        if letter.lower() in alphabet:
            #Calculate the new position of the character after shifting by the given position
            new_position = (alphabet.find(letter.lower()) + position) % 26
            #If the character is uppercase, append the shifted uppercase character to the encrypt list
            if letter.isupper():
                encrypt.append(alphabet[new_position].upper())
            #If the character is lowercase, append the shifted lowercase character to the encrypt list
            else:
                encrypt.append(alphabet[new_position])
        #If the character is not in the alphabet, append it to the encrypt list as is
        else:
            encrypt.append(letter)
    
    #Loop through each character in the message
    for letter in message:
        #Check if the character is in the alphabet
        if letter.lower() in alphabet:
            # Calculate the original position of the character before shifting by the given position
            new_position = (alphabet.find(letter.lower()) - position) % 26
            #If the character is uppercase, append the original uppercase character to the decrypt list
            if letter.isupper():
                decrypt.append(alphabet[new_position].upper())
            #If the character is lowercase, append the original lowercase character to the decrypt list
            else:
                decrypt.append(alphabet[new_position])
        #If the character is not in the alphabet, append it to the decrypt list as is
        else:
            decrypt.append(letter)
    
    #Determine whether to return the encrypted or decrypted message
    if action == 'encrypted':
        output = ''.join(encrypt)
    elif action == 'decrypted':
        output = ''.join(decrypt)
    else:
        output = 'Invalid action specified.'
    
    #Return the output
    return output

#Example 1
encrypted = caesar_cipher("THE EAGLE IS IN PLAY; MEET AT JOE'S", 3, action="encrypted")
print("Encrypted message: ", encrypted)
decrypted = caesar_cipher(encrypted[:], 3, action="decrypted")
print("Decrypted message: ", decrypted)

#Example 2

encrypted = caesar_cipher("Ya se la saben, banda! Carteras y celulares en mano", 5, action="encrypted")
print("Encrypted message: ", encrypted)
decrypted = caesar_cipher(encrypted[:], 5, action="decrypted")
print("Decrypted message: ", decrypted)



