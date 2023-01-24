def make_stack(end_list):
    list_of_value = []
    if end_list == 0 or end_list < 0:
        return []
    for i in range(end_list+1):
        list_of_value.append(i)
    return list_of_value


