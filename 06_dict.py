'''
import random
countries = ['col', 'mex', 'bol', 'pe']

population_v2 = { country: random.randint(1, 100)  for country in countries}
print(population_v2)

result = { country: population for (country, population) in population_v2.items() if population > 50 }
print(result)

text = 'Hola, soy Nicolas'
unique = { c: c.upper() for c in text if c in 'aeiou' }
print(unique)
'''

#https://static.platzi.com/media/user_upload/2022-10-24%2020_40_09-Window-d9e522c7-f24a-4d9b-9bc7-777708c05677.jpg
