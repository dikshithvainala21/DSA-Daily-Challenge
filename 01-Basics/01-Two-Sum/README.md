# Two Sum

## 1. Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

You may assume that each input has exactly one solution, and you may not use the same element twice.

## 2. Examples

**Example 1**

Input:
- nums = [2, 7, 11, 15]
- target = 9

Output: [0, 1]

Explanation: nums[0] + nums[1] = 2 + 7 = 9.

**Example 2**

Input:
- nums = [3, 2, 4]
- target = 6

Output: [1, 2]

## 3. Approaches

### Approach 1: Brute Force

- Use two nested loops.
- Check every possible pair.
- Return indices when their sum equals the target.

Time Complexity: O(n²)

Space Complexity: O(1)

Implementation: `brute_force.py`

### Approach 2: Optimized Approach (HashMap)

- Use a Python dictionary.
- Calculate the complement: target - current number.
- Check whether the complement already exists.
- If it exists, return both indices.
- Otherwise, store the current number and its index.

Time Complexity: O(n) average

Space Complexity: O(n)

Implementation: `optimal_approach.py`

## 4. Complexity Comparison

| Approach    | Time         | Space |
|-------------|--------------|-------|
| Brute Force | O(n²)        | O(1)  |
| HashMap     | O(n) average | O(n)  |

## 5. Key Learnings

- Understanding nested loops.
- Learning Python dictionaries.
- Understanding HashMap-based optimization.
- Comparing time and space complexity.
- Improving problem-solving skills.

## 6. Problem Source

LeetCode: https://leetcode.com/problems/two-sum/