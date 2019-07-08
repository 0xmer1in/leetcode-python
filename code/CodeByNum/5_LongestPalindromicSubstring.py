# 正常思路解法
# odd把i作为l和r传进去，even把i作为l，i+1作为r传进去
class Solution_1:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            odd = self.palindromeAt(s, i, i)
            even = self.palindromeAt(s, i, i+1)

            res = max(res, odd, even, key=len)
        return res

    def palindromeAt(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]


# 不正常思路解法(暂时看不懂)
class Solution_2:
    def longestPalindrome(self, s: str) -> str:
        maxLen, begin = 1, 0
        if len(s) < 2 or s == s[::-1]:
            return s
        for i in range(1, len(s)):
            odd = s[i - maxLen - 1:i + 1]
            even = s[i - maxLen:i + 1]

            if i - maxLen >= 1 and odd == odd[::-1]:
                begin = i - maxLen - 1
                maxLen += 2
                continue
            if i - maxLen >= 0 and even == even[::-1]:
                begin = i - maxLen
                maxLen += 1
        return s[begin:begin + maxLen]
