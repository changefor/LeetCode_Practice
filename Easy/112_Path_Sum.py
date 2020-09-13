# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None and sum == root.val:
            return True
        left_ret = Solution().hasPathSum(root.left, sum - root.val)
        right_ret = Solution().hasPathSum(root.right, sum - root.val)
        return left_ret or right_ret

root = TreeNode(5)
left = TreeNode(4)
right = TreeNode(8)
root.left = left
root.right = right

tmp = root.left
left = TreeNode(11)
tmp.left = left
tmp = tmp.left
left = TreeNode(7)
right = TreeNode(2)
tmp.left = left
tmp.right = right

tmp = root.right
left = TreeNode(13)
right = TreeNode(4)
tmp.left = left
tmp.right = right
tmp = tmp.right
right = TreeNode(1)
tmp.right = right

s = Solution()
print(s.hasPathSum(root, 22))



