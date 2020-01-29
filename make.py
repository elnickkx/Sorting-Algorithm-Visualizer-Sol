from time import sleep
import visualizer as vs
import sorting as st

full_array = None

def set_all(self, values):
        for i in range(len(self.values)):
            self.values[i] = values[i]
        for i in range(len(self.values)):
            full_array[self.lower_index + i] = values[i]

def pigeonhole_sort(nums):
    # as for the evaluation finding the max and min index 
    num_max = max(nums)
    num_min = min(nums)

    # acclude the size of the valuable range in order to fit the pigeons
    gap_size = num_max - num_min + 1

    #pigeon_arr = [0]*ga(p_size # an array
    pigeon_arr = set_all(0)
        # populating the holes with pigeons in it

    for i in nums:
        pigeon_arr[i - num_min] += 1

    #num_len = nums.get_lens()

    # taking the count of initialisser and maximising the response 
    # minimising the iterations
    index = 0
    for take in range(gap_size):
        while pigeon_arr[take] > 0:
            pigeon_arr[take] -= 1

            nums[index] = take + num_min
            index += 1


a = [2,1,13,23,11,5,27,7,3]

pigeonhole_sort(a)

for i in range(0, len(a)):
    print(a[i])