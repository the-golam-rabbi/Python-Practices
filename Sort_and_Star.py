def two_sort(array):
    array.sort()
    
    first = array[0]
    res = ""
    
    for ind, char in enumerate(first, start = 1):
        if (ind != len(first)):
            res += char
            res += "***"
        else:
            res += char
            
    return res
        
        
