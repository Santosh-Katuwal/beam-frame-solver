import csv
from tkinter import Tk, Radiobutton, IntVar, font, Label, Button
import pandas as pd

nodes=pd.read_csv('input\\nodes.csv')
n=len(nodes)

root = Tk()
root.title("Assign Supports (Prepared by: Santosh Katuwal)")
root.geometry("600x400")
root.configure(bg="#F5F5F5")

# Define radio button styles
radio_button_style = {
    "font": font.Font(family="Arial", size=10),
    "activeforeground": "black",
    "bg": "#F5F5F5",
}



# Create node labels
node_labels=[]
for i in range(n):
    node_labels.append("N"+str(i+1))
# Create radio buttons
radio_buttons = []
radio_button_vars = []

for i, node_label in enumerate(node_labels):
    var = IntVar()

    node_label = Label(root, text=node_label, bg="#F5F5F5", font=font.Font(family="Arial", size=12))
    node_label.grid(row=i, column=0, pady=10, padx=20, sticky="w")

    radio_button_roller = Radiobutton(root, text="Roller", variable=var, value=1, **radio_button_style)
    radio_button_hinged = Radiobutton(root, text="Hinged", variable=var, value=2, **radio_button_style)
    radio_button_fixed = Radiobutton(root, text="Fixed", variable=var, value=3, **radio_button_style)
    radio_button_internal_hinge = Radiobutton(root, text="Internal Hinge", variable=var, value=4, **radio_button_style)

    radio_buttons.append([radio_button_roller, radio_button_hinged, radio_button_fixed, radio_button_internal_hinge])
    radio_button_vars.append(var)

    radio_button_roller.grid(row=i, column=1, pady=10, padx=20)
    radio_button_hinged.grid(row=i, column=2, pady=10, padx=20)
    radio_button_fixed.grid(row=i, column=3, pady=10, padx=20)
    radio_button_internal_hinge.grid(row=i, column=4, pady=10, padx=20)

# Function to capture checked radio button with node name and save as CSV
def capture_checked_button():
    supports = []
    for i, var in enumerate(radio_button_vars):
        if var.get() != 0:
            node_name = node_labels[i]
            selected_option = radio_buttons[i][var.get() - 1]["text"]
            supports.append((node_name, selected_option))
    
    # Save supports as CSV file
    with open("input\\supports.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Node", "Support"])
        writer.writerows(supports)
    
    print("Supports saved as supports.csv")

# Create button to capture checked radio button and save as CSV
capture_button = Button(root, text="Transfer Checked", command=capture_checked_button, bg="#4CAF50", fg="white", font=font.Font(family="Arial", size=12), relief="raised", padx=20, pady=10)
capture_button.grid(row=6, column=0, columnspan=5, pady=20)

root.mainloop()
