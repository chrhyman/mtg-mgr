def only1(lst):
    found_true = False
    for b in lst:
        if b:
            if found_true:
                return False
            else:
                found_true = True
    return found_true

def morethan1(lst):
    x = 0
    for b in lst:
        if b:
            x += 1
    return x > 1

def exactly2(lst):
    x = 0
    for b in lst:
        if b:
            x += 1
    return x == 2
