def is_permutation_of_palindrome(phrase):
    bit_vector = create_bit_vector(phrase)
    return bit_vector == 0 or check_exactly_one_bit_set(bit_vector)

def create_bit_vector(phrase):
    bit_vector=0
    for c in phrase:
        x = get_char_number(c)
        bit_vector = toggle(bit_vector, x)
    return bit_vector

def toggle(bit_vector, index):
    if (index < 0):
        return bit_vector
    mask = 1 << index
    if ((bit_vector & mask)==0):
        bit_vector |= mask
    else:
        bit_vector &= ~mask
    return bit_vector

def check_exactly_one_bit_set(bit_vector):
    return (bit_vector & (bit_vector-1)) == 0

def get_char_number(c):
    a = ord('a')
    z = ord('z')
    val = ord(c)
    if (a <= val and val<= z):
        return val-a
    return -1
