#ID: 14
#Problem: Longest Common Prefix
#Difficulty: Easy
#Link: https://leetcode.com/problems/longest-common-prefix/

from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    #Storing first word
    prefix = strs[0]

    # Compare prefix against each remaining word
    for word in strs[1:]:
        # Shorten prefix from the end until current word starts with it
        while not word.startswith(prefix):
            #slicing [start:end] (-1 start from end of word)
            prefix = prefix[:-1] #removed last char
        
            #Return empty string for no common prefix
            if prefix == "":
                return ""      
    return prefix


# Example test cases
if __name__ == "__main__":
    print(longestCommonPrefix(["flower","flow", "flight"])) #Output: "fl"
    print(longestCommonPrefix(["dog","cat","mouse"]))       #Output: ""

