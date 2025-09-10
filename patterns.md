# LeetCode Patterns

Tracks common problem-solving patterns and example problems.

---

## Arrays
### Two Pointers
- **Description:** Use two indices to traverse an array, often from start/end or with slow/fast pointers. Helps reduce time complexity compared to nested loops.
- **Common Variations / Techniques:**
  - Opposite ends → merge, compare, or partition sorted arrays
  - Slow/fast → detect patterns, remove duplicates, or find cycles
- **Typical Use Cases:** Often used with sorted arrays
- **Example Problems:** 
  - #26 Remove Duplicates from Sorted Array
  - #27 Remove Element
  - #88 Merge Sorted Array
- **Status:** Learning / tentative
- **Notes / Tips:** Start pointers from the end for in-place merging to avoid overwriting

### Sliding Window
- Description: Maintain a window of elements to optimize subarray/subsequence problems.
- Example Problems:
  - TBD
- Status: Learning / tentative

### Prefix Sum
- **Description:** Keep a running total of sums in an array to quickly get the sum of any subarray.
- **Common Variations / Techniques:**
  - Calculate running totals (cumulative sums)
  - Handle multiple request (queries) on subarrays/ranges
- **Typical Use Cases:** Arrays with repeated range sum queries
- **Example Problems:**
  - #303 Range Sum Query
- **Status:** Learning / tentative
- **Notes / Tips:** For a range [i, j], sum = prefix[j] - prefix[i-1]. If i = 0, just use prefix[j].

---

## Strings
### Prefix Shrinking / Matching
- Description: Shorten or compare prefix among strings until a match is found.
- Example Problems:
  - #14 Longest Common Prefix
- Status: Learning / tentative

### Two Pointers
- Description: Compare characters from both ends.
- Example Problems:
  - TBD
- Status: Learning / tentative

---

## Bit Manipulation
### XOR (Exclusive OR)
- **Description:** Use XOR properties to find unique elements or differences. XOR cancels out identical values (`A ^ A = 0`) and preserves unique ones (`A ^ 0 = A`).
- **Common Variations / Techniques:**
 - Single unique element among duplicates
 - Finding missing numbers in sequences
 - Swapping variables without temp storage
- **Typical Use Cases:** 
 - **Red flags:** O(1) space constraint + duplicates + "bit manipulation" tag
 - Problems where identical elements should "cancel out"
 - Finding the odd-one-out in paired data
- **Key Properties:**
  - `A ^ A = 0` (same values cancel)
  - `A ^ 0 = A` (zero is neutral)
  - Order doesn't matter (commutative)
- Example Problems:
  - #136 Single Number

- **Status:** Learning / tentative
- **Notes / Tips:** When you see duplicates + O(1) space, think XOR before hash maps. Trace through small examples to verify cancellation works.

---

## Hash Maps
- Description: Store and retrieve key-value pairs efficiently.
- Example Problems:
  - #1 Two Sum (Revised)
- Status: Learning / tentative

---

## Dynamic Programming (DP)
- Description: A way to solve problems step by step by **reusing answers** from smaller problems. (In other words, break a big problem into smaller ones and build the solution incrementally.)  
- Intuition: Kind of like recursion (it repeats), but instead of doing the same work again and again, you **save the results** and build from them.  
- Example Problems:
  - TBD
- Status: Learning / tentative

---

## Trees
- Description: DFS / BFS traversals, recursive or iterative approaches.
- Example Problems:
  - TBD
- Status: Learning / tentative
