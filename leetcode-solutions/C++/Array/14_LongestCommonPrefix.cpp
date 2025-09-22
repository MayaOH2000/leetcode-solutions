// ID: 14
// Problem: Longest Common Prefix
// Difficulty: Easy
// Link: https://leetcode.com/problems/longest-common-prefix/
// Approach: Iteration with for loop over words + while loop to shrink 

# include <iostream>
# include <vector>

using namespace std;

 string longestCommonPrefix(vector<string>& strs) {
        // Empty string returns nothing
        if (strs.empty()) {
            return "";
        }

        // Taking  first words as prefix in list
        string prefix = strs[0];

        for(int i = 1; i < strs.size(); ++i){
            // Remove last letter if current word does not match prefix
            while (strs[i].find(prefix) != 0){
                prefix = prefix.substr(0, prefix.size() - 1 );
                if (prefix.empty()){
                    return "";
                }
            }
        }
        return prefix;
    }


//Test Case 
int main(){

    // Case 1 
    vector<string> words = {"flower", "flow", "flight"};
    cout << "Output: " << longestCommonPrefix(words) << endl;

    // Case 2
    vector<string> words2 = {"dog", "log", "car", "racecar"};
    cout << "Output: " << longestCommonPrefix(words2) << endl;

    return 0;
}


