def is_permutation_of_palindrome(phrase):
    count_odd = 0
    table = [0 for i in range(ord('z')-ord('a')+1)]
    for c in phrase:
        x = get_char_number(c)
        if (x!=-1):
            table[x] += 1
            if (table[x] %2 == 1):
                count_odd += 1
            else:
                count_odd-=1


    return count_odd <= 1

def get_char_number(c):
    a = ord('a')
    z = ord('z')
    val = ord(c)
    if (a <= val and val<= z):
        return val-a
    return -1
