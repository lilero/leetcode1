class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 双重for循环
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        # 单for循环
        for i in range(len(nums)):
            res = target - nums[i]
            if res in nums[i+1:]:
                return [i, nums[i+1:].index(res) + (i+1)]

        # 哈希表
        d = {}
        n = len(nums)
        for x in range(n):
            if target - nums[x] in d:
                return [d[target - nums[x]], x]
            else:
                d[nums[x]] = x