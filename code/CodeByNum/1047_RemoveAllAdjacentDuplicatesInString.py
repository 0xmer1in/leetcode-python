"""
    @author: Merlin 2019.06.23
    1047. Remove All Adjacent Duplicates In String
    思路: 像匹配括号一样，用栈实现，当前遍历的字符和栈顶相等就弹出栈顶元素，否则添加进栈
    time: O(n) space: O(n)
"""
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        top = -1
        for s in S:
            if not stack:
                stack.append(s)
            else:
                if stack[-1] == s:
                    stack.pop()
                else:
                    stack.append(s)

        return ''.join(stack)