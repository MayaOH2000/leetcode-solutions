# ID: 169
# Problem: Majority Element
# Difficulty: Easy
# Link: https://leetcode.com/problems/majority-element/
# Approach: Hash Map (dictionary)

from typing import List

def majorityElement(nums: List[int]) -> int:
    min_count = len(nums) // 2  # threshold: element must appear more than n/2 times
    num_count = {}  # dictionary to store counts for each number

    # Count occurrences of each number in the array
    for num in nums:
        if num in num_count:
            num_count[num] += 1  # increment count if number already seen
        else:
            num_count[num] = 1   # initialize count to 1 if number is new
    
    # Find the element that appears more than n/2 times
    for num, count in num_count.items():
        if count > min_count:
            return num


if __name__ == "__main__":
    print(majorityElement([3,2,3]))   # Output 3
    print(majorityElement([4,4,4,2,2,2,4])) # Ouput 4