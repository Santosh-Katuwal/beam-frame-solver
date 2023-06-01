import tkinter as tk
from tkinter import ttk
import csv
import pandas as pd


nodes=pd.read_csv('input\\nodes.csv')
n=len(nodes)

def save_data():
    # Get the user input values
    node_values = []
    for node in nodes:
        force = node[0].get()
        angle = node[1].get()
        moment = node[2].get()
        if force or angle or moment:  # Ignore blank fields
            node_values.append([node[3], force, angle, moment])

    # Save the data to a CSV file
    with open('input\\node_load.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Node", "Force_kN", "Angle_Degrees", "Moment_kNm"])  # Write header
        writer.writerows(node_values)

    print("Data saved to 'node_load.csv'.")

# Create the main window
root = tk.Tk()
root.title("Input Point Load (Prepared by Santosh Katuwal)")
root.geometry("600x400")

# Styling
root.configure(bg='#f0f0f0')
root.option_add("*Font", "Arial 10")

# Create a canvas and scroll bar
canvas = tk.Canvas(root, bg='#f0f0f0', width=400, height=500)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the canvas to use the scroll bar
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Create a frame inside the canvas to hold the user form
frame = tk.Frame(canvas, bg='#f0f0f0')
canvas.create_window((0, 0), window=frame, anchor="nw")

# List to store the input fields
nodes = []

# Function to validate numeric input
def validate_numeric_input(value):
    if value.lstrip('-').isdigit():
        return True
    elif value == '':
        return True
    else:
        return False

# Create the user form
for i in range(n+1):  # Increase the range to add more rows
    # Create labels for node names
    node_label = tk.Label(frame, text="N" + str(i))
    node_label.configure(bg='#f0f0f0')
    node_label.grid(row=i, column=0, pady=5)

    # Create entry fields for force, angle, and moment
    force_entry = tk.Entry(frame, validate="key", width=10)
    force_entry.configure(validatecommand=(force_entry.register(validate_numeric_input), '%P'))
    force_entry.grid(row=i, column=1, pady=5)

    angle_entry = tk.Entry(frame, validate="key", width=10)
    angle_entry.configure(validatecommand=(angle_entry.register(validate_numeric_input), '%P'))
    angle_entry.grid(row=i, column=2, pady=5)

    moment_entry = tk.Entry(frame, validate="key", width=10)
    moment_entry.configure(validatecommand=(moment_entry.register(validate_numeric_input), '%P'))
    moment_entry.grid(row=i, column=3, pady=5)

    # Add the entry fields and node name to the nodes list
    nodes.append((force_entry, angle_entry, moment_entry, "N" + str(i)))

# Create the headings
heading_node = tk.Label(frame, text="Nodes")
heading_node.configure(font=("Arial", 10, "bold"), bg='#f0f0f0')
heading_node.grid(row=0, column=0, sticky="we", pady=10)

heading_force = tk.Label(frame, text="Force (kN)")
heading_force.configure(font=("Arial", 10, "bold"), bg='#f0f0f0')
heading_force.grid(row=0, column=1, sticky="we", pady=10)

heading_angle = tk.Label(frame, text="Angle (Degrees)")
heading_angle.configure(font=("Arial", 10, "bold"), bg='#f0f0f0')
heading_angle.grid(row=0, column=2, sticky="we", pady=10)

heading_moment = tk.Label(frame, text="Moment (kNm)")
heading_moment.configure(font=("Arial", 10, "bold"), bg='#f0f0f0')
heading_moment.grid(row=0, column=3, sticky="we", pady=10)

# Create the save button
save_button = tk.Button(root, text="Transfer Loads", command=save_data, width=15, bd=0, bg='#4CAF50', fg='white', relief='flat')
save_button.configure(font=("Arial", 12, "bold"))
save_button.pack(pady=10)

# Configure the scroll bar
canvas.configure(scrollregion=canvas.bbox("all"))

# Start the main loop
root.mainloop()
