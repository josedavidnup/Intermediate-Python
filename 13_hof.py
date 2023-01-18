def increment(x):
  return x + 1


increment_v2 = lambda x: x + 1


def high_order_function(x, func):
  return x + func(x)


high_order_function_v2 = lambda x, func: x + func(x)

result = high_order_function(2, increment)
result_v2 = high_order_function_v2(2, increment_v2)

print('result =>', result)
print('result_v2 =>', result_v2)

result_v3 = high_order_function_v2(2, lambda x: x + 2)
print('result_v3 =>', result_v3)
result_v4 = high_order_function_v2(2, lambda x: x * 5)
print('result_v4 =>', result_v4)