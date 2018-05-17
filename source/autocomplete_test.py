#!python

from autocomplete import insert_word
from tries import Trie
import unittest


class TrieTest(unittest.TestCase):

    def test_init(self):
        trie = Trie()
        data, is_word = trie.root.data
        assert data == ""
        assert is_word is False
        assert trie.root.next == {}

    def test_insert_with_3_items(self):
        trie = Trie()
        assert trie.root.data == ('', False)
        assert trie.root.next == {}
        trie.insert("a")
        assert trie.root.next['a'] is not None
        assert len(trie.root.next) == 1
        node = trie.root.next['a']
        assert node.data == ('a', True)
        assert node.next == {}
        trie.insert("a")
        assert trie.root.next['a'] is not None
        assert len(trie.root.next) == 1
        node = trie.root.next['a']
        assert node.data == ('a', True)
        assert node.next == {}
        trie.insert("b")
        assert trie.root.next['b'] is not None
        assert len(trie.root.next) == 2
        node = trie.root.next['b']
        assert node.data == ('b', True)
        assert node.next == {}
        trie.insert("c")
        assert trie.root.next['c'] is not None
        assert len(trie.root.next) == 3
        node = trie.root.next['c']
        assert node.data == ('c', True)
        assert node.next == {}

    def test_inset_with_7_items(self):
        trie = Trie()
        words_list = ['a', 'app', 'apple', 'be', 'bee', 'beat', 'c']
        for word in words_list:
            trie.insert(word)
        assert trie.root.data == ('', False)
        assert len(trie.root.next) == 3

        assert trie.root.next['a'] is not None
        node = trie.root.next['a']
        assert node.data == ('a', True)
        assert len(node.next) == 1
        assert node.next['p'] is not None
        node = node.next['p']
        assert node.data == ('ap', False)
        assert len(node.next) == 1
        assert node.next['p'] is not None
        node = node.next['p']
        assert node.data == ('app', True)
        assert len(node.next) == 1
        assert node.next['l'] is not None
        node = node.next['l']
        assert node.data == ('appl', False)
        assert len(node.next) == 1
        assert node.next['e'] is not None
        node = node.next['e']
        assert node.data == ('apple', True)
        assert len(node.next) == 0

        assert trie.root.next['b'] is not None
        node = trie.root.next['b']
        assert node.data == ('b', False)
        assert len(node.next) == 1
        assert node.next['e'] is not None
        node = node.next['e']
        assert node.data == ('be', True)
        assert len(node.next) == 2
        assert node.next['e'] is not None
        node1 = node.next['e']
        assert node1.data == ('bee', True)
        assert len(node1.next) == 0
        assert node.next['a'] is not None
        node2 = node.next['a']
        assert node2.data == ('bea', False)
        assert len(node2.next) == 1
        assert node2.next['t'] is not None
        node = node2.next['t']
        assert node.data == ('beat', True)
        assert len(node.next) == 0

        assert trie.root.next['c'] is not None
        node = trie.root.next['c']
        assert node.data == ('c', True)
        assert len(node.next) == 0


class AutocompleteTest(unittest.TestCase):

    def test_insert_word():
