# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 17:44:45 2023

@author: wilks
"""

#The last bit is a parity-check bit.
x1 = [[0,0,1,1,0,1,1],
[1,1,1,0,1,1,0],
[1,0,0,1,0,1,1],
[1,1,0,0,1,1,1],
[1,1,1,1,1,1,0]]

#Encode these messages with triple repetition.
triple_enc = [[1, 1, 0, 0],
[0, 0, 1, 1],
[0, 1, 1, 0]]

#Message encoded with triple repetition that passed through a binary symmetric channel. Decode these.
triple_dec = [[0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
[0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
[1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1],
[0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1]]

test_message = [1, 1, 0, 1]
def encode_partity_check(message):
    sum = 0
    for i in message:
        sum += i
    if(sum % 2 == 1):
        message.append(1)
    else:
        message.append(0)
           
        
def detect_parity_check(codeword):
    loc = len(codeword) - 1
    if (codeword[loc] == 1):
        return True
    else:
        return False
def decode_partity_check(codeword):
    decoded = []
    for i in range (len(codeword) - 1):
        decoded.append(codeword[i])
    return decoded


print("\n\nTASK 1\n---------------------")
for i in range(len(x1)):
    print(detect_parity_check(x1[i]))
    print(decode_partity_check(x1[i]))

print("\n\nTASK 2")
print("---------------------\nTriple Encoding\n")   
for i in triple_enc:
    temp = []
    print("Before:", i)
    for j in range(3):
        encode_partity_check(i)
        for k in i:
            temp.append(k)
        i = decode_partity_check(i)
    print("After:", temp)

print("\n---------------------\nTriple Decoding\n")
    
for i in triple_dec:
    aVec = []
    bVec = []
    cVec = []
    for j in range(len(i)):
        if (j < 6):
            aVec.append(i[j])
        elif (j < 12):
            bVec.append(i[j])
        elif (j < len(i)):
            cVec.append(i[j])
    # print("\nA:", aVec)
    # print("\nB:", bVec)
    # print("\nC:", cVec)
    temp = []
    for j in range(len(aVec)):
        if aVec[j] == bVec[j]:
            temp.append(aVec[j])
        elif aVec[j] == cVec[j]:
            temp.append(aVec[j])
        elif bVec[j] == cVec[j]:
            temp.append(bVec[j])
    print("Solution:", temp)

        
