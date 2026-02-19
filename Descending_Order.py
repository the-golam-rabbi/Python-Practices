def descending_order(num):
    string = str(num)
    
    return int("".join(sorted(string, reverse = True)))
