# print(0 / 0)
# print(result)
print('Hola')

suma = lambda x, y: x + y
assert suma(2, 2) == 4

print('Hola 2')

age = 10
if age < 18:
  raise Exception('No se permiten menores de edad')

print('Hola 2')

# assert() hace una verificacion y manda un AssertionError cuando no se cumple el “statement”

# raise Exception() levanta un error creado por nosotros mismo
