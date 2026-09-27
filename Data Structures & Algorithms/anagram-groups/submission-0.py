class Solution:
    def groupAnagrams(self, strs):
        groups = {}

        for word in strs:
            freq = [0] * 26
            for c in word:
                freq[ord(c) - ord('a')] += 1

            signature = tuple(freq)

            if signature not in groups:
                groups[signature] = []
            groups[signature].append(word)

        return list(groups.values())
