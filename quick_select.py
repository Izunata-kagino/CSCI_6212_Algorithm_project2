import random

class QuickSelect:
    def quick_select(self, arr, k):
        """
        Find the kth smallest element in an array using Quick Select algorithm.

        Args:
            arr (List[int]): The list of integers to search within.
            k (int): The rank of the element to find (1-based indexing).

        Returns:
            int: The kth smallest element in the list.

        """
        if len(arr) == 1:
            return arr[0]

        pivot = self.pick_pivot(arr)
        small_list, equal_list, large_list = [], [], []
        
        for num in arr:
            if num < pivot:
                small_list.append(num)
            elif num == pivot:
                equal_list.append(num)
            else:
                large_list.append(num)
        
        if k <= len(small_list):
            return self.quick_select(small_list, k)
        elif k <= len(small_list) + len(equal_list):
            return pivot
        else:
            return self.quick_select(large_list, k - len(small_list) - len(equal_list))

    def pick_pivot(self, nums):
        if len(nums) <= 5:
            nums.sort()
            return nums[len(nums) // 2]
        
        # Divide nums into groups of 5 and find medians
        medians = []
        for i in range(0, len(nums), 5):
            group = nums[i:i+5]
            group.sort()
            median = group[len(group) // 2]
            medians.append(median)
        
        # Recursively find the median of medians
        return self.quick_select(medians, len(medians) // 2)

class Util:
    def Generate_random_array(length):

        # Generate array
        array = list(range(1, length + 1))

        # Shuffle the array
        random.shuffle(array)
        return array

if __name__ == '__main__':
    # Example usage
    s = QuickSelect()
    n = 98

    # Generate array from 1 to n-1
    array = list(range(1, n))

    # Shuffle the array
    random.shuffle(array)
    select_position = random.randint(1, n)
    result = s.quick_select(array, select_position)
    print(f"The {select_position}th smallest element is: {result}")

