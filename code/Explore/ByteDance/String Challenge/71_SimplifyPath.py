class Solution:
    def simplifyPath(self, path: str) -> str:
        places = [item for item in path if item != '.' and item != '']
        stack = []
        for item in places:
            if item == '..':
                if stack: stack.pop()
            else:
                stack.append(item)
        return '/' + '/'.join(stack)