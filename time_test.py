import random
import time
import matplotlib.pyplot as plt
import numpy as np

from quick_select import QuickSelect, Util

solution = QuickSelect()

def quickselect(arr, k):
    return solution.quick_select(arr, k)

# Define the array length range for testing
array_lengths = [10**1, 10**2, 10**3, 10**4, 10**5, 10**6]

# Lists to store the measured times and O(n) times
measured_times = []
on_times = []

for length in array_lengths:
    # Generate a random array and a random position
    arr = Util.Generate_random_array(length)
    k = random.randint(1, length)  # Generate a random position within the array length
    
    # Run the test 100 times and measure the time
    total_time = 0
    num_runs = 100

    for _ in range(num_runs):
        start_time = time.perf_counter()

        # Call the quickselect function
        result = quickselect(arr, k)

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        total_time += elapsed_time

    # Calculate the average running time
    average_time = total_time / num_runs
    measured_times.append(average_time)
    
    # Calculate the expected O(n) time for comparison
    on_time = length / 1000000  # Assuming 1 microsecond per element
    on_times.append(on_time)

    # Print the results and average running time
    print(f"Array length: {length}, {k}th smallest element is {result}")
    print(f"Average running time: {average_time} seconds")
    
    # Plot the measured times and O(n) times
plt.figure(figsize=(10, 6))
plt.plot(np.log10(array_lengths), measured_times, label='Measured Time (seconds)')
plt.plot(np.log10(array_lengths), on_times, label='O(n) Time', linestyle='--')
plt.xlabel('Log(Array Length)')
plt.ylabel('Time (seconds)')
plt.legend()

# Scale the O(n) time for comparison
scaling_factor = measured_times[5] / on_times[5]
scaled_on_times = [on_time * scaling_factor for on_time in on_times]
plt.plot(np.log10(array_lengths), scaled_on_times, label='Scaled O(n) Time')

plt.legend()
plt.title('Time Complexity Comparison')
plt.show()
