"""Binary search tree

methods: insert lookup delete
"""


class BoxVal:
    """Box class keeps links and values"""

    def __init__(self, val=None):
        """Create link and value of the next box"""
        self.val = val
        self.left = None
        self.right = None


class BinaryTreeSearch:
    """Handmade stack

    methods: insert lookup delete
    """

    def __init__(self):
        """Root of the binary tree"""
        self.root = None
        self.count = 0

    def insert(self, value):
        """Append value
        to root if None in it"""
        self.count += 1
        if self.root is None:
            self.root = BoxVal(value)
        else:
            self._add(value, self.root)

    def _add(self, val, node):
        """Append value
        recursive function
        node == self.root
        """
        if val < node.val:
            if node.left is not None:
                self._add(val, node.left)
            else:
                node.left = BoxVal(val)
        else:
            if node.right is not None:
                self._add(val, node.right)
            else:
                node.right = BoxVal(val)

    def lookup(self, val):
        """Find and return value"""
        if self.root is not None:
            return self._find(val, self.root)
        return None

    def _find(self, val, node):
        """Finding value
        recursive function
        node == self.root
        """
        if val == node.val:
            return node
        elif val < node.val and node.left is not None:
            return self._find(val, node.left)
        elif val > node.val and node.right is not None:
            return self._find(val, node.right)

    def delete(self, value):
        """Delete value"""
        if self.root is None:
            return
        if self.root is not None:
            node = self.root
            self._remove(value, node)

    def _remove(self, val, node):
        """Delete value
        recursive function
        node == self.root
        """

        if val < node.val:
            node.left = self._remove(val, node.left)
        elif val > node.val:
            node.right = self._remove(val, node.right)
        else:
            if node.left is None and node.right is None:

                if self.root == node:
                    self.root = None
                    return self.root
                node = None
                return node
            if node.left is None:
                if self.root == node:
                    self.root = node.right
                    return self.root
                node = node.right
                return node
            if node.right is None:
                if self.root == node:
                    self.root = node.left
                    return self.root
                node = node.left
                return node

            min_max = node.right
            while min_max.left is not None:
                min_max = min_max.left
            new_node = min_max
            node.val = new_node.val
            node.right = self._remove(new_node.val, node.right)
        return node
