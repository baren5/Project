#encrypt
def encrypt(text, key=0):
    if not isinstance(text, str):
        print("Should be a string")
    if not isinstance(key, int):
        print("Should be a integer")
    return "".join([chr(ord(i) + key) for i in text])


#decrypt
def decrypt(text, key=0):
    if not isinstance(text, str):
       print("Should be a string")
    if not isinstance(key, int):
        print("Should be a integer")
    return "".join([chr(ord(i) - key) for i in text])


# output = encrypt("baren",123)
# print(output)

# output1 = decrypt("ÝÜíàé",123)
# print(output1)