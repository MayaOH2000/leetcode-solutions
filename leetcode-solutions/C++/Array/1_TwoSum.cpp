// ID: 1
// Problem: Two Sum
// Difficulty: Easy
// Link: https://leetcode.com/problems/two-sum/
// Approach: Iteration with for loops (track seen numbers and indices)

# include <iostream>
# include <vector>
# include <unordered_map>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    // Creating a hasmap/map (key: index, value: number)
    unordered_map<int,int> seen;

    for( int i = 0; i < nums.size(); ++i) {
        int current = nums[i];
        int missing = target - current;

        // Checking if missing been seen or not (in hasmap)
        if (seen.find(missing) != seen.end()){
            return {seen[missing], i};
        }

        // Add number into hasmap
        seen[current] = i;
    }

    return {}; // no solution found
}
   

// Test output of function
int main() {
    
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> result = twoSum(nums, target);

    if (!result.empty()) {
        cout << "Indices: " << result[0] << ", " << result[1] << endl;
    } else {
        cout << "No solution found." << endl;
    }

    return 0;
}
