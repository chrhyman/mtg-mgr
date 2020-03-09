def only1(lst):
    found_true = False
    for b in lst:
        if b:
            if found_true:
                return False
            else:
                found_true = True
    return found_true
