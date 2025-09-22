// ID: 14
// Problem: Longest Common Prefix
// Difficulty: Easy
// Link: https://leetcode.com/problems/longest-common-prefix/
// Approach: Iteration with for loop over words + while loop to shrink 

public class LongestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) {
            return "";
        }

        // Start with the first word as the prefix
        String prefix = strs[0];

        // Compare with each word
        for (int i = 1; i < strs.length; i++) {
            // Keep trimming until current word starts with prefix
            while (!strs[i].startsWith(prefix)) {
                prefix = prefix.substring(0, prefix.length() - 1); // subtract char
                if (prefix.isEmpty()) {
                    return "";
                }
            }
        }
        return prefix;
    }

    public static void main(String[] args) {
        LongestCommonPrefix lcp = new LongestCommonPrefix();

        String[] test1 = { "flower", "flow", "flight" };
        String[] test2 = { "dog", "racecar", "car" };
        String[] test3 = { "interspecies", "interstellar", "interstate" };

        System.out.println(lcp.longestCommonPrefix(test1)); // Expected: "fl"
        System.out.println(lcp.longestCommonPrefix(test2)); // Expected: ""
        System.out.println(lcp.longestCommonPrefix(test3)); // Expected: "inters"
    }
}
