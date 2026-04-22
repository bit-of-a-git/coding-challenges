from collections import defaultdict
from typing import List


class Solution:
    # This takes O(n * k)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                # Subtracting ord("a") from the ord of the character
                # converts c, for example, into 2
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())

    # This takes O(n * k log k) because sorted() takes O(k log k) in the best and average cases.
    def groupAnagramsFirstGo(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        # We go through strs
        # Store each word as a value for the key of its sorted variant
        for s in strs:
            sortedS = "".join(sorted(s))
            ans[sortedS].append(s)
        # We take just the values, and then convert that to a list
        return list(ans.values())
