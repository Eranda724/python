class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in range(len(nums2)):
            nums1.append(nums2[i])

        nums1.sort()
        for i in range(len(nums1)):
            if(len(nums1)%2==0):
                return (nums1[len(nums1)//2]+nums1[(len(nums1)//2)-1])/2
            else:
                return nums1[len(nums1)//2]
            