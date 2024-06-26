class Solution(object):
    def findDifference(self, nums1, nums2):
        nums1,nums2=set(nums1),set(nums2)
        return list(nums1-nums2),list(nums2-nums1)
                    