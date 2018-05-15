import string


class Trie_node(object):
    def __init__(self, data, is_word=False):
        self.data = (data, is_word)
        self.next = {}


class Trie(object):
    def __init__(self, items=None):
        self.root = Trie_node("")
        # nodes = {}
        # for letter in string.ascii_lowercase:
        #     nodes[letter] = Trie_node(letter)

    def insert(self, word):
        node = self.root
        letters = node.data[0]
        for i in range(len(word)):
            letter = word[i]
            if letter in node.next:
                node = node.next[letter]
                letters += letter
            else:
                letters += letter
                is_word = False
                if i == len(word) - 1:
                    is_word = True
                node.next[letter] = Trie_node(letters, is_word)
