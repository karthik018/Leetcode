"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
    	if not root:
    		return []
    		
        nodes = [root]
        res = []
        while nodes:
        	children = []
        	for n in nodes:
        		if n and n.children:
        			children.extend(n.children)
        			
        	if children:
        		values = [c.val for c in n.children]
				res.extend(values)
        	
        	nodes = children
       	
       	return depth
