
def compress_bad(str1):
    compressed_string = []
    count_consecutive = 0
    for i in range(0,len(str1)):
        count_consecutive += 1
        if (i+1 >= len(str1) or str1[i] != str1[i+1]):
            compressed_string.append(str1[i])
            compressed_string.append(str(count_consecutive))
            count_consecutive = 0
    if len(compressed_string)<len(str1):
        return "".join(compressed_string)
    else:
        return str1
    
