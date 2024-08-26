import math
import os
import random
import re
import sys

def transformSentence(sentence):
    sentence.strip()
    res = ''
    ind = 0
    for x in sentence:
        if(ind==0):
            res+= x
            ind+=1
        elif(x == ' '):
            res += x
            ind+=1
        else:
            y = sentence[ind-1]
            if(y==' '):
                res+= x
                ind+=1
            elif(y.lower() < x.lower()):
                res += x.upper()
                ind+=1
            elif(y.lower()>x.lower()):
                res += x.lower()
                ind+=1
            else:
                res+= x
                ind+=1
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = transformSentence(sentence)

    fptr.write(result + '\n')

    fptr.close()