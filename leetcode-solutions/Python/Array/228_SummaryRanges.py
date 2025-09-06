# ID: 228
# Problem: Summary Ranges
# Difficulty: Easy
# Link: https://leetcode.com/problems/summary-ranges/
# Approach: Two pointers (check for consecutive numbers)

from typing import List

def summaryRanges(nums: List[int]) -> List[str]:
    # Return empty list if input is empty
    if not nums:
        return []

    # start marks the beginning of the current range
    start = nums[0]
    # p1 is our current pointer in the array
    p1 = 0
    range_list = []

    while p1 < len(nums):
        # p2 searches ahead to find the end of the consecutive range
        p2 = p1 + 1
        while p2 < len(nums) and nums[p2] == nums[p2 - 1] + 1:
            p2 += 1

        # Record the range
        if start == nums[p2 - 1]:
            # Single number range (e.g., 7)
            range_list.append(str(start))
        else:
            # Multiple number range (e.g., 2->4)
            range_list.append(f"{start}->{nums[p2 - 1]}")

        # Move start to the next potential range
        if p2 < len(nums):
            start = nums[p2]

        # Move p1 to p2 to continue scanning
        p1 = p2
    return range_list



if __name__ == "__main__":
    print(summaryRanges([0,2,3,4,6,8,9]))   # Output ["0","2->4","6","8->9"]
    print(summaryRanges([0,3,4])) # Output ["0","3->4"]