"""
International Morse Code defines a standard encoding where each letter is
mapped to a series of dots and dashes, as follows:

'a' maps to ".-",
'b' maps to "-...",
'c' maps to "-.-.", and so on.
For convenience, the full table for the 26 letters of the English alphabet is
given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--",
"-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Given an array of strings words where each word can be written as a
concatenation of the Morse code of each letter.

For example, "cab" can be written as "-.-..--...", which is the concatenation of
"-.-.", ".-", and "-...". We will call such a concatenation the transformation
of a word.
Return the number of different transformations among all words we have.

Example 1:
Input: words = ["gin","zen","gig","msg"]
Output: 2
Explanation: The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations: "--...-." and "--...--.".

Example 2:
Input: words = ["a"]
Output: 1

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 12
words[i] consists of lowercase English letters.
"""
from typing import List

import pytest

morse_codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
               ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]


class Solution:
    """
    Use set to track all unique sequences
    Time: O(n)
    Space: O(n)

    n - total amount of chars in words
    """
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        unique_tranforms = set()
        for word in words:
            word_code = [morse_codes[ord(char) - ord('a')] for char in word]
            unique_tranforms.add("".join(word_code))

        return len(unique_tranforms)


@pytest.mark.parametrize(
    "words,expected_output", (
        (["gin","zen","gig","msg"], 2),
        (["a"], 1),
    )
)
def test_unique_morse_repr(words, expected_output):
    assert Solution().uniqueMorseRepresentations(words) == expected_output
