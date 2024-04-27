def sort_htol(liste):
    sorted_list = []
    while liste:
        max_value = max(liste)
        sorted_list.append(max_value)
        liste.remove(max_value)
    return sorted_list


numbers = [5, 15, 9, 1, 8, 6]
highest_numbers = sort_htol(numbers)
print(highest_numbers)


def sort_ltoh(liste):
    sorted_list = []
    while liste:
        min_value = min(liste)
        sorted_list.append(min_value)
        liste.remove(min_value)
    return sorted_list

numbers = [5, 2, 2, 1, 17, 4]
lowest_numbers = sort_ltoh(numbers)
print(lowest_numbers)
