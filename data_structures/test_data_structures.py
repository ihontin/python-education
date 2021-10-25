"""Testing data structures
binary search tree, queue, linked list, hash table, graph, stack
"""

from random import sample, choices
import string
import pytest
from binary_search_tree import BinaryTreeSearch
from queue_list import QueueListImpl
from linked_list import LinkedList
from hash_table import HashTable
from graphs import Graphlist
from stack import StackList



def lists_gen():
    """Generate list with 100 random elements"""
    basic_list = [gen for gen in range(1000)]
    interim_list = sample(basic_list, 100)
    return interim_list


def lists_gen_next():
    """Generate list with 100 random elements"""
    basic_list = [gen for gen in range(1001, 2000)]
    interim_list = sample(basic_list, 100)
    return interim_list


class TestLinkedList:
    """Testing handmade linked list
    methods: append prepend lookup insert delete
    """

    @pytest.mark.parametrize("lists_g", [lists_gen()])
    def test_append_linked_list(self, lists_g):
        """Testing handmade linked list
        methods: append lookup
        lookup return index of element
        after each applying of the append method index of the element will increment from 0
        """
        counter = 0
        test_mod = LinkedList()
        while counter < 100:
            value = lists_g[counter]
            test_mod.append(value)
            assert test_mod.lookup(value) == lists_g.index(value), "equal should be"
            counter += 1

    @pytest.mark.parametrize("lists_g", [lists_gen()])
    def test_prepend_linked_list(self, lists_g):
        """Testing handmade linked list
        methods: prepend lookup
        lookup return index of element
        after each applying of the prepend method index of the element should be 0
        """
        counter = 0
        prepend_mod = LinkedList()
        lists_g.reverse()
        while counter < 100:
            value = lists_g[counter]
            prepend_mod.prepend(value)
            assert prepend_mod.lookup(value) == 0, "0 should be"
            counter += 1

    @pytest.mark.parametrize("lists_g, lists_g_next", [(lists_gen(), lists_gen_next())])
    def test_insert_linked_list(self, lists_g, lists_g_next):
        """Testing handmade linked list
        methods: lookup insert
        lookup return index of element
        after each applying of the insert method index of the element should be
        the same, as another list.index(value) method return
        """
        counter = 0
        prepend_mod = LinkedList()
        for i in lists_g:
            prepend_mod.append(i)
        while counter < 100:
            value = lists_g_next[counter]
            lists_g.insert(counter, value)
            prepend_mod.insert(counter, value)
            assert prepend_mod.lookup(value) == lists_g.index(value), "equal should be"
            counter += 2

    @pytest.mark.parametrize("lists_g", [lists_gen()])
    def test_delete_linked_list(self, lists_g):
        """Testing handmade linked list
        methods: lookup delete
        lookup return index of element
        after each applying of the delete method, index of the element should not be found
        """
        counter = 0
        prepend_mod = LinkedList()
        for i in lists_g:
            prepend_mod.append(i)
        while counter < 100:
            prepend_mod.delete(0)
            assert prepend_mod.lookup(lists_g[counter]) == f"'{lists_g[counter]}' not found" \
                , "equal should be"
            counter += 1


class TestStack:
    """Testing handmade Stack
    methods: push pop peek
    """

    @pytest.mark.parametrize("lists_g", [lists_gen()])
    def test_peek_stack(self, lists_g):
        """Testing handmade Stack
        methods: push pop peek
        compare first elements of the stack and list
        """
        counter = 0
        prepend_mod = StackList()
        for i in lists_g:
            prepend_mod.push(i)
        while counter < 100:
            assert prepend_mod.peek() == lists_g[counter], "equal should be"
            prepend_mod.pop()
            counter += 1

    @pytest.mark.parametrize("lists_g", [lists_gen()])
    def test_pop_stack(self, lists_g):
        """Testing handmade Stack
        methods: push pop
        applying of the pop method delete and return value of the first element
        """
        counter = 0
        prepend_mod = StackList()
        for i in lists_g:
            prepend_mod.push(i)
        while counter < 100:
            assert prepend_mod.pop() == lists_g[counter], "equal should be"
            counter += 1


