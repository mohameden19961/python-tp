
def counter(nombre):
    count=0
    while nombre > 0 :
        nombre //= 10
        count+=1
    return count


def chiffres_identiques(nombre):
    error=f"la taille du {nombre} est different du 3"
    taille=counter(nombre)
    if taille != 3:
        return error
    

    case1 = "sont identiques"
    case2 = "deux identiques"
    case3 = "tous différents"

    unite = nombre % 10
    nombre //= 10

    dizaine = nombre % 10
    nombre //=10

    centaine = nombre
    

    if dizaine == unite :
        if centaine == dizaine :
            return case1
        else:
            return case2
    elif  centaine == dizaine or centaine == unite:
        return case2
    else:
        return case3

  



nombre=int(input("saisir un nombre de trois chiffres: "))
case=chiffres_identiques(nombre)
print(case)

     
     







            
        
        


       

    