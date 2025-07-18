class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        nums_sorted = sorted(nums1)

        idx = len(nums_sorted) // 2

        if len(nums_sorted) % 2 != 0:
            return nums_sorted[idx]

        return (nums_sorted[idx-1] + nums_sorted[idx]) / 2
