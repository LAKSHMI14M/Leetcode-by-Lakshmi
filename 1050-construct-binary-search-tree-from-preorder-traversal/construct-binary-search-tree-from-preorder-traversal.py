# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root=TreeNode(preorder[0])
        left_subtree=[]
        right_subtree=[]
        for val in preorder[1:]:
            if val<root.val:
                left_subtree.append(val)
            else:
                right_subtree.append(val)
        root.left=self.bstFromPreorder(left_subtree)
        root.right=self.bstFromPreorder(right_subtree)
        return root