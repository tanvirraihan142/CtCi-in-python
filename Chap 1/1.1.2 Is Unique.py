def is_unique_chars(str1):
    checker = 0

    for i in range(len(str1)):
        val = ord(str1[i]) - ord('a')
        if ((checker &(1<<val) > 0)):
            return False
        checker |= (1<<val)
            
    return True
