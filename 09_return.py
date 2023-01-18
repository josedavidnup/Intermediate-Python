def find_volume(length=1, width=1, depth=1):
  return length * width * depth * 10, width, 'hola'


# result = find_volume(10, 20, 3)
# result, width, text = find_volume(width=10)

# print(result)
# print(width)
# print(text)

uno, dos, tres = find_volume(width=10)

print(uno)
print(dos)
print(tres)
