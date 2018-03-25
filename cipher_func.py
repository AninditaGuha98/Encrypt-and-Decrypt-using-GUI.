__author__ = 'Anindita'
import string
import sys

#Caesar Cipher encryption and decryption
def caesar_encrypt(plaintext,key):
        #plaintext=raw_input("Insert your text").lower()

        #key=int(raw_input("Enter the key value:"))
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


#One time pad encryption and decryption
otp= string.ascii_lowercase
one_time_pad = list(otp)

def OTP_encrypt(msg, key):
    ciphertext = ''
    for idx, char in enumerate(msg):
        char_ID = otp.index(char)
        key_ID= one_time_pad.index(key[idx])

        cipher = (key_ID + char_ID) % len(one_time_pad)
        ciphertext += otp[cipher]

    return ciphertext


def OTP_decrypt(ciphertext, key):
    if ciphertext == '' or key == '':
        return ''
    char_ID = otp.index(ciphertext[0])
    key_ID = one_time_pad.index(key[0])

    cipher = (char_ID - key_ID) % len(one_time_pad)
    char = otp[cipher]

    return char + decrypt(ciphertext[1:], key[1:])