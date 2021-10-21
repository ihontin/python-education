"""Queue module

methods: enqueue dequeue peek
"""


class QueueVal:
    """Box class keeps links and values"""

    def __init__(self, val=None, nex=None):
        """Create link and value of the next box"""
        self.val = val
        self.next = nex


class QueueListImpl:
    """Handmade Queue
    methods: enqueue dequeue peek"""

    def __init__(self):
        """Head - first, tail - last"""
        self.first = None
        self.last = None

    def enqueue(self, value):
        """Enqueue value at the end of the queue"""
        if self.first is None:
            self.first = QueueVal(value, None)
            self.last = self.first
        elif self.first is not None:
            self.last.next = QueueVal(value, None)
            self.last = self.last.next

    def dequeue(self):
        """Dequeue first element from a head"""
        self.first = self.first.next

    def peek(self):
        """Show first element from a head"""
        if self.first is None:
            return None
        return self.first.val

    def show_all(self):
        """Show all Queue elements"""
        if self.first is not None:
            first_el = self.first
            save_all = str(first_el.val)
            while first_el.next is not None:
                save_all += f" {first_el.next.val}"
                first_el = first_el.next
            return save_all
        return "Empty list"
