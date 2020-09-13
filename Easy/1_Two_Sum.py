from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}

        for index in range(len(nums)):
            diff = target - nums[index]
            if diff in index_map:
                return [index_map[diff], index]
            index_map[nums[index]] = index


test = Solution()
ret = test.two_sum([2, 7, 11, 15], 9)
print(ret)
