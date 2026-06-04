class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def solve_med(merged) -> float:
            N = len(merged)
            lo,hi = 0, N - 1
            mid = (lo + hi) // 2
            if N % 2 == 0:
                next_elem = mid + 1
                add_res = float(merged[mid] + merged[next_elem])
                return (add_res / 2.0)
            else:
                return float(merged[mid])
        if not nums1:
            return solve_med(nums2)
        if not nums2:
            return solve_med(nums1)
        def solve(M: int, N: int):
            p1, p2, p3 = 0,0,0
            C=[]
            while p1 < M and p2 < N:
                if nums1[p1] <= nums2[p2]:
                    C.append(nums1[p1])
                    p1+=1
                    # p3+=1
                else:
                    C.append(nums2[p2])
                    p2+=1
                    # p3+=1
            while p1 < M:
                C.append(nums1[p1])
                p1+=1
                # p3+=1
            while p2 < N:
                C.append(nums2[p2])
                p2+=1
                # p3+=1
            return solve_med(C)
        return solve(len(nums1), len(nums2))