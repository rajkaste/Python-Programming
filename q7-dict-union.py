# merging dict using update() method
def dict_union(dict1, dict2):
    return dict2.update(dict1)


d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 4, 'd': 'e'}

print(dict_union(d1, d2))
# if we directly print the result of dict_union method it will show None
# because after calling it dict2 gets updated due to update() method which merges one dict into another but in this,
# the dict2 is merged into dict1 and no new dict is created. It returns None.

# hence we print dict2 instead, after calling the dict_union method
print(d2)
