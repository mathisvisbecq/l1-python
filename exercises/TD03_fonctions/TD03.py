#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    jour = temps[0]
    heure = temps[1]+jour*24
    minute = temps[2]+heure*60
    seconde = temps[3]+minute*60
    return seconde

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    temps[0, 0, 0, 0]
    temps[3] = seconde % 60
    temps[2] = seconde // 60 % 60
    temps[1] = seconde // 3600 % 24
    temps[0] = seconde // 86400
    return
#temps = (secondeEnTemps(342094))
#print(temps[0], "jour", temps[1], "heure", temps[2], "minute", temps[3], "seconde")




#fonction auxiliaire ici

def afficheTemps(temps):   
    jour = temps[0]
    heure = temps[1]
    minute = temps[2]
    seconde = temps[3]

    if (jour == 0) :
        jours = ''
    elif (jour == 1) :
        jours = str(jour) + 'jour'
    else :
        jours = str(jour) + 'jours'
    
    if (heure == 0) :
        heures = ''
    elif (heure == 1) :
        heures = str(heure) + 'heure'
    else :
        heures = str(heure) + 'heures'
    
    if (minute == 0) :
        minutes = ''
    elif (minute == 1) :
        minutes = str(minute) + 'minute'
    else :
        minutes = str(minute) + 'minutes'

    if (seconde == 0) :
        secondes = ''
    elif (seconde == 1) :
        secondes = str(seconde) + 'seconde'
    else :
        secondes = str(seconde) + 'secondes'
    print("cela représente", jours, heures, minutes, secondes)
         
        
#afficheTemps((1,0,14,23))


def demandeTemps():
    temps = [0, 0, 0, 0]


    temps[0] = int(input("entrez un nombre de jour: "))

    temps[1] = int(input("entrez un nombre d'heure: "))
    while (temps[1] >= 24):
        temps[1] = int(input("entrez un nombre d'heure inferieur ou egale a 24: "))

    temps[2] = int(input("entrez un nombrede minute: "))
    while (temps[2] >= 60):
        temps[2] = int(input("entrez un nombre de minute inferieur ou egale a 60: "))

    temps[3] = int(input("entrez un nombre de seconde: "))
    while (temps[3] >= 60):
        temps[3] = int(input("entrez un nombre de seconde inferieur ou egale a 60: "))
    
    return temps
    

#afficheTemps(demandeTemps())


def sommeTemps(temps1,temps2):
    

    afficheTemps(secondeEnTemps(tempsEnSeconde(temps1) + tempsEnSeconde(temps2)))

#sommeTemps((2,3,4,25),(5,22,57,1))


def proportionTemps(temps,proportion):
    if(proportion < 0.0 or proportion > 1.0):
        print("Erreur de proportion (Doit etre entre 0 et 1)")
        return 0
    return secondeEnTemps(tempsEnSeconde(temps)*proportion)
#afficheTemps(proportionTemps((2,0,36,0),0.2))
#appeler la fonction en échangeant l'ordre des arguments




def tempsEnDate(temps):
    print(temps)
    tmps = [0, 0, 0, 0, 0, 0]
    mois = (temps[0] % 365)
    tmps[0] = 1970 + (temps[0] // 365)
    if(mois <= 31):
        tmps[1] = 1
        tmps[2] = mois % 31 + 1
    elif(mois <= 59):
        tmps[1] = 2
        tmps[2] = mois % 28 + 1
    elif(mois <= 90):
        tmps[1] = 3
        tmps[2] = mois % 31 + 1
    elif(mois <= 120):
        tmps[1] = 4
        tmps[2] = mois % 30 + 1
    elif(mois <= 151):
        tmps[1] = 5
        tmps[2] = mois % 31 + 1
    elif(mois <= 181):
        tmps[1] = 6
        tmps[2] = mois % 30 + 1
    elif(mois <= 212):
        tmps[1] = 7
        tmps[2] = mois % 31 + 1
    elif(mois <= 243):
        tmps[1] = 8
        tmps[2] = mois % 31 + 1
    elif(mois <= 273):
        tmps[1] = 9
        tmps[2] = mois % 30 + 1
    elif(mois <= 304):
        tmps[1] = 10
        tmps[2] = mois % 31 + 1 
    elif(mois <= 334):
        tmps[1] = 11
        tmps[2] = mois % 30 + 1 
    else:
        tmps[1] = 12
        tmps[2] = mois % 31 + 1

    tmps[3] = tmps[1]
    tmps[4] = tmps[2]
    tmps[5] = tmps[3] 

    return tmps


def afficheDate(temps):
    annee = temps[0]
    moi = temps[1]
    jour = temps[2]
    heure = temps[3]
    minute = temps[4]
    seconde = temps[5]


    annees = str(annee)

    if (moi == 1):
        mois = ' Janvier '
    elif (moi == 2):
        mois = ' Fevrier '
    elif (moi == 3):
        mois = ' Mars '
    elif (moi == 4):
        mois = ' Avril '
    elif (moi == 5):
        mois = ' Mai '  
    elif (moi == 6):
        mois = ' Juin ' 
    elif (moi == 7):
        mois = ' Juillet ' 
    elif (moi == 8):
        mois = ' Aout '
    elif (moi == 9):
        mois = ' Septembre '
    elif (moi == 10):
        mois = ' Octobre '
    elif (moi == 11):
        mois = ' Novembre '
    elif (moi == 12):
        mois = ' Decembre '
    else:
        mois = ''

    
    jours = str(jour)

    if(heure == 0):
        heures = ''
    elif(heure == 1):
        heures = str(heure) + ' Heure '
    else:
        heures = str(heure) + ' Heures '
    

    if(minute == 0):
        minutes = ''
    elif(minute == 1):
        minutes = str(minute) + ' Minute '
    else:
        minutes = str(minute) + ' Minutes '
    
    if(seconde == 0):
        secondes = ''
    elif(seconde == 1):
        secondes = ' et ' + str(seconde) + ' Seconde '
    else:
        secondes = ' et ' + str(seconde) + ' Secondes '
    
    print("Cela représente le" + jours + mois + annees, "a", heures + minutes + secondes)



def bisextile(jour):

    njour = jour
    nb = 0

    while(njour > 366):
        njour = njour - 365


        if((nb%4 == 0 and (1970 + nb)%100 != 0) or (1970 + nb)%400 == 0):
            print(1970 + nb)


def nombreBisextile(jour):


    njour = jour
    nb = 0
    nbbisex = 0


    while(njour > 366):
        njour -= 365
        nb += 1


        if((nb%4 == 0 and (1970 + nb) % 100 != 0) or (1970 + nb) % 400 == 0):

            nbbisex += 1
    return nbbisex



def tempsEnDateBisextile(temps):
    print(temps)
