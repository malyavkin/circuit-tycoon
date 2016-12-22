def is_tuple_of_n_ints(n, var):
    if type(var) is not tuple:
        return False
    if len(var) != n:
        return False
    for i in var:
        if type(i) is not int:
            return False
    return True

