import fonctions as f

while True : 


    nb1=int(input("nombre qui sera mis en puissance ?"))
    nb2=int(input("puissance ?"))
    if type(nb1) is not int : 
        raise TypeError("seulement les entiers sont accepté")
    else : 
        result=f.puissance(nb1,nb2)
        print("La puissance de",nb1, "par",nb2, "est", result)
