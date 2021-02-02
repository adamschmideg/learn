from queue import Queue

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

    def count_nodes(self):
        """
        >>> node = BSTNode.from_list([2, [1, 0, None], 3])
        >>> node.count_nodes()
        4
        """
        count = 0

        def inc(_):
            nonlocal count
            count += 1

        self.breadth_first(inc)
        return count

    def breadth_first(self, visit_fn):
        nodes = Queue()
        nodes.put_nowait(self)
        while not nodes.empty():
            elem = nodes.get_nowait()
            visit_fn(elem)
            if elem.left is not None:
                nodes.put_nowait(elem.left)
            if elem.right is not None:
                nodes.put_nowait(elem.right)

    def sequences(self):
        """
        >>> root = BSTNode.from_list([2, 1, 3])
        >>> [x for x in root.sequences()]
        [[2, 1, 3], [2, 3, 1]]
        """
        count = self.count_nodes()
        partials = Queue()
        partials.put_nowait([self])
        while not partials.empty():
            some_nodes = partials.get_nowait()
            if len(some_nodes) == count:
                yield [n.value for n in some_nodes]
            else:
                for node in some_nodes:
                    if node.left is not None and node.left not in some_nodes:
                        partials.put_nowait(some_nodes + [node.left])
                    if node.right is not None and node.right not in some_nodes:
                        partials.put_nowait(some_nodes + [node.right])

if __name__ == "__main__":
    import doctest
    doctest.testmod()
