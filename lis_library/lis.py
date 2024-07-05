import bisect

class LongestIncreasingSubsequence:
    def __init__(self, sequence):
        self.sequence = sequence
        self.n = len(sequence)
        self.pred = [0] * self.n
        self.result = []
        self.lis_sequence = []

    # Fungsi Divide and Conquer
    def calculate_lis(self):
        def lis_util(start, end):
            if start == end:
                return [self.sequence[start]], [start]

            mid = (start + end) // 2
            left_lis, left_indices = lis_util(start, mid)
            right_lis, right_indices = lis_util(mid + 1, end)

            combined_lis, combined_indices = self.combine_lis(left_lis, right_lis, left_indices, right_indices)
            return combined_lis, combined_indices

        self.result, _ = lis_util(0, self.n - 1)
        return self.result

    def combine_lis(self, left_lis, right_lis, left_indices, right_indices):
        combined = []
        combined_indices = []

        i, j = 0, 0
        while i < len(left_lis) and j < len(right_lis):
            if left_lis[i] < right_lis[j]:
                combined.append(left_lis[i])
                combined_indices.append(left_indices[i])
                i += 1
            else:
                combined.append(right_lis[j])
                combined_indices.append(right_indices[j])
                j += 1

        while i < len(left_lis):
            combined.append(left_lis[i])
            combined_indices.append(left_indices[i])
            i += 1

        while j < len(right_lis):
            combined.append(right_lis[j])
            combined_indices.append(right_indices[j])
            j += 1

        self.update_predecessors(combined_indices)
        return combined, combined_indices

    def update_predecessors(self, combined_indices):
        for i in range(1, len(combined_indices)):
            if self.sequence[combined_indices[i]] > self.sequence[combined_indices[i - 1]]:
                self.pred[combined_indices[i]] = combined_indices[i - 1]

    # Fungsi Binary Search Tree
    def find_lis(self):
        lis_indices = []  # This will store the indices of the LIS elements
        predecessors = [-1] * self.n  # This will store the predecessors of each element in the LIS

        for i, num in enumerate(self.sequence):
            pos = bisect.bisect_left(self.lis_sequence, num)
            
            # If pos is equal to the length of lis_sequence, it means num is greater than all elements in lis_sequence
            if pos == len(self.lis_sequence):
                self.lis_sequence.append(num)
            else:
                self.lis_sequence[pos] = num

            # Update predecessors
            if pos > 0:
                predecessors[i] = lis_indices[pos - 1]
            
            # Update lis_indices
            if pos == len(lis_indices):
                lis_indices.append(i)
            else:
                lis_indices[pos] = i

        # Reconstruct the LIS from lis_indices
        lis_result = []
        k = lis_indices[-1]
        for _ in range(len(self.lis_sequence)):
            lis_result.append(self.sequence[k])
            k = predecessors[k]

        lis_result.reverse()
        self.result = lis_result
        self.pred = predecessors
        return self.result

    def get_lis_length(self):
        return len(self.result)
    
    def get_predecessors(self):
        return self.pred
