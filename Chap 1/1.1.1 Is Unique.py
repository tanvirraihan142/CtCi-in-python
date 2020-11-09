def is_unique_chars(str1):
    length=128
    
    if (len(str1) > length):
        return False
    
    char_set = []
    
    for i in range(length):
        char_set.append(True)
        
    for i in range(0,len(str1):
        val = str1[i]
        if char_set[ord(a[i])]==True:
            return False
        char_set[ord(a[i])] = True
    return True
