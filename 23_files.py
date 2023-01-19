file = open('./text.txt')
# print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

for line in file:
  print(line)

file.close()

with open('./text.txt') as file:
  for line in file:
    print(line)

# lee un archivo en forma de lista
print(file.readlines())

#También es recomendable usar esta estructura para que no aparezcan símbolos raros encaso de que se sean archivos binarios.
# ‘r’ = para leer el archivo
# ’encoding="UTF-8’ = convierte todo en letras

# with open("./archivos/numbers.txt", "r", encoding="UTF-8") as f:
