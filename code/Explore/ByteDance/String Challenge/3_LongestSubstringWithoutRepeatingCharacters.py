class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result, temp = 0, []
        for item in s:
            if item in temp:
                if result < len(temp):
                    result = len(temp)
                temp = temp[temp.index(item)+1:]
                temp.append(item)
            else:
                temp.append(item)
        return max(result, len(temp))