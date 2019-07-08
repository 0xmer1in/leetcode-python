class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res, cur = "", ""
        level = 0
        for i in range(len(S)):
            if S[i] == "(":
                if level: cur += "("
                level += 1
            else:
                level -= 1
                if level: cur += ")"
                else: res += cur; cur = ""
        return res