class Cell:
    next = None
    value = None

    def __init__(self, value):
        self.value = value

    @staticmethod
    def build(vals):
        last_cell = None
        head = None
        for v in vals:
            cell = Cell(v)
            if last_cell:
                last_cell.next = cell
                last_cell = cell
            else:
                last_cell = cell
                head = cell
        return head

    def list(self):
        """
        >>> head = Cell.build([1, 2, 3])
        >>> head.list()
        [1, 2, 3]
        """
        v = []
        cell = self
        while cell:
            v.append(cell.value)
            cell = cell.next
        return v

    def revert(self):
        """
        >>> head = Cell.build([1, 2, 3])
        >>> head.revert().list()
        [3, 2, 1]
        """
        if not self.next:
            return self
        old_head = self.next
        new_head = self
        new_head.next = None
        while old_head:
            tmp = old_head.next
            old_head.next = new_head
            new_head = old_head
            old_head = tmp
        return new_head

    def has_loop(self):
        """
        >>> good = Cell.build([1, 2, 3])
        >>> good.has_loop()
        False
        >>> a = Cell('a')
        >>> b = Cell('b')
        >>> c = Cell('c')
        >>> d = Cell('d')
        >>> b.next = c
        >>> c.next = d
        >>> d.next = b
        >>> a.next = b
        >>> a.has_loop()
        True
        """
        rev = self.revert()
        return rev == self

if __name__ == "__main__":
    import doctest
    doctest.testmod()
