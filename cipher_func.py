__author__ = 'Anindita'
import string
import sys

#Caesar Cipher encryption and decryption
def caesar_encrypt(plaintext,key):

        answer_e=''
        for value in plaintext:
            value=(ord(value)+int(key))
            if value-int(key)==32:
                value=32
            elif value>ord('z'):
                value-=26
            elif value<ord('a'):
                value+=26
            value=chr(value)
            answer_e = answer_e +value
        print(answer_e)
        return(answer_e)





def caesar_decrypt(ciphertext,key):
        answer_d=''
        for value in ciphertext:
            value=(ord(value)-int(key))
            if value + int(key)==32:
                value = 32
            elif value > ord('z'):
                value-=26
            elif value < ord('a'):                
                value+=26
            value=chr(value)
            answer_d=answer_d+value
        return (answer_d)


def vigenere_encrypt(plaintext, key):
    keylength = len(key)
    key_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_int[i % keylength]) % 26
        ciphertext += chr(value + 65)
    return (ciphertext)

def vigenere_decipher(ciphertext,key):
    keylength = len(key)
    key_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_int[i % keylength]) % 26
        plaintext += chr(value + 65)
    return (plaintext)


