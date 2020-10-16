import hashlib
import binascii
import os


def hash_string(input_string):                            #  hashing system
    """Hash a string."""
    salt = hashlib.sha256(os.urandom(30)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', input_string.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


def verify_hash(hashed_string, user_input):                # Verify Hashing
    """Verify hash string"""
    salt = hashed_string[:64]
    hashed_string = hashed_string[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  user_input.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == hashed_string



# inp=hash_string('hi')
# print(inp)

# print(verify_hash(inp,'ashi'))