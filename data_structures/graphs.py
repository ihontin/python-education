"""Graphs module

methods: insert lookup delete
"""
from linked_list import LinkedList


class Vertexlist:
    """Box class keeps links and values"""

    def __init__(self, vertex=None, ed=None, link_next=None):
        self.next = link_next
        self.vertex = vertex
        self.edges = ed


class Graphlist:
    """Handmade Graph
    methods: lookup insert delete
    """

    def __init__(self):
        """first vertex, last vertex and"""
        self.first = None
        self.last = None

    def insert(self, key, *args):
        """Insert vertex and edges to end of our list"""
        edge = LinkedList()
        if len(args) > 0:
            for next_edge in args:
                edge.append(next_edge)
        if self.first is None:
            self.first = Vertexlist(key, edge, None)
            self.last = self.first
        elif self.first is not None:
            self.last.next = Vertexlist(key, edge, None)
            self.last = self.last.next

    def lookup(self, value):
        """Find by value and return link of vertex"""
        if self.first is None:
            return f"'{value}' not found"
        twin_first = self.first
        while twin_first is not None:
            if twin_first.vertex == value:
                return twin_first
            twin_first = twin_first.next
        return f"'{value}' not found"

    def delete(self, vertex_val):
        """Delete element by value"""
        if self.first is None:
            return
        twin_first = prev_first = self.first
        if vertex_val == twin_first.vertex:
            self.first = self.first.next
            return
        while twin_first is not None:
            if twin_first.vertex == vertex_val:
                prev_first.next = twin_first.next
                if twin_first.next is None:
                    self.last = prev_first
                break
            prev_first = twin_first
            twin_first = twin_first.next
