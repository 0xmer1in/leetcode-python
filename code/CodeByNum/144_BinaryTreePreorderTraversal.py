from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



"""
    @author: Merlin 2019.05.26
    144.Binary Tree Preorder Traversal
    思路: 前序遍历得到的顺序为左子树、根节点、右子树，根据这个特点进行递归
    time: O(n) space: O(n)
"""
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        self.dfs(root)
        return self.res

    def dfs(self, root: TreeNode):
        if not root: return
        self.res.append(root.val)
        self.dfs(root.left)
        self.dfs(root.right)
