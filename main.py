# ############################### PROGRAMME PRINCIPAL ###########################

# import des fichiers secondaires
from question1 import reponse1
from question2 import reponse2
from question3 import reponse3
from question4 import reponse4
from question5 import reponse5

# initialisation de la reponse
reponse = ""

while reponse != "0":
    print("Quel exercice souhaitez-vous lancer ?")
    reponse = input("""
        1 : Afficher les 20 premiers termes de la table de multiplication
        2 : Afficher une table de conversion € en CAD
        3 : Afficher suite de 12 nombres dont chaque terme soit égal au triple du terme précédent
        4 : A partir des notes des élèves, créer une liste des notes au dessus de la moyenne
        5 : Trouver l'union de 2 tableaux qui renvoie un tableau unique et trié
        0 : Pour quitter l'application
    """)

    if reponse == "1":
        reponse1()
    elif reponse == "2":
        reponse2()
    elif reponse == "3":
        reponse3()
    elif reponse == "4":
        reponse4()
    elif reponse == "5":
        reponse5()
