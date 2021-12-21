#!/usr/bin/python

import sys
import hashlib
import caesarCipher2
from caesarCipher2 import Caesar2

#print ('Number of arguments:', len(sys.argv), 'arguments.')
#print ('Argument List:', str(sys.argv))

parameters = sys.argv
#print (parameters)
#print (len(parameters))

#for x in range(len(parameters)):
#    print (parameters[x])
if parameters[1] == '-h' or parameters[1] == '-help' or parameters[1] == 'help':
    print ("usage: -'encrypt method', -'encrypt or decrypt', key, -'File or sentence'")
    print ("method: -C         = Caesar cypher")
    print ("encrypt/ decrypt   = -e or -d")
    print ("key                 = number")
    print ("-s                  = sentence to decrypt followed by sentence")
    print()
    print ( "Example:")
    print ('cryptfriend -C -e 14 -s "{}"'.format("Hello World"))
    print ()
    print ('Output:')
    print()
    print('encrypting with keynumber 14.......')
    print()
    print('Sentence to encrypt: "Hello World"')
    print()
    print ('encrypted sentence(between brackets): "Vszz}.e}!zr"')

if parameters[1] == "-C":
       
    if parameters[2]== "-e":
        mode = 'encrypt'
    else:
        mode = 'decrypt'
        
    key = int(parameters[3])
            
    if parameters[4] == "-s":
        sentence = parameters[5]
        print()
        print ('{}ing with keynumber {}.......'.format(mode,key))
        print()
        print ('Sentence to {}: "{}"'.format(mode, sentence))
        print ("")
        es = Caesar2(sentence, mode, key)   
        
    else:
        print ("Something went wrong.")
        

if parameters[1] != '-h' and parameters[1] != '-help' and parameters[1] != 'help':
    print ('{}ed sentence(between brackets): "{}"'.format(mode,es))
