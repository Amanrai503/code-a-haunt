import cv2
from detect import run_dect



import tkinter as tk

def custom_detect():
    xml_file = (entry1.get())#'csds\\cascade.xml'
    w_name = (entry2.get())
    run_dect(xml_file,w_name)



# Create the main window
root = tk.Tk()
root.title("ML detector")

# Create entry fields
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

# Create a button to perform the addition
calculate_button = tk.Button(root, text="Detect", command=custom_detect)

# Arrange widgets using grid
entry1.grid(row=0, column=0)
entry2.grid(row=1, column=0)

calculate_button.grid(row=2, column=0)

# Start the GUI event loop
root.mainloop()

