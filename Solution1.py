"""
https://leetcode-cn.com/problems/two-sum/submissions/
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for (index, val) in enumerate(nums):
            another = target - val
            if another in map:
                return [map[another], index]
            map[val] = index


if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([3, 2, 4], 6))
