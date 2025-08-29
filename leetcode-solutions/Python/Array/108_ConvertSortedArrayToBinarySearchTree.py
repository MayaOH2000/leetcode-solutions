# ID: 108
# Problem: Convert Sorted Array to Binary Search Tree
# Difficulty: Easy
# Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Approach: Recursion (repeats itself)

from typing import List, Optional

# Definition for a binary tree node.
# Given to you by leetcode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    #Empty array -> no node
    if not nums:
        return None
    
    #Find root/ starting node
    middle = len(nums) // 2
    print(nums[middle])

    #Create root node
    root = TreeNode(nums[middle])

    # Create left subtree
    root.left = sortedArrayToBST(nums[:middle])

    # Creat right subtree
    root.right = sortedArrayToBST(nums[middle + 1:])

    return root


if __name__ == "__main__":
    print(sortedArrayToBST([-10,-3,0,5,9])) # Output [0,-3,9,-10,null,5]
    print(sortedArrayToBST([1,3])) # Output [3,1]