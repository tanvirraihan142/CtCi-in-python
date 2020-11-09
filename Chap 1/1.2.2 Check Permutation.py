def permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    letters = [0 for i in range(128)]
    str1_array = list(str1)

    for i in str1_array:
        letters[ord(i)] += 1

    for i in range(len(str2)):
        c = str2[i]
        letters[ord(c)] -= 1

    for i in letters:
        if i!=0:
            return False
        
    return True
    
