
#!/usr/bin/python
import time
import argparse

print '++++++++Just a So DAMN stupid Ecryption script!!+++++++++\n\n\n\n'
print "Example: encrypto.py e 'My message is this' keyIsThis \n\n"



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

def Main():
	parser = argparse.ArgumentParser()
	parser.add_argument("encCheck", help="e to encode d to decode", type=str)
	parser.add_argument("encText", help="enter the string after e or d", type=str)
	parser.add_argument("encKey", help="enter the key after text", type=str)
	args = parser.parse_args()

	check = args.encCheck
	msg = args.encText
	key = args.encKey

	if(check == "e"):
		encrypt(msg,key)
	elif(check == "d"):
		decrypt(msg,key)
	else:
		print "Example: encrypto.py e 'My message is this' keyIsThis"

if __name__ == '__main__':
	Main()

















