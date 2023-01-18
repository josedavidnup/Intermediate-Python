price = 100  #global


def increment():
  price = 200
  result = price + 10
  print(result)
  return result


print(price)
price2 = increment()
print(price2)