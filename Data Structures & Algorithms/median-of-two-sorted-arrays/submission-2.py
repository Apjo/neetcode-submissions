class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median1, median2 = 0,0
        M,N = len(nums1), len(nums2)
        mid_loc = (M + N) // 2 + 1
        p1,p2=0,0
        for i in range(mid_loc):
            median2 = median1
            if p1 < M and p2 < N:
                if nums1[p1] <= nums2[p2]:
                    median1 = nums1[p1]
                    p1+=1
                else:
                    median1 = nums2[p2]
                    p2+=1
            elif p1 < M:
                median1 = nums1[p1]
                p1+=1
            else:
                median1 = nums2[p2]
                p2+=1
        if (M+N) % 2 == 1:
            return float(median1)
        else:
            return (median1 + median2) / 2.0