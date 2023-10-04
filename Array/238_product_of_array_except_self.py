# Time: O(n)
# Space: O(1)
# uses idea of pre and post fix
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = 1, 1
        ans = len(nums) * [0]

        for i in range(len(nums)):
            ans[i] = pre
            pre *= nums[i]

        for j in range(len(nums)-1, -1, -1):
            ans[j] *= post
            post *= nums[j]

        return ans