class TestQueue:
    """Testing handmade Queue
    methods: enqueue dequeue peek
    """

    @pytest.mark.parametrize("lists_g", [lists_gen()])
    def test_peek_enqueue_dequeue(self, lists_g):
        """Testing handmade Queue
        methods: enqueue dequeue peek
        enqueue method add 100 values at the end of the queue
        dequeue method remove values one by one from the beginning of the queue
        peek method show first element value
        """
        counter = 0
        prepend_mod = QueueListImpl()
        for i in lists_g:
            prepend_mod.enqueue(i)
        while counter < 100:
            prepend_mod.dequeue()
            if counter == 99:
                assert prepend_mod.peek() is None, "equal should be"
                break
            counter += 1
            assert prepend_mod.peek() == lists_g[counter], "equal should be"


class TestHashTable:
    """Testing handmade hash table
    methods: lookup insert delete
    """

    @pytest.mark.parametrize("lists_g, lists_g_next", [(lists_gen(), lists_gen_next())])
    def test_insert_hash_table(self, lists_g, lists_g_next):
        """Testing handmade Hash Table
        methods: lookup insert
        insert method adding value and hashed key at the end of the Hash Table
        lookup return value by hashed index
        """
        counter = 0
        prepend_mod = HashTable()
        for i in lists_g:
            prepend_mod.insert(i, lists_g_next[counter])
            counter += 1
        counter = 0
        for i in lists_g:
            assert prepend_mod.lookup(i) == lists_g_next[counter], "equal should be"
            counter += 1

    @pytest.mark.parametrize("lists_g, lists_g_next", [(lists_gen(), lists_gen_next())])
    def test_delete_hash_table(self, lists_g, lists_g_next):
        """Testing handmade Hash Table
        methods: lookup delete
        lookup return value by key
        after deleting value and key
        lookup should return str: Key '{key}' not found
        """
        counter = 0
        prepend_mod = HashTable()
        for i in lists_g:
            prepend_mod.insert(i, lists_g_next[counter])
            counter += 1
        counter = 0
        for i in lists_g:
            prepend_mod.delete(i)
            assert prepend_mod.lookup(i) == f"Key '{i}' not found", "equal should be"
            counter += 1


class TestBinaryTree:
    """Testing handmade binary search tree
    methods: insert lookup delete
    """

    @pytest.mark.parametrize("lists_g", [lists_gen()])
    def test_lookup_binary_search_tree(self, lists_g):
        """Testing handmade binary search tree
        methods: insert lookup delete
        compare elements of the binary search tree and base list
        """
        counter = 0
        prepend_mod = BinaryTreeSearch()
        for i in lists_g:
            prepend_mod.insert(i)
        for i in lists_g:
            assert prepend_mod.lookup(i).val == lists_g[counter], "equal should be"
            counter += 1

    @pytest.mark.parametrize("lists_g", [lists_gen()])
    def test_delete_binary_search_tree(self, lists_g):
        """Testing handmade binary search tree
        methods: insert lookup delete
        fill binary tree with using insert method
        delete every element one by one and check with lookup method
        """
        counter = 0
        prepend_mod = BinaryTreeSearch()
        for i in lists_g:
            prepend_mod.insert(i)
        for i in lists_g:
            prepend_mod.delete(i)
            assert prepend_mod.lookup(i) is None, "equal should be"
            counter += 1


class TestGraph:
    """Testing handmade Graph
    methods: insert lookup delete
    """

    def test_lookup_graph(self):
        """Testing handmade Graph
        methods: insert lookup
        test_vertex - 52 letters
        test_edges - 10 random generating letters
        lookup method should return vertex link
        each vertex should be equal to letter
        """
        test_vertex = string.ascii_lowercase + string.ascii_uppercase
        append_mod = Graphlist()
        for letter in test_vertex:
            test_edges = ''.join(choices(string.ascii_lowercase + string.ascii_uppercase, k=10))
            append_mod.insert(letter, *test_edges)
            assert append_mod.lookup(letter).vertex == letter, "equal should be"

    def test_delete_graph(self):
        """Testing handmade Graph
        methods: lookup delete
        test_vertex - 52 letters
        test_edges - 10 random generating letters
        lookup method should return vertex link
        after delete each vertex link lookup should be return '{vertex}' not found
        """
        test_vertex = string.ascii_uppercase + string.ascii_lowercase
        append_mod = Graphlist()
        for letter in test_vertex:
            test_edges = ''.join(choices(string.ascii_lowercase + string.ascii_uppercase, k=10))
            append_mod.insert(letter, *test_edges)
        for vertex in test_vertex:
            append_mod.delete(vertex)
            assert append_mod.lookup(vertex) == f"'{vertex}' not found", "equal should be"
