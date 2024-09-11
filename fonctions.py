def puissance(base, exposant):
    try :
        if exposant == 0:
            return 1
        elif exposant < 0:
            return 1 / puissance(base, -exposant)
    
        resultat = 1
        base_temp = base

        for i in range (exposant -1):
            base_temp *= base

        return base_temp
    except ZeroDivisionError:
        print("Attention, il n'est pas possible de diviser par 0 ! ")



#print(puissance(2,2))
