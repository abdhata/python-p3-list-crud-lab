def create_an_empty_list():
    return []
pass

def create_a_list():
    return [1, 2, 3, 4]
pass

def add_element_to_end_of_list(l, element):
    l.append(element)
    return l
pass

def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l
    pass

def remove_element_from_end_of_list(l):
    l.pop()
    return l

def remove_element_from_start_of_list(l):
    l.pop(0)
    return l
pass

def retrieve_first_element_from_list(l):
    return l[0]

def retrieve_element_from_index(l, index):
    return l[index]

def retrieve_last_element_from_list(l):
    return l[-1]
