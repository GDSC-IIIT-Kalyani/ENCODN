"""
Information on the Baconian Cipher can be found at:
https://www.dcode.fr/bacon-cipher

BACON.py
Written by: MrLukeKR
Updated: 17/10/2020
"""

letter_1 = 'A'
letter_2 = 'B'

def encrypt(plaintext: str):
    """
    Encrypts a plaintext string using the Bacnoian cipher, using 2 distinct
    letters.
    """

    # Check if the encrpytion letters are different
    if (letter_1 == letter_2):
        print("The two letters used for encryption must be different!")
        raise ValueError

    # Convert plaintext to upper case
    plaintext = plaintext.upper()

    # Initialise the ciphertext string to the empty string
    ciphertext = ""

    # Iterate over every letter in the plaintext string
    for index, letter in enumerate(plaintext):
        # If there is more than one cipher word, add a space between them
        if index > 0:
            ciphertext += " "

        # Get alphabetical value of letter by subtracting the ASCII code value
        # for capital A
        letter_value = ord(letter) - ord('A')

        # Get binary representation of the alphabetical position of the letter
        # and pad if necessary to ensure the binary string is 5 bits long
        letter_binary = bin(letter_value)[2:].zfill(5)

        # Replace any zeros with the first encryption letter and any ones with
        # the second encryption letter
        cipher_word = letter_binary.replace('0', letter_1)
        cipher_word = cipher_word.replace('1', letter_2)

        # Add the cipher word to the total encrypted ciphertext
        ciphertext += cipher_word

    return ciphertext


def decrypt(ciphertext: str):
    """
    Decrypts a ciphertext string using the Rozier cipher and a constant key.
    Optionally, the function can accept a different key as a parameter.
    """

    # Convert ciphertext to upper case
    ciphertext = ciphertext.upper()

    # Split the ciphertext into its individual words
    cipher_words = str.split(ciphertext, ' ')

    # Initialise the plaintext string to the empty string
    plaintext = ""

    # Iterate over every word in the ciphertext string
    for index, word in enumerate(cipher_words):

        # Convert the cipher word to a binary string
        word_binary = word.replace(letter_1, '0')
        word_binary = word_binary.replace(letter_2, '1')
        word_binary = '0b' + word_binary

        # Convert binary string to its ASCII code representation
        letter_value = int(word_binary, 2) + ord('A')

        # Convert ASCII code value to character
        plain_letter = chr(letter_value)

        # Add the character to the total plaintext string
        plaintext += plain_letter

    return plaintext
