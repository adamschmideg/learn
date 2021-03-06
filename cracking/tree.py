from queue import Queue
import unittest


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
    def insert_from_flat_list(vals):
        root = BSTNode(vals[0])
        for v in vals[1:]:
            root.insert(v)
        return root

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

    def count_nodes(self, breadth_first=True):
        """
        >>> node = BSTNode.from_list([2, [1, 0, None], 3])
        >>> node.count_nodes(breadth_first=True)
        4
        >>> node.count_nodes(breadth_first=False)
        4
        """
        count = 0

        def inc(_):
            nonlocal count
            count += 1

        if breadth_first:
            self.breadth_first(inc)
        else:
            self.depth_first(inc)
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

    def depth_first(self, visit_fn):
        path = [self]
        last = None
        while path:
            bottom = path[-1]
            if last is None:
                visit_fn(bottom)
                # Descend to first existing child
                if bottom.left is not None:
                    path.append(bottom.left)
                elif bottom.right is not None:
                    path.append(bottom.right)
                # no child
                else:
                    last = path.pop()
            else:
                # we may descent to the right
                if bottom.left == last and bottom.right is not None:
                    path.append(bottom.right)
                    last = None
                else:
                    # ascend more
                    last = path.pop()

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


class BSTTest(unittest.TestCase):

    def test_sequences(self):
        root= BSTNode.from_list([3, [1, None, 2], [5, 4, 6]])
        seqs = [tuple(x) for x in root.sequences()]
        self.assertEqual(len(seqs), len(set(seqs)), "all should be different")
        baseline = BSTNode.insert_from_flat_list(seqs[0]).to_list()
        for seq in seqs[1:]:
            nodes = BSTNode.insert_from_flat_list(seq).to_list()
            self.assertEqual(baseline, nodes, "same as the first")


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    unittest.main()
