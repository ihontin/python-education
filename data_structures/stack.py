"""Stack module

methods: push pop peek
"""


class StackVal:
    """Box class keeps links and values"""

    def __init__(self, val=None, nex=None):
        """Create link and value of the next box"""
        self.val = val
        self.next = nex


class StackList:
    """Handmade stack
    methods: push pop peek
    """

    def __init__(self):
        """Head - first, tail - last"""
        self.first = None
        self.last = None

    def show_all(self):
        """Show all stack elements"""
        if self.first is not None:
            first_el = self.first
            save_all = str(first_el.val)
            while first_el.next is not None:
                save_all += f" {first_el.next.val}"
                first_el = first_el.next
            return save_all
        return "Empty list"

    def push(self, value):
        """Insert value at the end of the stack"""
        if self.first is None:
            self.first = StackVal(value, None)
            self.last = self.first
        elif self.first is not None:
            self.last.next = StackVal(value, None)
            self.last = self.last.next

    def pop(self):
        """Remove and show value
                 of the stack first element"""
        element = self.first
        self.first = self.first.next
        return element.val

    def peek(self):
        """Show value of the stack first element"""
        return self.first.val
