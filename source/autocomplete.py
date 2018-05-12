#!python

import random
import time



def get_words(filename):
    with open(filename, 'r') as f:
        words_list = f.read().split()

    return words_list


def binaryserch(list_, item, left=None, right=None):
    if left is None and right is None:
        left = 0
        right = len(list_) - 1
    middle = (right + left) // 2
    item_length = len(item)
    middle_item = list_[middle]
    if middle_item[:item_length].lower() == item.lower():
        return find_all_words(list_, item, middle)
    elif middle_item[:item_length].lower() < item.lower():
        return binaryserch(list_, item, middle + 1, right)
    elif middle_item[:item_length].lower() > item.lower():
        return binaryserch(list_, item, left, middle - 1)
    elif left > right:
        return None


def find_all_words(list_, item, middle):
    predicted_words = [list_[middle]]
    item_length = len(item)
    left_match = True
    right_match = False
    left_index = middle
    right_index = middle
    while left_match:
        left_index -= 1
        if left_index < 0:
            left_match = False
        else:
            word = list_[left_index]
            if word[:item_length] == item:
                predicted_words.append(word)
            else:
                left_match = False
    while right_match:
        right_index += 1
        if right_index >= len(list_):
            right_match = False
        else:
            word = list_[right_index]
            if word[:item_length] == item:
                predicted_words.append(word)
            else:
                right_match = False
    return predicted_words

def autocomplete(prefix=""):
    filename = "/usr/share/dict/words"
    words_list = get_words(filename)
    # prefix_length = len(prefix)
    # predicted_words = []
    # for word in words_list:
    #     # if word.startswith(prefix):
    #     if word[:prefix_length] == prefix:
    #         predicted_words.append(word)
    predicted_words = binaryserch(words_list, prefix)
    return predicted_words


def benchmark(all_prefixes):
    t1 = time.time()
    for prefix in all_prefixes:
        autocomplete(prefix)
    t2 = time.time()
    return t2 - t1


def main():
    all_words = get_words('/usr/share/dict/words')
    all_prefixes = set([word[:len(word)//2] for word in all_words])
    time = benchmark(all_prefixes)
    print('Took {} seconds to benchmark {} prefixes on {} words'.format(time, len(all_prefixes), len(all_words)))
    # import sys
    # prefix = sys.argv[1]
    # words = autocomplete(prefix)
    # print(words)

if __name__ == '__main__':
    main()
