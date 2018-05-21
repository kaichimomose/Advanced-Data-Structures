class BTreeNode(object):

    def __init__(self, data):
        """initialize this B-tree node with the given data"""
        self.data = [data]
        self.left = None
        self.middle = None
        self.right = None
        self.reserve = None

    def __repr__(self):
        """Return a string repsentaion of this B-tree Node"""
        return 'BTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)"""
        if self.left is None and self.middle is None and self.right is None:
            return True
        else:
            return False

    def is_branch(self):
        """Return True is this node is a branch (has at least one child)"""
        if self.is_leaf():
            return False
        else:
            return True

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node)"""
        left_height = 0
        middle_height = 0
        right_height = 0

        if self.left is not None:
            left_height = self.left.height() + 1
        if self.middle is not None:
            middle_height = self.middle.height() + 1
        if self.right is not None:
            right_height = self.right.height() + 1

        return max(left_height, middle_height, right_height)

class BTree(object):

    def __init__(self, items=None):
        """initialize this B-tree and insert the insert items"""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this B-tree is empty (has no node)"""
        return self.root is None

    def height(self):
        """Return the height of B-tree"""
        return self.root.height()

    def contain(self, item):
        """Return True if this B-tree contains the given item"""
        node = self._find_node_recursive(item, self.root)
        return node is not None

    def search(self, item):
        """Return an item in this B-tree matching the given item, or None
        if the given item is not found"""
        node = self._find_node_recursive(item, self.root)
        return node.data if node is not None else None

    def insert(self):
        """Insert the given item in order into this B-tree"""

    def split(self, node, parent):
        large = node.data.pop()
        middle = node.data.pop()
        small = node.data.pop()

        if parent is None:
            new_node = BTreeNode(middle)
            new_left_node = BTreeNode(small)
            new_right_node = BTreeNode(large)

            new_node.left = new_left_node
            new_node.right = new_right_node
            self.root = new_node

            if node.second_middle is not None:
                new_left_node.left = node.left
                new_left_node.right = node.middle
                new_right_node.left = node.reserve
                new_right_node.right = node.right

            node = None

        else:
            if 


    def _find_node_recursive(self, item, node):
        if node is None:
            return None
        else:
            for data in node.data:
                if data == item:
                    return node
            if len(node.data) == 1:
                if node.data[0] > item:
                    return self._find_node_recursive(item, node.left)
                else:
                    return self._find_node_recursive(item, node.right)
            elif len(node.data) == 2:
                small, large = node.data
                if small > item:
                    return self._find_node_recursive(item, node.left)
                elif large < item:
                    return self._find_node_recursive(item, node.right)
                else:
                    return self._find_node_recursive(item, node.middle)

    def _find_parent_node_recursive(self, item, node, parent=None):
        if node is None:
            return parent
        else:
            for data in node.data:
                if data == item:
                    return parent
            if len(node.data) == 1:
                if node.data[0] > item:
                    return self._find_parent_node_recursive(item, node.left,
                                                            node)
                else:
                    return self._find_parent_node_recursive(item, node.right,
                                                            node)
            elif len(node.data) == 2:
                small, large = node.data
                if small > item:
                    return self._find_parent_node_recursive(item, node.left,
                                                            node)
                elif large < item:
                    return self._find_parent_node_recursive(item, node.right,
                                                            node)
                else:
                    return self._find_parent_node_recursive(item, node.middle,
                                                            node)
