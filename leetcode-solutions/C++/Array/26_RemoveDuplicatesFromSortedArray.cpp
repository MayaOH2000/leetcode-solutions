// ID: 26
// Problem: Removed Duplicates from Sorted Array
// Difficulty: Easy
// Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
// Approch: Double Iteration (sorted array)

#include <iostream>
#include <vector>

using namespace std;

int removeDuplicates(vector<int>& nums) {
    // Edge case for empty array
    if (nums.empty()) {
        return 0;
    }

    int p1 = 0;
    int count = 0;

    while (p1 < nums.size()) {
        int p2 = p1 + 1;
        while (p2 < nums.size()) {
            if (nums[p1] == nums[p2]) {
                // Remove duplicate from vector where p2 pointing
                nums.erase(nums.begin() + p2);
                // Don't increment p2 since next element shifts into this position
            } else {
                p2++;
            }
        }
        count++; // Increment count value
        p1++;    // Moving p1 to next element in vector
    }

    return count;
}

int main() {
    //Test Case 1 
    vector<int> num = {0,0,1,1,2,3,4,5,6,6};
    cout << removeDuplicates(num)<<endl;

    //Test Case 2
    vector<int> num_2 = {};
    cout << removeDuplicates(num_2)<< endl;

    return 0;
}