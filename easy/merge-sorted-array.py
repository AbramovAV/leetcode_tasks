class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end_ptr = m + n - 1
        i = m-1
        j = n-1
        while j>=0:
            if i<0 or nums1[i]<=nums2[j]:
                nums1[end_ptr] = nums2[j]
                j -= 1
            else:
                nums1[end_ptr] = nums1[i]
                i -= 1
            end_ptr -= 1