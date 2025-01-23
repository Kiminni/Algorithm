# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        def check_height(node):
            if not node:
                return 0 # 빈 노드
            hl = check_height(node.left)
            hr = check_height(node.right)

            if hl == -1 or hr == -1 or abs(hl - hr) > 1:
                return -1 # 균형 깨짐
            return max(hl, hr) + 1 # 현재 노드 높이
        return check_height(root) != -1