# ID: 108
# Problem: Convert Sorted Array to Binary Search Tree
# Difficulty: Easy
# Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Approach: 

from typing import List, Optional

# Definition for a binary tree node.
# Given to you by leetcode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:



if __name__ == "__main__":
    print(sortedArrayToBST([-10,-3,0,5,9])) # Output [0,-3,9,-10,null,5]