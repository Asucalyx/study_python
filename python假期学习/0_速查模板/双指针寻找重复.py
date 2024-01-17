# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         slow, fast = 0, 1
#         while fast < len(nums):
#             if nums[fast] != nums[slow]:
#                 slow = slow + 1
#                 nums[slow] = nums[fast]
#             fast = fast + 1
#         return slow + 1
#
# nums = [0,0,1,1,1,2,2,3,3,4]; // 输入数组
