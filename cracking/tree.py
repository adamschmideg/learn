class BSTNode:
    left = None
    right = None
    parent = None
    value = None

    def __init__(self, value):
        self.value = value

    def insert(self, new_val):
        if new_val < self.value:
            if self.left:
                self.left.insert(new_val)
            else:
                self.left = BSTNode(new_val)
        elif self.right:
            self.right.insert(new_val)
        else:
            self.right = BSTNode(new_val)

    @staticmethod
    def from_list(vals_or_v):
        """
        >>> node = BSTNode.from_list([2, [1, 0, None], 3])
        >>> node.value
        2
        >>> node.left.value
        1
        >>> node.left.left.value
        0
        >>> node.right.value
        3
        """
        try:
            p, l, r = vals_or_v
            parent = BSTNode(p)
            if l is not None:
                parent.left = BSTNode.from_list(l)
            if r is not None:
                parent.right = BSTNode.from_list(r)
        except TypeError:
            parent = BSTNode(vals_or_v)
        return parent

    def to_list(self):
        """
        >>> node = BSTNode.from_list([2, [1, 0, None], 3])
        >>> node.to_list()
        [2, [1, 0, None], 3]
        """
        if self.left is None and self.right is None:
            return self.value
        l = self.left.to_list() if self.left is not None else None
        r = self.right.to_list() if self.right is not None else None
        return [self.value, l, r]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
