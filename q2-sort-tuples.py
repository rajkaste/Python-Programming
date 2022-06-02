tuple1 = (('k', 5), ('n', 1), ('a', 7), ('t', 6), ('j', 11))

var = sorted(tuple1, key=lambda x: x[0], reverse=True)

print(tuple(var))
