"""
Information on the Rozier Cipher can be found at:
https://www.dcode.fr/rozier-cipher

ROZIER.py
Written by: MrLukeKR
Updated: 16/10/2020
"""

# The Rozier cipher needs a string based key, which can be constant for ease
# or changed for each message, for better security
constant_key = "DCODE"

def encrypt(plaintext: str, key: str=constant_key):
    """
    Encrypts a plaintext string using the Rozier cipher and a constant key.
    Optionally, the function can accept a different key as a parameter.
    """

    # Convert plaintext to upper case
    plaintext = plaintext.upper()

    # Initialise the ciphertext string to the empty string
    ciphertext = ""

    # Iterate over every letter in the plaintext string
    for index, letter in enumerate(plaintext):
        # Get the first and second letters of the key at index of letter,
        # using modulus to allow for a key to be repeated
        first_key = key[index % len(key)]
        second_key = key[(index + 1) % len(key)]

        # Get the position in the alphabet of the current plaintext letter.
        # Negating the ASCII value of capital A allows us to convert from
        # an ASCII code to alphabet position.
        letter_position = ord(letter) - ord('A')

        # Convert the first and second key values to ASCII codes
        first_key_value = ord(first_key)
        second_key_value = ord(second_key)

        # Use the first and second key ASCII codes to determine the distance
        # between the two letters. Negative values indicate that the ciphertext
        # letter moves to the right of the current letter and positive values
        # indicate a move to the left
        key_distance = second_key_value - first_key_value

        # Calculate the ciphertext letter by adding the original plaintext
        # letter to the key distance derived from the two letters from the key.
        # Modulus is applied to this to keep the letter within the bounds of
        # the alphabet (numbers and special characters are not supported).
        # This is added to the ASCII code for capital A to convert from
        # alphabet space back into an ASCII code
        cipher_letter_value = ord('A') + ((letter_position + key_distance) % 26)

        # Convert the ASCII code to a character
        cipher_letter = chr(cipher_letter_value)

        # Add the character to the total ciphertext string
        ciphertext += cipher_letter

    return ciphertext


def decrypt(ciphertext: str, key: str=constant_key):
    """
    Decrypts a ciphertext string using the Rozier cipher and a constant key.
    Optionally, the function can accept a different key as a parameter.
    """

    # Convert ciphertext to upper case
    ciphertext = ciphertext.upper()

    # Initialise the plaintext string to the empty string
    plaintext = ""

    # Iterate over every letter in the ciphertext string
    for index, letter in enumerate(ciphertext):
        # Get the first and second letters of the key at index of letter, using
        # modulus to allow for a key to be repeated
        first_key = key[index % len(key)]
        second_key = key[(index + 1) % len(key)]

        # Get the position in the alphabet of the current ciphertext letter.
        # Negating the ASCII value of capital A allows us to convert from
        # an ASCII code to alphabet position.
        letter_position = ord(letter) - ord('A')

        # Convert the first and second key values to ASCII codes
        first_key_value = ord(first_key)
        second_key_value = ord(second_key)

        # Use the first and second key ASCII codes to determine the distance
        # between the two letters. Negative values indicate that the plaintext
        # letter moves to the right of the current letter and positive values
        # indicate a move to the left
        key_distance = second_key_value - first_key_value

        # Calculate the plaintext letter by subtracting the key distance derived
        # from the two letters from the key, from the original ciphertext letter
        # position.
        # Modulus is applied to this to keep the letter within the bounds of
        # the alphabet (numbers and special characters are not supported).
        # This is added to the ASCII code for capital A to convert from
        # alphabet space back into an ASCII code
        plain_letter_value = ord('A') + ((letter_position - key_distance) % 26)

        # Convert the ASCII code to a character
        plain_letter = chr(plain_letter_value)

        # Add the character to the total plaintext string
        plaintext += plain_letter

    return plaintext
