# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        nodes = [root]
        from collections import defaultdict
        while nodes:
        	d = defaultdict(list)
        	children = []
        	for n in nodes:
        		if n and n.left:
        			d[n.val].append(n.left.val)
        			children.append(n.left)
        		if n and n.right:
        			d[n.val].append(n.right.val)
        			children.append(n.right)
        	print(d)
        	is_x, is_y = False, False
        	for p, c in d.items():
        		if x in c and y in c:
        			return False
        		if x in c:
        			is_x = True
        		if y in c:
        			is_y = True
        			
        	if is_x ^ is_y:
        		return False
        	if is_x and is_y:
        		return True
        	
        	nodes = children
        			
        return is_x and is_y
