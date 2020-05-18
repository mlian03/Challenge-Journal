class Solution:
    def maxSubarraySumCircular(self, A: [int]) -> int:
        # Get Sum of A
        summation = sum(A)
        # Pop A[0] and Initialise Variables to A[0]
        current_max = current_min = maximum_val = minimum_val = A.pop(0)

        # Loop through A
        for v in A:
            # Update Maximums
            current_max = max(current_max + v, v)
            maximum_val = max(current_max, maximum_val)
            # Update Minimums
            current_min = min(current_min + v, v)
            minimum_val = min(current_min, minimum_val)
        
        # Return Maximum Sum Circular Subarray
        if (summation == minimum_val):
            return maximum_val
        return max(maximum_val, summation - minimum_val)
