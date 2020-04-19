#!/usr/bin/env python
'''
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

#第一遍
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            begin = nums[0]
            c=1
            n=0
            for item in nums[1:]:
                n+=1
                if item == begin:
                    continue
                else:
                    if n > c:
                        nums[c] = item
                    c+=1
                    begin = item
            return c
        else:
            return 0
#看解析后优化：
class Solution1(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = 0
        if nums:
            now=0
            for item in nums[1:]:
                now+=1
                if item != nums[n]:
                    n+=1
                    if now > n:
                        nums[n]=item
            n+=1
        return n