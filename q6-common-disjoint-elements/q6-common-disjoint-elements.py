def something(list1, list2):
    # sorting the 2 lists to compare correctly
    list1.sort()
    list2.sort()
    # checking whether all the elements in the first list are in the second list
    if list1 == list2:
        print("True")
    else:
        print("False")
    # printing the common elements in both lists
    print(common_elements(list1, list2))
    # writing the output to a file with each element on a newline
    with open('common_elements.txt', 'w') as f:
        for line in common_elements(list1, list2):
            f.write(str(line))
            f.write('\n')

    # printing the disjoint elements in both lists
    print(disjoint_elements(list1, list2))
    # writing the output to a file with each element on a newline
    with open('disjoint_elements.txt', 'w') as f:
        for line in disjoint_elements(list1, list2):
            f.write(str(line))
            f.write('\n')


def common_elements(list1, list2):
    # converting the lists into set for the intersection of two sets to get
    # all the common elements of both the sets using intersection() method or the & operator.
    # Then covert the output into list and store it in result
    result = list(set(list1) & set(list2))
    return result


def disjoint_elements(list1, list2):
    # converting the lists into set for the symmetric difference of two sets to get
    # all the disjoint elements of both the sets that are either in the
    # first set or the second set but not in both.
    # using symmetric_difference() method or the ^ operator.
    # Then covert the output into list and store it in result
    result = list(set(list1) ^ set(list2))
    return result


l1 = [1, 2, 3, 7, 5]
l2 = [1, 6, 4, 5, 3]
something(l1, l2)
