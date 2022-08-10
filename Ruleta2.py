import random
ruleta = []
opt = input("Escribe todas las opciones que quieras\nPara elegir una de ellas aleatoriamente, escribe \"!\": ")
while opt != "!":
    ruleta.append(opt)
    opt = input("Escribe otra opción: ")

result = random.choice(ruleta)
print(result)
