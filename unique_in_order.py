def unique_in_order(sequence):
    res = []
    
    
    for ind, val in enumerate(sequence):
        if ind == 0:
            res.append(val)
        else:
            if val != sequence[ind - 1]:
                res.append(val)
    return res
    
