__author__ = 'Anindita'

#Caesar Cipher encryption and decryption
def caesar_encrypt(plaintext):
        #plaintext=raw_input("Insert your text").lower()

        #key=int(raw_input("Enter the key value:"))
        answer_e=''
        for value in plaintext:
            value=(ord(value)+3)
            if value-3==32:
                value=32
            elif value>ord('z'):
                value-=26
            elif value<ord('a'):
                value+=26
            value=chr(value)
            answer_e = answer_e +value
        return(answer_e)

def caesar_decrypt():
        ciphertext=raw_input("Enter the cipher text").lower()
        key_d=int(raw_input("Enter the key value:"))
        answer_d=''
        for value in ciphertext:
            value=(ord(value)-key_d)
            if value + key_d==32:
                value = 32
            elif value > ord('z'):
                value-=26
            elif value < ord('a'):                
                value+=26
            value=chr(value)
            answer_d=answer_d+value
        print(answer_d)

#