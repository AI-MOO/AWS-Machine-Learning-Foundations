# bad 
def count_unique_values_of_names_list_with_set(names_list):
    return len(set(names_list))


# better 
def count_unique_values(arr):
    return len(set(arr))