class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur_index: int, subset: List[int]) -> None:
            res.append(subset[:])
            processed = set()

            for index in range(cur_index, len(nums)):
                if index > 0 and nums[index - 1] == nums[index]:
                    continue

                subset.append(nums[index])
                dfs(index + 1, subset)
                subset.pop()

        nums.sort()
        dfs(0, [])

        return res

