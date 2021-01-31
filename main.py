#Apertura de un fichero .txt
f = open("createdfile.txt")
contents = f.read()
f.close()
print(contents)

#Creacion de un fichero .txt
f = open("createdfile.txt", "w")
f.write("This is some data that our Python script created.\n")
f.close()
