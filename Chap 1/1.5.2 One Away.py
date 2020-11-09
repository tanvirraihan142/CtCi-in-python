def one_edit_away(first,second):
    if abs(len(first)-len(second)) > 1:
        return False

    if (len(first) < len(second)):
        s1 = first
        s2 = second
    else:
        s1 = second
        s2 = first

    index1 = 0
    index2 = 0

    found_diff = False
    while(index2 < len(s2) and index1 < len(s1)):
        if (s1[index1] != s2[index2]):
            if (found_diff):
                return False
            found_diff = True
            if (len(s1) == len(s2)):
                index1 += 1
        else:
            index1 += 1
        index2+=1

    return True
            
            
