list_of_lists = [[1, 2, 3, 4], ['a', 'b', 'c'], [5, 6, 'd']]

# list comprehension
flat_list = [item for sublist in list_of_lists for item in sublist]
print(flat_list)
