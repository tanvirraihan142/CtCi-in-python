def replace_spaces(str1,true_length):
    space_count=0
    i=0
    str1 = list(str1)
    for i in range(true_length):
        if (str1[i]==' '):
            space_count+=1
    index = true_length + space_count*2

    if (true_length < len(str1)):
        str1[true_length] = '\0'

    str2 = [' ' for i in range(index)]
    for i in range(true_length-1,-1,-1):
        if (str1[i]==' '):
            str2[index-1]='0'
            str2[index-2]='2'
            str2[index-3]='%'
            index = index - 3
        else:
            str2[index-1] = str1[i]
            index-=1

    return "".join(str2)
            
