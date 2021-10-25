"""Linked list module

methods: append prepend lookup insert delete
"""


class ListVal:
    """Box class keeps links and values"""
    def __init__(self, val=None, nex=None):
        """Create link and value of the next box"""
        self.val = val
        self.next = nex


class LinkedList:
    """Handmade linked list
    methods: append prepend lookup insert delete
    """

    def __init__(self):
        """Head - first, tail - last"""
        self.first = None
        self.last = None

    def __str__(self):
        """Show all list elements"""
        if self.first is not None:
            twin_first = self.first
            output = str(twin_first.val)
            while twin_first.next is not None:
                twin_first = twin_first.next
                output += f" {str(twin_first.val)}"
            return output
        return "Empty list"

    def getlink(self, value):
        """Return link to the element by value"""
        if self.first is None:
            return f"{value} not found"
        link = self.first
        while link is not None:
            if link.val == value:
                return link
            link = link.next

    def append(self, value):
        """Insert value at the end of the list"""
        if self.first is None:
            self.first = ListVal(value, None)
            self.last = self.first
        elif self.first is not None:
            self.last.next = ListVal(value, None)
            self.last = self.last.next

    def prepend(self, f_value):
        """Insert value at the beginning of the list"""
        if self.first is None:
            self.first = ListVal(f_value, None)
            self.last = self.first
        else:
            self.first = ListVal(f_value, self.first)

    def lookup(self, value):
        """Return index of the first found value"""
        if self.first is None:
            return f"'{value}' not found"
        twin_first = self.first
        index = 0
        while twin_first is not None:
            if twin_first.val == value:
                return index
            index += 1
            twin_first = twin_first.next
        return f"'{value}' not found"

    def insert(self, i, vale):
        """Insert element by index"""
        if self.first is None:
            self.last = self.first = ListVal(vale, None)
            return
        if i == 0:
            self.first = ListVal(vale, self.first)
            return
        twin_first = self.first
        count = 0
        while twin_first is not None:
            count += 1
            if count == i:
                twin_first.next = ListVal(vale, twin_first.next)
                if twin_first.next.next is None:
                    self.last = twin_first.next
                break
            twin_first = twin_first.next

    def delete(self, delindex):
        """Delete element by index"""
        if self.first is None:
            return
        count = 0
        twin_first = prev_first = self.first
        if delindex == 0:
            self.first = self.first.next
            return
        while twin_first is not None:
            if count == delindex:
                prev_first.next = twin_first.next
                if twin_first.next is None:
                    self.last = prev_first
                break
            prev_first = twin_first
            twin_first = twin_first.next
            count += 1

    def show_all(self):
        """Show all list elements"""
        if self.first is not None:
            first_el = self.first
            save_all = str(first_el.val)
            while first_el.next is not None:
                save_all += f" {first_el.next.val}"
                first_el = first_el.next
            return save_all
        return "Empty list"
