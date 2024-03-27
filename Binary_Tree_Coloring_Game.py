class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
      #min runtime(45 ms) T(C(N)=O(N)) and SC(N))=(O(1)) as it require no contigous memory allocation recursively 
        node=self.find_node(root,x)#node declare

        left=self.count_nodes_in_subtree(node.left,x)#left node declare
        right=self.count_nodes_in_subtree(node.right,x)#Right subtree declare

        parent_node=n-left-right-1#parent node declare
        target=(n//2)+1#target declare
        
        if left >= target or right>=target or parent_node>=target:return True#printing true to assigned target val
        return False#printing false toe the non target val
        
    def find_node(self,root,x):#find_node funct()declare
        if root is None:return None#initializing root node
        if root.val==x:return root#printing current root node val
            
        return self.find_node(root.left,x) or self.find_node(root.right,x)#finding both left and right sub tree node val
        

    def count_nodes_in_subtree(self,root,x):#count_nodes_in_subtree funct declare
        if root is None:return 0#inintialing root 
        if root.val==x:return root#printing current root node val

        return 1+ self.count_nodes_in_subtree(root.left,x) + self.count_nodes_in_subtree(root.right,x)#coutning nodes in each subtree
     
