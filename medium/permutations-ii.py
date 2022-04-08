"""Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.



Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(nums, perm):
            if not nums:
                res.append(perm[:])
                return

            for i, num in enumerate(nums):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                perm.append(num)
                dfs(nums[:i] + nums[i + 1:], perm)
                perm.pop()

        nums.sort()
        dfs(nums, [])

        return res


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []

        for i, num in enumerate(nums):

            for j in range(len(nums) - 1):
                if j == i:
                    continue

                for n in nums[:j] + nums[j + 1:]:
                    perm.append(nums[j])

            res.append(perm)

        return res
