// ID: 1
// Problem: Two Sum
// Difficulty: Easy
// Link: https://leetcode.com/problems/two-sum/
// Approach: HashMap (track seen numbers and indices)

import java.util.HashMap;
import java.util.Map;

public class TwoSum {

    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int missingNum = target - nums[i];
            if (map.containsKey(missingNum)) {
                //Return index values of the associte numbers
                return new int[] { map.get(missingNum), i };
            }
            // Adds new value into hasmap (key,value)
            map.put(nums[i], i);
        }
        return new int[] {};
    }

    public static void main(String[] args) {
        int[] nums = { 2, 7, 11, 15 };
        int target = 9;
        TwoSum solver = new TwoSum();
        int[] result = solver.twoSum(nums, target);
        System.out.println("[" + result[0] + ", " + result[1] + "]");
    }

}
