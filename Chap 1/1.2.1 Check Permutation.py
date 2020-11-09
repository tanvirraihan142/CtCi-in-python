def permutation(str1, str2):
    l1 = list(str1)
    l1.sort()
    l2 = list(str2)
    l2.sort()
    sorted_str1 = "".join(l1)
    sorted_str2 = "".join(l2)
    print(sorted_str1,sorted_str2)
    if len(str1)==len(str2):
        if sorted_str1 == sorted_str2:
            return True
        else:
            return False
    else:
        return False
