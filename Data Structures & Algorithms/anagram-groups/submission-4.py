
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_dict = defaultdict(list)

        for s in strs:

            freq_array = [0] * 26

            for char in s:
                index = ord(char) - ord('a')
                freq_array[index] += 1

            key = tuple(freq_array)

            anagram_dict[key].append(s)

        return list(anagram_dict.values())
