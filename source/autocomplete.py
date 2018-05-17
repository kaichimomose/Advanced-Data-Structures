#!python

import random
import time
from tries import Trie


def get_words(filename):
    with open(filename, 'r') as f:
        words_list = f.read().split()

    return words_list


def binarysearch(list_, item, left=None, right=None):
    if left is None and right is None:
        left = 0
        right = len(list_) - 1
    middle = (right + left) // 2
    item_length = len(item)
    middle_item = list_[middle]
    if middle_item[:item_length].lower() == item.lower():
        return find_all_words(list_, item, middle)
    elif middle_item[:item_length].lower() < item.lower():
        return binarysearch(list_, item, middle + 1, right)
    elif middle_item[:item_length].lower() > item.lower():
        return binarysearch(list_, item, left, middle - 1)
    elif left > right:
        return None


def find_all_words(list_, item, middle):
    predicted_words = [list_[middle]]
    item_length = len(item)
    left_match = True
    right_match = True
    left_index = middle
    right_index = middle
    while left_match:
        left_index -= 1
        if left_index < 0:
            left_match = False
        else:
            word = list_[left_index]
            if word[:item_length].lower() == item.lower():
                predicted_words.append(word)
            else:
                left_match = False
    while right_match:
        right_index += 1
        if right_index >= len(list_):
            right_match = False
        else:
            word = list_[right_index]
            if word[:item_length].lower() == item.lower():
                predicted_words.append(word)
            else:
                right_match = False
    return predicted_words


def insert_word(words_list):
    trie = Trie()
    for word in words_list:
        trie.insert(word)
    return trie


def find_prefix(trie, prefix):
    node = trie.root
    for letter in prefix:
        node = node.next[letter]
    return node.next


def find_words(nodes, words=[]):
    if nodes != {}:
        for letter in nodes:
            if nodes[letter].data[1]:
                words.append(nodes[letter].data[0])

            words = find_words(nodes[letter].next, words)
        return words
    else:
        return words

def find_all_words_with_trie(trie, prefix):
    nodes = find_prefix(trie, prefix)
    all_words = find_words(nodes)
    return all_words

def autocomplete(words_list, prefix=""):
    # prefix_length = len(prefix)
    # predicted_words = []
    # for word in words_list:
    #     # if word.startswith(prefix):
    #     if word[:prefix_length] == prefix:
    #         predicted_words.append(word)
    # predicted_words = binarysearch(words_list, prefix)
    predicted_words = find_all_words_with_trie(words_list, prefix)
    return predicted_words


def benchmark(all_prefixes):
    t1 = time.time()
    filename = "/usr/share/dict/words"
    words_list = get_words(filename)
    t2 = time.time()
    print('Took {} seconds to create list'.format(t2-t1))
    trie = insert_word(words_list)
    t3 = time.time()
    print('Took {} seconds to create trie'.format(t3-t2))
    for prefix in all_prefixes:
        # print(autocomplete(words_list, prefix))
        # autocomplete(words_list, prefix)
        autocomplete(trie, prefix)
    t4 = time.time()
    return t4 - t3


def main():
    all_words = get_words('/usr/share/dict/words')
    all_prefixes = set([word[:len(word)//2] for word in all_words])
    time = benchmark(all_prefixes)
    print('Took {} seconds to benchmark {} prefixes on {} words'.format(time, len(all_prefixes), len(all_words)))
    # Took 3.200831890106201 seconds to benchmark 71244 prefixes on 235886 words
    # import sys
    # filename = "/usr/share/dict/words"
    # words_list = get_words(filename)
    # prefix = sys.argv[1]
    # words = autocomplete(words_list, prefix)
    # print(words)

if __name__ == '__main__':
    main()
