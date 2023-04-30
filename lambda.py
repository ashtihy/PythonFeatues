def say_hello(name, age): return f"Hello {name} your age is {age}"


hello = lambda name, age: f"Hello {name} your age is {age}"

print(say_hello("Ahmed", 29))
print(hello("Ahmed", 30))

print(say_hello.__name__)
print(hello.__name__)

print("="*100)

nums = [48, 6, 9, 21, 1]

square_all = map(lambda num: num ** 2, nums)

print(square_all)
print(list(square_all))
