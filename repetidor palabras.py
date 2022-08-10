word = input("Escribe la palabra: ")
amount = int(input("Escribe la cantidad de veces que quieres repetir la palabra: "))

omaiga = word * amount
file = open("Sussy.txt", "w")
file.write(omaiga)
file.close()