import tkinter as tk
from tkinter import ttk
import csv
from pandas import read_csv

N_el = read_csv('input\\elements.csv')
n_el = len(N_el)

def save_data():
    # Create a list to store user inputs
    user_data = []

    # Append the column headings
    user_data.append(['Element', 'UDL', 'Angle'])

    # Iterate over each row
    for row, (udl_entry, angle_entry) in enumerate(zip(udl_entries, angle_entries)):
        # Get the UDL value from the corresponding entry
        udl_value = udl_entry.get()
        angle_value = angle_entry.get()

        # Check if the UDL value is not empty
        if udl_value and angle_value:
            # Append the row data to the user_data list
            user_data.append([f'E{row+1}', udl_value, angle_value])

    # Save user data to a CSV file
    with open('input\\udl.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(user_data)

    print("UDL data saved to 'udl.csv'.")
    # Display a message to indicate successful data saving
    status_label.config(text='Data saved successfully!')

# Create the main window
root = tk.Tk()
root.title('User Form')

# Set the window size
root.geometry('500x300')

# Create empty lists to store the entry widgets
udl_entries = []
angle_entries = []

# Create the label for the column headings
heading_label = tk.Label(root, text='UDL (kN/m)', font=('Arial', 12, 'bold'))
heading_label.grid(row=0, column=1, padx=10)

# Create the label for the Angle column
angle_label = tk.Label(root, text='Angle (Degrees)', font=('Arial', 12, 'bold'))
angle_label.grid(row=0, column=2, padx=10)

# Create a frame to contain the scrollable content
scroll_frame = ttk.Frame(root)
scroll_frame.grid(row=1, column=0, columnspan=3)

# Create a canvas widget to hold the scrollable content
canvas = tk.Canvas(scroll_frame, height=200)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a scrollbar and associate it with the canvas
scrollbar = ttk.Scrollbar(scroll_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame to hold the form fields
form_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=form_frame, anchor=tk.NW)

# Add labels and textboxes for each row
for row in range(n_el):
    # Create label for node name
    node_label = tk.Label(form_frame, text=f'E{row+1}', font=('Arial', 12))
    node_label.grid(row=row, column=0, padx=10)

    # Create entry for UDL value
    udl_entry = tk.Entry(form_frame, font=('Arial', 12))
    udl_entry.grid(row=row, column=1, padx=10)
    udl_entries.append(udl_entry)

    # Create entry for Angle value
    angle_entry = tk.Entry(form_frame, font=('Arial', 12))
    angle_entry.grid(row=row, column=2, padx=10)
    angle_entries.append(angle_entry)

# Update the scrollable area
form_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Create the Save button
save_button = tk.Button(root, text='Save', command=save_data, font=('Arial', 12, 'bold'))
save_button.grid(row=2, column=0, columnspan=3, pady=20)

# Create a label to display status messages
status_label = tk.Label(root, text='', font=('Arial', 12), fg='green')
status_label.grid(row=3, column=0, columnspan=3)

# Start the tkinter event loop
root.mainloop()
