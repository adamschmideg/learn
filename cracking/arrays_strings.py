
def urlify(s, char_count):
    """
    >>> urlify('a b  ', 2)
    'a%20b'
    >>> urlify('a b c    ', 3)
    'a%20b%20c'
    >>> urlify('Mr John Smith    ', 11)
    'Mr%20John%20Smith'
    """
    chars = list(s)
    i = len(chars) - 1
    end_spaces = 0
    while chars[i] == ' ':
        i -= 1
        end_spaces += 1
    spaces = len(s) - char_count - end_spaces
    offset = spaces * 2
    while i >= 0:
        if chars[i] == ' ':
            chars[i + offset] = '0'
            chars[i + offset - 1] = '2'
            chars[i + offset - 2] = '%'
            offset -= 2
        else:
            chars[i + offset] = chars[i]
        if offset > 0:
            chars[i] = 'X'
        i -= 1
        #print(i+1, chars[i], "".join(chars))
    return "".join(chars)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
#    r = urlify("a b c    ", 3)
#    print(r)
