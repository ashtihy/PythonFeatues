def my_generator():
    yield 1
    yield 2
    yield 3


# Print type of yield function it is a generator class which return a generator iterator.
print(type(my_generator()))

print(("="*100))
# Here Both will return 1 because each time we call the function generator, it returns a new generator iterator.
print(next(my_generator()))
print(next(my_generator()))

print(("="*100))
# Here both will return 1 and then 2 because we called the function generator once, it returns a new generator iterator and we iterate over it.
generator_iterator = my_generator()
print(type(generator_iterator))
print(next(generator_iterator))
print(next(generator_iterator))
# looping started from third item because I used next two times.
for num in generator_iterator:
    print(num)
