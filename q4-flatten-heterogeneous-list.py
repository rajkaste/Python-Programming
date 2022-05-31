def flatten(list1):
    result = []
    for element in list1:
        # In this loop we check whether the element in list is an instance of type list or tuple,
        # if it is then extend that list or tuple into the result list
        if isinstance(element, (list, tuple)):
            # extend() method will add specified list elements to the end of the result list
            result.extend(element)
        else:
            # and if the element is not a type of list or tuple it will append it to result list
            result.append(element)
    return result


mixed_list = [35, 53, (525, 6743), 64, 63, [743, 754, 757]]
print(flatten(mixed_list))
