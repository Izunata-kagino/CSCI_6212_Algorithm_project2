import tkinter as tk
import time
import random

from quick_select import QuickSelect, Util

random_array = []
input_value = 56
quickselect = QuickSelect()

def run_function():
    global input_value
    start_time = time.perf_counter()  # Record the start time
    print("Select ", input_value, "th smallest.")
    for i in range(1000):
        input_value = random.randint(1, 100)
        result = quickselect.quick_select(random_array, input_value)
        print(f"The {input_value}th smallest element is: {result}")
    end_time = time.perf_counter()  # Record the end time

    elapsed_time = (end_time - start_time) / 1000  # Calculate the elapsed time
    result_label.config(text=f"Elapsed Time: {elapsed_time:.9f} seconds")
    
def generate_random_array():
    global random_array
    # Generate a random array of 10 integers between 1 and 100
    random_array = Util.Generate_random_array(100)
    # Display the random array in the text widget
    result_text.delete(1.0, tk.END)  # Clear previous content
    result_text.insert(tk.END, str(random_array))

# Create the main window
window = tk.Tk()
window.title("Function Timer")

# Create and configure a label to display the result
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Create a button to run the function and time it
run_button = tk.Button(window, text="Run Quick Select", command=run_function)
run_button.pack()

# Create a button to generate a random array
random_array_button = tk.Button(window, text="Generate Random Array", command=generate_random_array)
random_array_button.pack()

# Create a text widget to display the random array
result_text = tk.Text(window, height=7, width=80)
result_text.pack()

# Start the GUI main loop
window.mainloop()
