class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
    递归解法
    @author: Merlin 2019.05.23
    236.Lowest Common Ancestor of a Binary Tree
    思路: 由于是普通的二叉树，不是二叉搜索树那样有规律，所以只能每个节点都遍历一遍
    time: O(n) space: O(n)
"""
class Solution_1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q): return root
        left, right = (self.lowestCommonAncestor(kid, p, q)
                       for kid in (root.left, root.right))
        return root if left and right else left or right


# python2
class Solution_2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        answer = []
        stack = [[root, answer]]
        while stack:
            top = stack.pop()
            (node, parent), subs = top[:2], top[2:]
            if node in (None, p, q):
                parent += node,
            elif not subs:
                stack += top, [node.right, top], [node.left, top]
            else:
                parent += node if all(subs) else max(subs),
        return answer[0]


# python2
class Solution_3:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def path(root, goal):
            path, stack = [], [root]
            while True:
                node = stack.pop()
                if node:
                    if node not in path[-1:]:
                        path += node,
                        if node == goal:
                            return path
                        stack += node, node.right, node.left
                    else:
                        path.pop()

        return next(a for a, b in zip(path(root, p), path(root, q))[::-1] if a == b)