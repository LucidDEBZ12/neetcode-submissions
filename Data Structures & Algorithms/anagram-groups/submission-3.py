class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary: key = character frequency tuple
        # value = list of anagrams
        hashmap = defaultdict(list)

        # Iterate through each word
        for word in strs:

            # Frequency array for 26 lowercase letters
            count = [0] * 26

            # Count each character
            for char in word:
                count[ord(char) - ord('a')] += 1

            # Convert list to tuple (hashable) and use as key
            hashmap[tuple(count)].append(word)

        # Return all grouped anagrams
        return list(hashmap.values())