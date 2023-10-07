import random
import time
import matplotlib.pyplot as plt
import numpy as np
import csv
from datetime import datetime
import os

from quick_select import QuickSelect, Util

solution = QuickSelect()

def quickselect(arr, k):
    return solution.quick_select(arr, k)

# Define the array length range for testing
array_lengths = []
n_range = 6
for i in range(1, n_range):
    array_lengths.extend([1 * (10 ** i), 4 * (10 ** i), 7 * (10 ** i)])
array_lengths.append(10 ** n_range)

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

# Scale the O(n) time for comparison
scaling_factor = measured_times[(n_range * 3) - 3] / on_times[(n_range * 3) - 3]
scaled_on_times = [on_time * scaling_factor for on_time in on_times]

# Get current date and time
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

# Create the directory for record files
record_dir = os.path.join('record', formatted_datetime)
os.makedirs(record_dir, exist_ok=True)

# Create the file name with date and time
csv_file_name = f"time_record_{formatted_datetime}.csv"
figure_file_name = f"time_comparison_figure_{formatted_datetime}.png"

# Write the data to a CSV file in the record directory
csv_file_path = os.path.join(record_dir, csv_file_name)
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Array Length", "Measured Time (seconds)", "O(n) Time", "Scaled O(n) Time"])
    
    for i in range(len(array_lengths)):
        writer.writerow([array_lengths[i], measured_times[i], on_times[i], scaled_on_times[i]])

# Plot the measured times and O(n) times
plt.figure(figsize=(10, 6))
plt.plot(np.log10(array_lengths), measured_times, label='Measured Time (seconds)')
plt.plot(np.log10(array_lengths), on_times, label='O(n) Time', linestyle='--')
plt.xlabel('Log(Array Length)')
plt.ylabel('Time (seconds)')
plt.legend()

plt.plot(np.log10(array_lengths), scaled_on_times, label='Scaled O(n) Time')

plt.legend()
plt.title('Time Complexity Comparison')

# Save the figure in the record directory
figure_file_path = os.path.join(record_dir, figure_file_name)
plt.savefig(figure_file_path)

# Show the figure
plt.show()
