#!/usr/bin/python
import time;

print '++++++++Just a So DAMN stupid Ecryption script!!+++++++++\n\n\n\n'

flag = input('Please Tell This Script for your privacy sake that what do you wanna do??\n\nEncrypt(1) OR Decrypt(2) :')


def encrypt(enc,key):
    e = list(enc.encode('base64','strict').rstrip('\n'))
    k = list(key.encode('base64','strict').rstrip('\n'))
    f = [' ']*len(e)
    i = 0
    j = 0
    while(i<len(e)):
        f[i] = e[i]+k[j]
        i = i + 1
        j = j + 1
        if(j>=len(k)):
            j = 0
    enc = ''.join(f)
    print 'The Encrypted message is :',enc +'\n'
    print '+'*80
    print '+'*80


def decrypt(dec,key):
    k = key.encode('base64','strict').rstrip('\n')
    d = list(dec)
    f = d[::2]
    n = d[1::2]
    key = ''.join(n)
    dec = ''.join(f)
    a = key[0:len(k)]
    if(k==a):
        print 'The decrypted text is :'+ dec.decode('base64','strict') + '\n\n Bye babe, Will see you soon!!'
    else:
        print 'Please provide a valid key Sweetheart'

if(flag == 1):
    print '+'*80
    print '+'*80+'\n'
    enc = raw_input('^_^ Please enter your message :')
    key = raw_input('^_^ Your key please :')
    print '\n'
    print '+'*80
    print '+'*80
    print '\n\n+++++    Holy Crap!!!!!!!!!!!!   +++++'
    time.sleep(2)
    print '\n\n+++++    You wanna encrypt such a long message   +++++\n\n'
    print '+'*80
    print '+++++    Wait you devil  +++++'
    print '+'*80+'\n'
    time.sleep(2)
    encrypt(enc,key)


elif(flag == 2):
    print '+'*80
    print '+'*80
    dec = raw_input('Please enter the Encrypted text :')
    key = raw_input('Please enter your key :')
    print '+'*80
    print '+'*80
    print '\n\n+++++    Are you kidding me!!!!  +++++'
    print '\n\n+++++     Why the Hell Your wanna decrypt this message?   +++++\n\n'
    print '+'*80
    print '+++++     Wait while I decrypt    +++++\n\n'
    print '+'*80
    decrypt(dec,key)


else:
    print 'Please Provide a Valid input either 1 or 2. IDIOT!!'
