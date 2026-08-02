class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        left, right = 0, len(A)

        while left <= right:
            num_A = (left + right) // 2
            num_B = half - num_A

            Aleft = A[num_A - 1] if num_A > 0 else float("-inf")
            Aright = A[num_A] if num_A < len(A) else float("inf")

            Bleft = B[num_B - 1] if num_B > 0 else float("-inf")
            Bright = B[num_B] if num_B < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return min(Aright, Bright)

                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            if Aleft > Bright:
                right = num_A - 1
            else:
                left = num_A + 1