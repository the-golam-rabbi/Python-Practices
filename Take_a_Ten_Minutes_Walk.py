def is_valid_walk(walk):
    
    if len(walk) != 10:
        return False
    elif((walk.count("n") == walk.count("s")) and (walk.count("e") == walk.count("w"))):
        return True
    else:
        return False
   
#just realized, I could have just 
    return ((len(walk) == 10) and walk.count("n") == walk.count("s")) and (walk.count("e") == walk.count("w"))
