#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    s = temps[0] * 86400 + temps[1] * 3600 + temps[2] * 60 + temps[3]
    return s

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    j = seconde // 86400
    hs = seconde % 3600
    h = hs - j * 24
    m = hs // 60
    s = hs % 60
    print(j, h, m, s)
    return
temps = str(secondeEnTemps(342094))
temps = (3,23,1,34)
print(temps[0], "jour", temps[1], "heure", temps[2], "minute", temps[3], "seconde")




#fonction auxiliaire ici

def afficheTemps(temps):   
        if temps[0]  > 1 :
           print(temps[0], "jours")
        elif temps[0] == 1 :
            print(temps[0], "jours")
        else :
            pass
        if temps[1]  > 1 :
            print(temps[1], "heures")
        elif temps[1] == 1 :
            print(temps[1], "heure")
        else :
            pass
        if temps[2]  > 1 :
            print(temps[2], "minutes")
        elif temps[2] == 1 :
            print(temps[2], "minute")
        else :
            pass
        if temps[3]  > 1 :
            print(temps[3], "secondes")
        elif temps[3] == 1 :
            print(temps[3], "seconde")
        else :
            pass
        return 
        
afficheTemps((1,0,14,23))

