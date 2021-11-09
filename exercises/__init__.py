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
    j = 342094 // 86400
    hs = 342094 % 3600
    h = hs - j * 24
    m = hs // 60
    s = hs % 60
    print(j, h, m, s)
    return
    

    
temps = secondeEnTemps(100000)
print(temps[0], "jour", temps[1], "heure", temps[2], "minute", temps[3], "seconde")




