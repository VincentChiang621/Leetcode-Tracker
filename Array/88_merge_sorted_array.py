# Time: O(m)
# Space: O(1)
# two pointer and modify nums1 from back
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for r in range(len(nums1)-1, -1, -1):
            if (n-1) < 0:
                break
            elif (m-1) < 0:
                nums1[0:n] = nums2[0:n]
                break
            if nums1[m-1] < nums2[n-1]:
                nums1[r] = nums2[n-1]
                n -= 1
            else:
                nums1[r] = nums1[m-1]
                m -= 1