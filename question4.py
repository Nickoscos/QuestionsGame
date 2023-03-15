# Question 4

def reponse4() :

    L = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]
    print('Voici les notes des élèves')
    print(L)

    L1 = []

    for i in range(len(L)):
        if L[i] >= 10:
            L1.append(L[i])

    print("Et voici la liste des notes supérieures ou égales à 10")
    print(L1)
