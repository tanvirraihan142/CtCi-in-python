def compress(str1):
    final_length = count_compression(str1)
    if (final_length >= len(str1)):
        return str1
    compressed = []
    count_consecutive = 0
    for i in range(len(str1)):
        count_consecutive+=1
        if (i+1 >= len(str1) or str1[i] != str1[i+1]):
            compressed.append(str1[i])
            compressed.append(str(count_consecutive))
            count_consecutive = 0
    return "".join(compressed)

def count_compression(str1):
    compressed_length = 0
    count_consecutive = 0
    for i in range(len(str1)):
        count_consecutive +=1
        if (i+1>=len(str1) or str1[i] != str1[i+1]):
            compressed_length += len(str(count_consecutive)) + 1
            count_consecutive = 0
    return compressed_length
