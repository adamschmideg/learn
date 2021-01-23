
max_count = 32
large_prime = 31

class Hashtable:
    """
    >>> ht = Hashtable()
    >>> ht.get('answer') is None
    True
    >>> ht.put('answer', 42)
    >>> ht.get('answer')
    42
    >>> ht.put('answer', 100)
    42
    >>> ht.get('answer')
    100
    """

    def __init__(self):
        self.storage = [[]] * max_count

    def _hash(self, value):
        """
        >>> ht = Hashtable()
        >>> ht._hash(5)
        5
        >>> ht._hash(100)
        7
        """
        try:
            return ord(value)
        except TypeError:
            pass
        try:
            h = 0
            for x in iter(value):
                h = h ^ self._hash(x)
            return h
        except TypeError:
            pass
        try:
            return int(value) % large_prime
        except ValueError:
            pass
        return 1

    def put(self, key, value):
        h = self._hash(key)
        for entry in self.storage[h]:
            if entry[0] == key:
                old_val = entry[1]
                entry[1] = value
                return old_val
        self.storage[h].append([key, value])
        return None

    def get(self, key):
        h = self._hash(key)
        for entry in self.storage[h]:
            if entry[0] == key:
                return entry[1]
        return None


if __name__ == "__main__":
    import doctest
    doctest.testmod()