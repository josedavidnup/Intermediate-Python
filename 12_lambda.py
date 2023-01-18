def increment(x):
  return x + 1


result = increment(10)
print(result)

inLambda = lambda x: x + 1

result2 = inLambda(20)
print(result2)

full_name = lambda name, last_name: f'Full name is {name.title()} {last_name.title()}'

text = full_name('Jose', 'Nunez')
print(text)