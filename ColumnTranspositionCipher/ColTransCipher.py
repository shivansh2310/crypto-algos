import math
def encryptMessage():
    #key=input ('Enter a key\n')
    #v=input ('Enter a value\n')

    key = "ZEBRAS"
    message = "HELLOWEWILLMEETTOMORROW"

    key1 = "orange"
    message1 = "defendtheeastwallofthecastle"

    col=len(key)
    if((len(message)%col)!=0):
        message+="x"*(len(key)-(len(message)%col))
    message=message.replace(' ', '')
    o=[]
    for i in key:
        o.append(i)
    h=[]
    for i in range(col):
        h.append(message[i:len(message):col])

    dic=dict(zip(o,h))
    so=sorted(dic.keys())

    emsg = ''.join(dic[i] for i in so)
    #         Addition emsg = odd elements +even elements
    count=0
    a=''
    b=''
    for i in emsg:
        count+=1
        if count%2==0:
            a+=i
        else:
            b+=i
    emsg=a+b
    print("Encrypted Message is : ",emsg)

def decryptMessage():
    #key=input ('Enter a key\n')
    #userval=input ('Enter the encrypted Message\n')

    key = "ZEBRAS"
    encryptedmsg = "LWIRWRLOMxEOOOLTEELTWMHE"

    encryptedmsg1 = "OLOWLITREWERLLTOWMMxHEEO"
    key1 = "orange"
    encryptedmsg2 = "feahldsoaxnalcxeeleedttfsehwtt"

    a = encryptedmsg[int(len(encryptedmsg) / 2):]
    b = encryptedmsg[:int(len(encryptedmsg)/2)]
    c=''
    for i in range(len(a)):
        c += a[i]
        c += b[i]

    # think of using a 2d list
    encryptedmsg = c


    o=[]
    for i in key:
        o.append(i)

    n = math.ceil(len(encryptedmsg)/len(key))
    data = [encryptedmsg[i:i+n] for i in range(0, len(encryptedmsg), n)]

    o.sort()
    dic=dict(zip(o,data))

    decryptedmsg = ''
    for i in range(n):
        for j in key:
            decryptedmsg+=dic[j][i]

    decryptedmsg = decryptedmsg.replace('x','')
    print("Decrypted message is : ",decryptedmsg)


if __name__ == '__main__':

    print("Implementing Columnar Transposition\n")

    encryptMessage()
    decryptMessage()
