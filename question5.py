# Question 5
import numpy as np

def reponse5() :
    T1 = np.array([0, 10, 20, 40, 60, 80])
    T2 = np.array([10, 30, 40, 50, 70])

    print("T1 = ", T1)
    print("T2 = ",  T2)
    print("L'union des deux tableaux donne :", np.union1d(T1, T2))
