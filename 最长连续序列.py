class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        res = 0
        for i in nums:

            if i - 1 not in nums:
                # 只找每个序列的开头
                j = i + 1
                # 计算每个序列的长度
                while j in nums:
                    j += 1
                res = max(res, j - i)
        return res