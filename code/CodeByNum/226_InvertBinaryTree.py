class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    @author: Merlin 2019.05.24(没看答案做出来的)
    226.Invert Binary Tree
    思路: 翻转一棵二叉树就像从根节点竖着放一块镜子，把左子树照到右子树，把右子树照到左子树(或者想象成一棵3d的树顺时针或逆时针转了180°)
    1.利用递归，遍历到最深层时，开始交换父节点指向的左右节点
    2.从下往上一路交换，最后达成翻转二叉树
    time: O(n) space: O(n)
"""
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        self.dfs(root, root.left, root.right)
        return root

    def dfs(self, root, left, right):
        if not left and not right: return
        if left: self.dfs(left, left.left, left.right)
        if right: self.dfs(right, right.left, right.right)
        root.left, root.right = right, left
