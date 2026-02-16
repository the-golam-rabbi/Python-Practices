def two_sum(numbers, target):
    res = ()
    
    for i in range (len(numbers)):
        for i in range (i + 1, len(numbers)):
            if (i != j):
                sum = numbers[i] + numbers[j]
                if sum == target:
                    res = res + (i,)
                    res = res + (j,)
                    return res
                
