class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 使用删除、添加函数
        for i, n in enumerate(nums):
            if n == 0:
                nums.remove(n)
                nums.append(n)
        #return nums

        # 参考快排，双指针
        j = 0
        for i in range(len(nums)):
            if (nums[i] != 0):
                t = nums[i]
                nums[i] = nums[j]
                nums[j] = t
                j += 1
        return nums
