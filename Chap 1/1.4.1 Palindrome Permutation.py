def is_permutation_of_palindrome(phrase):
    table = build_char_frequency_table(phrase)
    return check_max_one_odd(table)

def check_max_one_odd(table):
    found_odd = False
    for count in table:
        if (count%2==1):
            if (found_odd):
                return False
            found_odd = True
    return True

def get_char_number(c):
    a = ord('a')
    z = ord('z')
    val = ord(c)
    if (a <= val and val<= z):
        return val-a
    return -1

def build_char_frequency_table(phrase):
    table = [0 for i in range(ord('z') - ord('a') + 1)]
    for c in list(phrase):
        x = get_char_number(c)
        if (x != -1):
            table[x] += 1
    return table
