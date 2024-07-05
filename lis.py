class LongestIncreasingSubsequence:
    def __init__(self, sequence):
        self.sequence = sequence
        self.n = len(sequence)
        self.pred = [0] * self.n
        self.result = []

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

    def get_lis_length(self):
        return len(self.result)
    
    def get_predecessors(self):
        return self.pred

# Contoh penggunaan
if __name__ == "__main__":
    arr1 = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    arr2 = [3, 10, 2, 1, 20]
    arr3 = [100, 180, 260, 310, 40, 535, 695]

    lis1 = LongestIncreasingSubsequence(arr1)
    lis2 = LongestIncreasingSubsequence(arr2)
    lis3 = LongestIncreasingSubsequence(arr3)

    print("LIS untuk arr1 adalah:", lis1.calculate_lis())  # Output: [10, 22, 33, 50, 60, 80]
    print("LIS untuk arr2 adalah:", lis2.calculate_lis())  # Output: [3, 10, 20]
    print("LIS untuk arr3 adalah:", lis3.calculate_lis())  # Output: [100, 180, 260, 310, 535, 695]

    print("Panjang LIS untuk arr1 adalah:", lis1.get_lis_length())  # Output: 6
    print("Panjang LIS untuk arr2 adalah:", lis2.get_lis_length())  # Output: 3
    print("Panjang LIS untuk arr3 adalah:", lis3.get_lis_length())  # Output: 6

    print("Predecessors untuk arr1 adalah:", lis1.get_predecessors())
    print("Predecessors untuk arr2 adalah:", lis2.get_predecessors())
    print("Predecessors untuk arr3 adalah:", lis3.get_predecessors())

