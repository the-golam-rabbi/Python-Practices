def series_sum(n):
    sum = 0
    frac = 1
    count = 0
    
    if(n == 0):
        return "0.00"
    else:
        while (count < n):
            sum += (1/frac)
            frac += 3
            count += 1
        return f"{sum:.2f}"
            
            
            
