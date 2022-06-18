"""
https://leetcode.com/problems/prefix-and-suffix-search/solution/
Design a special dictionary with some words that searchs the words in it by a
prefix and a suffix.

Implement the WordFilter class:

WordFilter(string[] words) Initializes the object with the words in the
dictionary.
f(string prefix, string suffix) Returns the index of the word in the dictionary,
which has the prefix prefix and the suffix suffix. If there is more than one
valid index, return the largest of them. If there is no such word in the
dictionary, return -1.

Example 1:
Input
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output
[null, 0]

Explanation
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix =
"a" and suffix = 'e".


Constraints:
1 <= words.length <= 15000
1 <= words[i].length <= 10
1 <= prefix.length, suffix.length <= 10
words[i], prefix and suffix consist of lower-case English letters only.
At most 15000 calls will be made to the function f.
"""
from itertools import zip_longest
from typing import List


class TrieNode:
    def __init__(self, char: str, links=None):
        self.char = char
        self.keys = set()
        self.links = links
        if links is None:
            self.links = {}


class WordFilter:
    """
    Use trie to track prefixes and suffixes. Got TLE
    Time:
        init: O(n*k)
        f: O(n+k)

    n - amount of words
    k - longest word
    """
    def __init__(self, words: List[str]):
        self.prefix = TrieNode("#")
        self.suffix = TrieNode("#")

        for index, word in enumerate(words):
            self._add_word(word, index, self.prefix) # k
            self._add_word(word[::-1], index, self.suffix)

    def _add_word(self, word: str, key: int, trie: TrieNode):
        for char in word:
            if char not in trie.links:
                trie.links[char] = TrieNode(char)

            trie = trie.links[char]
            trie.keys.add(key)

    def _find_keys(self, pref: str, trie: TrieNode) -> set:
        for char in pref:
            if char in trie.links:
                trie = trie.links[char]
            else:
                return set()

        return trie.keys

    def f(self, prefix: str, suffix: str) -> int:
        pref_keys = self._find_keys(prefix, self.prefix)
        suff_keys = self._find_keys(suffix[::-1], self.suffix)

        keys = pref_keys & suff_keys
        return max(keys) if keys else -1


class WordFilter2:
    # TODO: refactor Trie as default dict?
    """
    Use on trie to store combination for pref and suffix. If pref and suff are
    different length store longest + None for shortest.
    Time:
        init: O(n*k^2)
        f: O(k)
    """
    def __init__(self, words: List[str]):
        self.trie = TrieNode("#")

        for index, word in enumerate(words):
            self._add_word(word, index, self.trie)  # k

    def _add_word(self, word: str, index: int, trie: TrieNode):
        # k ^ 2
        for i in range(len(word)):

            cur = trie
            for char in word[i:]:
                key = (char, None)
                if key not in cur.links:
                    cur.links[key] = TrieNode(key)

                cur = cur.links[key]
                cur.key = index

            cur = trie
            for char in word[:-i or None][::-1]:
                key = (None, char)
                if key not in cur.links:
                    cur.links[key] = TrieNode(key)

                cur = cur.links[key]
                cur.key = index

            key = (word[i], word[-i - 1])
            if key not in trie.links:
                trie.links[key] = TrieNode(key)

            trie = trie.links[key]
            trie.key = index

    def _find_keys(self, pref: str, suff: str) -> set:
        trie = self.trie

        for p, s in zip_longest(pref, suff[::-1]):
            key = (p, s)
            if key in trie.links:
                trie = trie.links[key]
            else:
                return -1

        return trie.key

    def f(self, prefix: str, suffix: str) -> int:
        return self._find_keys(prefix, suffix)  # k
