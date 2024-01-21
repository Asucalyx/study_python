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

# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         slow, fast = 0, 0
#         slow = nums[slow]
#         fast = nums[nums[fast]]
#         while slow != fast:
#             slow = nums[slow]
#             fast = nums[nums[fast]]
#
#         slow = 0
#         while slow != fast:
#             slow = nums[slow]
#             fast = nums[fast]
#         return slow

 # class Solution:
 #     def findDuplicate(self, nums: List[int]) -> int:
 #        temp = 0
 #        for i in nums:
 #            temp ^= i
 #        return temp