from lis_library import LongestIncreasingSubsequence

if __name__ == "__main__":
    arr1 = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    arr2 = [3, 10, 2, 1, 20]
    arr3 = [100, 180, 260, 310, 40, 535, 695]

    lis1 = LongestIncreasingSubsequence(arr1)
    lis2 = LongestIncreasingSubsequence(arr2)
    lis3 = LongestIncreasingSubsequence(arr3)

    print("LIS untuk arr1 adalah:", lis1.find_lis())  # Output: [10, 22, 33, 50, 60, 80]
    print("LIS untuk arr2 adalah:", lis2.find_lis())  # Output: [3, 10, 20]
    print("LIS untuk arr3 adalah:", lis3.find_lis())  # 

    print("LIS untuk arr1 adalah:", lis1.calculate_lis())  # Output: [10, 22, 33, 50, 60, 80]
    print("LIS untuk arr2 adalah:", lis2.calculate_lis())  # Output: [3, 10, 20]
    print("LIS untuk arr3 adalah:", lis3.calculate_lis())  # Output: [100, 180, 260, 310, 535, 695]

    print("Panjang LIS untuk arr1 adalah:", lis1.get_lis_length())  # Output: 6
    print("Panjang LIS untuk arr2 adalah:", lis2.get_lis_length())  # Output: 3
    print("Panjang LIS untuk arr3 adalah:", lis3.get_lis_length())  # Output: 6

    print("Predecessors untuk arr1 adalah:", lis1.get_predecessors())
    print("Predecessors untuk arr2 adalah:", lis2.get_predecessors())
    print("Predecessors untuk arr3 adalah:", lis3.get_predecessors())
