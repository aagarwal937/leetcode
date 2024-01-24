# NOTE: 1457. Pseudo-Palindromic Paths in a Binary Tree

# Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

# Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

 

# Example 1:

# Input: root = [2,3,1,3,1,null,1]
# Output: 2 
# Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).



# Example 2:

# Input: root = [2,1,1,1,3,null,null,null,null,null,1]
# Output: 1 
# Explanation: The figure above represents the given binary tree. There are three paths \
                # going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. \
                # Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).



# Example 3:

# Input: root = [9]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [1, 105].
# 1 <= Node.val <= 9


# NOTE: IMPLEMENTATION ALGORITHM ===============================================
# Initialize a variable count to keep track of the number of pseudo-palindromic paths.

# Implement a helper function dfs(node, freq) to perform the DFS traversal. \
# The node parameter represents the current node being visited, and freq \
# is a list of size 10 to keep track of the frequency of each digit from 1 to 9 in the current path.

# Inside the dfs function:
# a. If the current node is None, return.
# b. Increment the frequency of the current node's value in freq by 1.
# c. If the current node is a leaf node (i.e., both left and right children are None):
# i. Check if the current path is pseudo-palindromic by counting the number of odd frequencies in freq. If there are at most one odd frequency, increment count by 1.
# d. Recursively call dfs for the left and right children of the current node, passing the updated freq list.
# e. Decrement the frequency of the current node's value in freq by 1 to backtrack.

# Call the dfs function with the root node and an empty freq list.

# Return the final value of count.


# SOLUTION: PYTHON3 ============================================================

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        count = 0
        freq = [0] * 10
        
        def dfs(node, freq):
            if not node:
                return
            
            freq[node.val] += 1
            
            if not node.left and not node.right:
                odd_count = sum(1 for f in freq if f % 2 == 1)
                if odd_count <= 1:
                    nonlocal count
                    count += 1
            
            dfs(node.left, freq)
            dfs(node.right, freq)
            
            freq[node.val] -= 1
        
        dfs(root, freq)
        return count
    
# TIME_COMPLEXITY: The time complexity of this solution is O(N), where N is the number of nodes in the binary tree, as we visit each node exactly once.

        