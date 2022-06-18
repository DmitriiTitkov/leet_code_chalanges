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

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)