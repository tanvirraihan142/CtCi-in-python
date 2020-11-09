def is_rotation(s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    if (len1 == len2 and len1>0):
        s1s1 = s1+s1
        return is_substring(s1s1, s2)
    return False

def is_substring(s1s1,s2):
    if s2 in s1s1:
        return True
    else:
        return False
