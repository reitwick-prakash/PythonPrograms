

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import binascii


def rsa_enc_public(inputblock, keyPair):
    pubKey = keyPair.publickey()

#    msg = b'A message for encryption'
    encryptor = PKCS1_v1_5.new(pubKey)  #The variable pubKey was derived from the keyPair variable in the above code cell.
    encrypted = encryptor.encrypt(inputblock)
#    print("Encrypted:", binascii.hexlify(encrypted))
    return encrypted

def rsa_dec_private(cipherblock, keyPair):
    decryptor = PKCS1_v1_5.new(keyPair)
    decrypted = decryptor.decrypt(cipherblock, None)
#    print('Decrypted:', decrypted)
    
    return decrypted
#
#
#    keyPair = RSA.generate(2048)
#    ciphertext=rsa_enc_public(b'BlahBlah', keyPair)
#    plaintext=rsa_dec_private(ciphertext,keyPair)


    
