class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    简洁版
    @author: Merlin 2019.05.23
    124.Binary Tree Maximum PathSum
    思路: 遍历至最深，self.max表示全局最大路径，每遍历一个结点返回局部最大路径，
    如一棵树的左右子树，你只能选择其最大的一端来作为路径的一部分，如果你把左右子树都作为路径一部分，就无法连接上它的父节点
    time: O(n) space: O(n)
"""
class Solution:
    def maxPathSum(self, root: TreeNode, ok=True) -> int:
        if not root: return 0
        l, r = self.maxPathSum(root.left, ok=False), self.maxPathSum(root.right, ok=False)
        self.max = max(getattr(self, 'max', float('-inf')), l + root.val + r)
        return self.max if ok else max(root.val + max(l, r), 0)


"""
    详细版
    @author: Merlin 2019.05.23
    124.Binary Tree Maximum PathSum
    思路: 思路如上
    time: O(n) space: O(n)
"""
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return 0
        left = max(0, self.helper(root.left))
        right = max(0, self.helper(root.right))
        self.res = max(self.res, root.val + left + right)
        return max(left, right) + root.val