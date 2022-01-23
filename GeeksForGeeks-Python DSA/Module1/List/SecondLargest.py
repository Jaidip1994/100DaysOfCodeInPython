elem_list = [5,20,12,10, 20, 10, 12]

def find_second_largest(elem_list):
    if len(elem_list) <= 1:
        return None
    larg = elem_list[0]
    slar = None
    for elem in elem_list:
        if elem > larg:
            slar, larg = larg, elem
        elif elem != larg:
            if slar == None or elem > slar:
                slar = elem
    return slar

print(find_second_largest(elem_list))
print(find_second_largest([10, 10, 10]))