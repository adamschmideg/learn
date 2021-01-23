
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
    >>> ht.put(42, 'yey')
    >>> ht.put(42 + large_prime, 'key collision')
    >>> ht.get(42)
    'yey'
    >>> ht.get(42 + large_prime)
    'key collision'
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


len_factor = 2


class ArrayList:
    """
    >>> a = ArrayList()
    >>> len(a)
    0
    >>> a.append('x')
    >>> a.append('y')
    >>> a.append('z')
    >>> len(a)
    3
    >>> a[0]
    'x'
    >>> a[1]
    'y'
    >>> a[2]
    'z'
    """

    def __init__(self):
        self._storage = [None]
        self._len = 0
        self._real_len = 1

    def append(self, value):
        self._len += 1
        if self._len > self._real_len:
            old_len = self._real_len
            self._real_len = int(self._real_len * len_factor + 1)
            new_storage = [None for _ in range(self._real_len)]
            for i in range(old_len):
                new_storage[i] = self._storage[i]
            self._storage = new_storage
        self._storage[self._len - 1] = value
        assert self._real_len >= self._len

    def extend(self, xs):
        """
        >>> a = ArrayList()
        >>> a.extend([1, 2, 3, 4, 5])
        >>> len(a)
        5
        """
        for x in xs:
            self.append(x)

    def __getitem__(self, item):
        if item >= self._len:
            raise ValueError
        return self._storage[item]

    def __len__(self):
        return self._len


if __name__ == "__main__":
    import doctest
    doctest.testmod()