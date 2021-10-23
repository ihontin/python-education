"""Hash Table module

methods: lookup insert delete
"""


class ListVal:
    """Box class keeps links, keys and values"""

    def __init__(self, val=None, nex=None, key=None):
        """Create link and value of the next box"""
        self.val = val
        self.next = nex
        self.index = key


class HashTable:
    """Handmade HashTable
    methods: lookup insert delete
    """

    def __init__(self):
        """Head - first, tail - last"""
        self.first = None
        self.last = None
        self.capacity = 30

    def __str__(self):
        """Show all list elements"""
        if self.first is not None:
            twin_first = self.first
            output = str(twin_first.index) + " " + str(twin_first.val)
            while twin_first.next is not None:
                twin_first = twin_first.next
                output += f", {str(twin_first.index)}  {str(twin_first.val)}"
            return output
        return "Empty list"

    def insert(self, key, value):
        """Insert value and hashed key at the end of the list"""
        index = hash(key)
        if self.first is None:
            self.first = ListVal(value, None, index)
            self.last = self.first
        elif self.first is not None:
            self.last.next = ListVal(value, None, index)
            self.last = self.last.next

    def hash(self, key):
        """Handmade hash function"""
        hashsum = 0
        for idx, elem in enumerate(key):
            hashsum += (idx + len(key)) ** ord(elem)
        hashsum = hashsum % self.capacity
        return hashsum

    def lookup(self, key):
        """Return value by key"""
        index = hash(key)
        if self.first is None:
            return f"Key '{key}' not found"
        twin_first = self.first
        while twin_first is not None:
            if index == twin_first.index:
                return twin_first.val
            twin_first = twin_first.next
        return f"Key '{key}' not found"

    def delete(self, key):
        """Delete element by key"""
        index = hash(key)
        if self.first is None:
            return
        twin_first = prev_first = self.first
        if index == twin_first.index:
            self.first = self.first.next
            return
        while twin_first is not None:
            if index == twin_first.index:
                prev_first.next = twin_first.next
                if twin_first.next is None:
                    self.last = prev_first
                break
            prev_first = twin_first
            twin_first = twin_first.next
