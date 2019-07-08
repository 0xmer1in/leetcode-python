class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    @author: Merlin 2019.05.24
    98.Validate Binary Search Tree
    思路: 二叉搜索树的特征如下
    1.节点的左子树只包含小于当前节点的数。
    2.节点的右子树只包含大于当前节点的数。
    3.所有左子树和右子树自身必须也是二叉搜索树。
    根据以上三点，我们设定两个值，一个为最小值，一个为最大值
    当遍历左子树时，应把最大值设置为该子树的父节点的值，而遍历右子树则把最小值设成该子树的父节点的值。
    递归终止条件为当前节点不存在时返回True
    得出递推公式为dfs(root, _min, _max) = dfs(root.left, _min, root.val) and dfs(root.right, root.val, _max)
    注: 原本这题不需要在遍历左子树的时候设置最小值，但由于涉及边界值问题，只要设置最小值，对右子树遍历时同理，设置最大值以防超过边界。
    补充: 移位运算 1 << 63 = 2 ** 63
    time: O(n) space: O(n)
"""
import sys
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.valid(root, -sys.maxsize, sys.maxsize)

    def valid(self, root: TreeNode, _min: int, _max: int) -> bool:
        if not root: return True
        if root.val >= _max or root.val <= _min: return False
        return self.valid(root.left, _min, root.val) and self.valid(root.right, root.val, _max)
