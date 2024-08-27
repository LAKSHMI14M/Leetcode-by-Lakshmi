# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        if key<root.val:
            root.left=self.deleteNode(root.left,key)
        elif key>root.val:
            root.right=self.deleteNode(root.right,key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            min_val=self.min_value(root.right)
            root.val=min_val.val
            root.right=self.deleteNode(root.right,min_val.val)
        return root
    def min_value(self,node):
        current=node
        while current.left is not None:
            current=current.left
        return current
        