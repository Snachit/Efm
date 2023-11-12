def NbCMIn(Pass):
    c = 0
    for i in Pass :
        if i.islower() == True :
            c += 1
    return c
def NbCMaj(Pass):
    c = 0 
    for i in Pass :
        if i.isupper() == True:
            c += 1 
    return c 
def NbCAlpha(Pass):
    c = 0
    for i in Pass :
        if i.isalpha() == False : 
            c += 1
    return c 
def LongMaj(Pass):
    longest_sequence = ""
    for i in Pass:
        if i.isupper() == True:
            longest_sequence += i
    return longest_sequence
def LongMin(Pass):
    longest_sequence = ""
    for i in Pass :
        if i.islower():
            longest_sequence += i
    return longest_sequence
def Bonus(Pass):
    bonus = 0 
    bonus = (len(Pass) * 4) + ((len(Pass) - NbCMaj(Pass)) * 2 ) + (( len(Pass) - NbCMIn(Pass)) * 3) + NbCAlpha(Pass) * 5 
    return bonus
def Malus(Pass) :
    malus = (len(LongMin(Pass))*2) + (len(LongMaj(Pass))*2)
    return malus
def Score(Pass):
    score = Bonus(Pass) + Malus(Pass) 
    return score

PassWord = str(input("Entrer votre mot de pass :"))
if Score(PassWord) < 20 :
    print(f" Le {PassWord} est très faible ")
elif 20 <= Score(PassWord) < 40 :
    print(f" Le {PassWord} est faible ")
elif  40 <= Score(PassWord) < 80 :
    print(f" Le {PassWord} est fort ")
else :
    print(f" Le {PassWord} est très fort ")




    