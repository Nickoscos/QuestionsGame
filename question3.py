# Question 3

def reponse3():
    num = input("Veuillez saisir un chiffre de départ entre 0.01 et 0.9 ")
    num = float(num)

    if 0.01 <= num <= 0.9:
        L = [num]
        for i in range(0, 12):
            item = L[i] ** 3
            L.append(item)

        print(L)
    else:
        print("Consigne non respectée, dommage !")
