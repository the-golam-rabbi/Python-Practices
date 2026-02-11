def accum(st):
    length = 1
    string_leng = len(st)
    res = ""
    
    for char in st:
        res += char.upper()
        
        for i in range(length-1):
            res += char.lower()
        
        if (string_leng != length):
            res += "-"
        length += 1   
    return res
        
