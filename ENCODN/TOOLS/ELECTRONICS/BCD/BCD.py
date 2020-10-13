import re

# Converts string of decimals to a BCD string
def encrypt(string):
    cipher = ''
    try:
        dec = int(string)
        while dec != 0:
            bit = dec % 2
            cipher += str(bit)
            dec //= 2
    except ValueError:
        return "The entered value is incorrect!!!"
    return cipher[::-1]

# Input : BCD string
# Output: Decimal string
def decrypt(cipher):
    decipher = 0
    try:
        # Check if cipher is a binary string
        char_Re = re.compile(r'[^0-1.]')
        is_binary = not bool(char_Re.search(cipher))
        if is_binary:
            # Decryption starting from LSB
            cipher = cipher[::-1]
            for i in range(len(cipher)):
                bit = int(cipher[i])
                bit_value = bit * (2**i)
                decipher += bit_value
        else:
            raise ValueError
    except ValueError:
        return "The entered value is incorrect!!!"
    return str(decipher)
