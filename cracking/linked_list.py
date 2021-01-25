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

if __name__ == "__main__":
    import doctest
    doctest.testmod()
