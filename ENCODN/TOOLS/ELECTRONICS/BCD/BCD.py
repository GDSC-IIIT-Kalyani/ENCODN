
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
        print("The entered value is incorrect!!!")
        print("Unable to convert String to Decimal")
    return cipher[::-1]

# Input : BCD string
# Output: Decimal string
def decrypt(cipher):
    decipher = 0
    # Decryption starting from LSB
    cipher = cipher[::-1]
    for i in range(len(cipher)):
        bit = int(cipher[i])
        bit_value = bit * (2**i)
        decipher += bit_value
    return str(decipher)
