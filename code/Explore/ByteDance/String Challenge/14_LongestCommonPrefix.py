from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''

        for i, item in enumerate(zip(*strs)):
            if len(set(item)) > 1:
                return strs[0][:i]
        else:
            return min(strs)