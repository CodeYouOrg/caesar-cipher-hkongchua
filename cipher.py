# Function to encrypt text using a Caesar cipher with a right shift of 5
def caesar_cipher(text):

    # Define the shift amount
    shift = 5

    # Create an empty list to hold the encrypted characters
    encrypted_text = []

    # Loop through each character in the input text
    for char in text:

        # Check if the character is an uppercase letter
        if char.isupper():

            # Find the position in the alphabet (0-25) and apply the shift
            new_char = chr((ord(char) - 65 + shift) % 26 + 65)

            # Append the new character to the encrypted_text list
            encrypted_text.append(new_char)

        # Check if the character is a lowercase letter
        elif char.islower():

            # Find the position in the alphabet (0-25) and apply the shift
            new_char = chr((ord(char) - 97 + shift) % 26 + 97)

            # Append the new character to the encrypted_text list
            encrypted_text.append(new_char)
        else:
            
	    # If the character is not a letter, leave it unchanged
            encrypted_text.append(char)

    # Join the list of characters into a single string and return it
    return ''.join(encrypted_text)

# Ask the user for a plain text sentence
plain_text = input("Please enter a sentence: ")

# Encrypt the plain text using the caesar_cipher function
encrypted_text = caesar_cipher(plain_text)

# Print the encrypted text
print("The encrypted sentence is:", encrypted_text)
