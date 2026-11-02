class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow=fast=nums[0]
        while True:
            fast=nums[nums[fast]]
            slow=nums[slow]
            if slow==fast:
                break
        slow=nums[0]
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
        return slow