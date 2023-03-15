# Question 2

def reponse2():
    print('Table de conversion € => CAD')

    for euro in range(1, 16385):
        print(f"-> {euro} euro(s) = {round(euro*1.65, 2):.2f} dollar(s)")
