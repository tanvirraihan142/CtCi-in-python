def one_edit_away(first,second):
    if len(first) == len(second):
        return one_edit_replace(first,second)
    if len(first)+1 == len(second):
        return one_edit_insert(first,second)
    if len(first) -1 == len(second):
        return one_edit_insert(second,first)

def one_edit_replace(s1,s2):
    found_diff = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if (found_diff):
                return False
            found_diff = True
    return True

def one_edit_insert(s1,s2):
    index1=0
    index2=0
    while(index2 < len(s2) and index1<len(s1):
          if (s1[index1] != s2[index2]):
              if (index1 != index2):
                  return False
              index2+=1
          else:
              index1+=1
              index2+=1
    return True
