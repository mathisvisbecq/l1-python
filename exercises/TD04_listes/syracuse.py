def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
liste = []
n = int(input("nombre"))
while n != 1 :
    if n % 2 == 0:
        n = n // 2
    elif n % 2 != 0:
        n = n * 3 + 1
    liste.append(n)
print(liste)
print(syracuse(3))




def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """

#print(testeConjecture(10000))