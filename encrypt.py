import gost_crypto

def encrypt(message, key):
    encryptor = gost_crypto.Crypt(key)
    list_of_chars= [char for char in message] 
    encrypted_list_of_chars=[]

    for i in list_of_chars:


        encrypted_list_of_chars.append(str(encryptor.encrypt_i64(ord(i))))
    encrypted_message=''.join(encrypted_list_of_chars)
    return encrypted_message

