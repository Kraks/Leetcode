# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    def auxConnect(self, node):
        if node.left: self.auxConnectLeft(node.left, node)
        if node.right: self.auxConnectRight(node.right, node)
        
    def auxConnectLeft(self, node, parent):
        node.next = parent.right
        self.auxConnect(node)
    
    def auxConnectRight(self, node, parent):
        if parent.next:
            node.next = parent.next.left
        else:
            node.next = None
        self.auxConnect(node)
        
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root: 
            root.next = None
            if root.left: self.auxConnectLeft(root.left, root)
            if root.right: self.auxConnectRight(root.right, root)
        

