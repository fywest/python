def convert_hex_to_ascii(h):
    chars_in_reverse = []
    while h != 0x0:
        chars_in_reverse.append(chr(h & 0xFF))
        h = h >> 8
    chars_in_reverse.reverse()
    return ''.join(chars_in_reverse)

if __name__=='__main__':
    hex_str=0x7061756c
    print(convert_hex_to_ascii(hex_str))
    hex_str = 0x3D303445
    print(convert_hex_to_ascii(hex_str))