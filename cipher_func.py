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

    return char + OTP_decrypt(ciphertext[1:], key[1:])

def matrix(key):
	matrix=[]
	for e in key.upper():
		if e not in matrix:
			matrix.append(e)
	alphabet="ABCDEFGHIKLMNOPQRSTUVWXYZ"

	for e in alphabet:
		if e not in matrix:
			matrix.append(e)

	#initialize a new list. Is there any elegant way to do that?
	matrix_group=[]
	for e in range(5):
		matrix_group.append('')

	#Break it into 5*5
	matrix_group[0]=matrix[0:5]
	matrix_group[1]=matrix[5:10]
	matrix_group[2]=matrix[10:15]
	matrix_group[3]=matrix[15:20]
	matrix_group[4]=matrix[20:25]
	return matrix_group

def message_to_digraphs(message_original):
	#Change it to Array. Because I want used insert() method
	message=[]
	for e in message_original:
		message.append(e)

	#Delet space
	for unused in range(len(message)):
		if " " in message:
			message.remove(" ")

	#If both letters are the same, add an "X" after the first letter.
	i=0
	for e in range(len(message)/2):
		if message[i]==message[i+1]:
			message.insert(i+1,'X')
		i=i+2

	#If it is odd digit, add an "X" at the end
	if len(message)%2==1:
		message.append("X")
	#Grouping
	i=0
	new=[]
	for x in xrange(1,len(message)/2+1):
		new.append(message[i:i+2])
		i=i+2
	return new

def find_position(key_matrix,letter):
	x=y=0
	for i in range(5):
		for j in range(5):
			if key_matrix[i][j]==letter:
				x=i
				y=j

	return x,y

def encrypt(message):
	message=message_to_digraphs(message)
	key_matrix=matrix(key)
	cipher=[]
	for e in message:
		p1,q1=find_position(key_matrix,e[0])
		p2,q2=find_position(key_matrix,e[1])
		if p1==p2:
			if q1==4:
				q1=-1
			if q2==4:
				q2=-1
			cipher.append(key_matrix[p1][q1+1])
			cipher.append(key_matrix[p1][q2+1])
		elif q1==q2:
			if p1==4:
				p1=-1;
			if p2==4:
				p2=-1;
			cipher.append(key_matrix[p1+1][q1])
			cipher.append(key_matrix[p2+1][q2])
		else:
			cipher.append(key_matrix[p1][q2])
			cipher.append(key_matrix[p2][q1])
	return cipher

def cipher_to_digraphs(cipher):
	i=0
	new=[]
	for x in range(len(cipher)/2):
		new.append(cipher[i:i+2])
		i=i+2
	return new