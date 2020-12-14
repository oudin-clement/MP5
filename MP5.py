frequencelettre = {"A":0.084,"B":0.0106,"C":0.0303,"D":0.0418,"E":0.1726,"F":0.0112,"G":0.0127,"H":0.0092,"I":0.0734,"J":0.0031,"K":0.0005,"L":0.0601,"M":0.0296,"N":0.0713,"O":0.0526,"P":0.0301,"Q":0.0099,"R":0.0655,"S":0.0808,"T":0.0707,"U":0.0574,"V":0.0132,"W":0.0004,"X":0.0045,"Y":0.0030,"Z":0.0012}


def freqmax(dico):
    inverse = [(value, key) for key, value in dico.items()]
    Max=max(inverse)[1]
    return Max

def frequence(dico):
    with open('Diderot.txt','r') as Diderot:
        tome1 = Diderot.read()
    nblettre=len(tome1)
    lettre={chr(i+65) :float(0) for i in range(26)}
    for i in tome1:
        if i in lettre:
            lettre[i]+=1
    for j in lettre:
        A=lettre[j]
        lettre[j]=A/nblettre
    for k in dico:
        B=freqmax(dico)
    for i in lettre:
        C=freqmax(lettre)
    decalage=ord(C)-ord(B)
    return int(decalage)

def decodagecesar(mess,cle):
    d = {chr(i+65):chr((i-cle) %26+65) for i in range(26)}
    nouv=""
    for j in range(len(mess)):
        if mess[j] not in d:
            nouv+=mess[j]
        else:
            nouv+=d[mess[j]]
    return nouv

        
with open('Diderot.txt','r') as Diderot:
        tome1 = Diderot.read()  
    
    
print(decodagecesar(tome1,frequence(frequencelettre)))