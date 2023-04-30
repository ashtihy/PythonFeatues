# First I need to have an iteratable object.
name = "Ahmed"
# I use iter(iteratable_object) to creatr an iterator
str_iter = iter(name)
# I use next to iterate through this iterable -> next(iterator)

# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))


# for loop it taskes an interator and use next() on this iterator and then brak when "StopIteration" Exception it throw.
for char in iter(name):
    print(char)