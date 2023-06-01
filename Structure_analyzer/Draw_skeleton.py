import csv
from tkinter import *
from tkinter import simpledialog
import math

# Global variables
canvas_width = 1200
canvas_height = 600
grid_spacing = 20
current_tool = "line"
line_start = None
node_count = 0
element_count = 0
nodes = []
elements = []

# Function to handle mouse click event
def draw(event):
    global node_count, element_count, line_start

    x = round(event.x / grid_spacing) * grid_spacing
    y = round(event.y / grid_spacing) * grid_spacing

    if current_tool == "line":
        if line_start is None:
            line_start = (x, y)
        else:
            x1, y1 = line_start
            x2, y2 = (x, y)

            existing_node_1 = None
            existing_node_2 = None
            for node in nodes:
                nx, ny = node[1:]
                if (nx, ny) == (x1, y1):
                    existing_node_1 = node[0]
                if (nx, ny) == (x2, y2):
                    existing_node_2 = node[0]

            if existing_node_1:
                node_name_1 = existing_node_1
            else:
                node_count += 1
                node_name_1 = "N" + str(node_count)
                nodes.append((node_name_1, x1, y1))
                canvas.create_oval(x1 - 2, y1 - 2, x1 + 2, y1 + 2, fill="black")
                canvas.create_text(x1, y1 - 12, text=node_name_1, fill="black", font=("Arial", 10))
                #print(node_name_1 + ":", (x1 - canvas_width/2) / grid_spacing, (canvas_height/2 - y1) / grid_spacing, "m")

            if existing_node_2:
                node_name_2 = existing_node_2
            else:
                node_count += 1
                node_name_2 = "N" + str(node_count)
                nodes.append((node_name_2, x2, y2))
                canvas.create_oval(x2 - 2, y2 - 2, x2 + 2, y2 + 2, fill="black")
                canvas.create_text(x2, y2 - 12, text=node_name_2, fill="black", font=("Arial", 10))
                #print(node_name_2 + ":", (x2 - canvas_width/2) / grid_spacing, (canvas_height/2 - y2) / grid_spacing, "m")

            element_count += 1
            element_name = "E" + str(element_count)
            elements.append((element_name, node_name_1, node_name_2))
            canvas.create_line(x1, y1, x2, y2, fill="black", width=2)
            canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=element_name, fill="black", font=("Arial", 10))
            #print(element_name + ":", node_name_1, node_name_2)
            
            line_start = None

# Function to change the current drawing tool
def change_tool(tool):
    global current_tool
    current_tool = tool

# Function to handle mouse motion event and update the crosshair cursor
def update_crosshair(event):
    x = round(event.x / grid_spacing) * grid_spacing
    y = round(event.y / grid_spacing) * grid_spacing
    crosshair_coords = [x - grid_spacing, y, x + grid_spacing, y, x, y - grid_spacing, x, y + grid_spacing]
    canvas.coords(crosshair, crosshair_coords)
    mouse_coords_label.config(text="Mouse Coordinates: ({:.2f}m, {:.2f}m)".format((x - canvas_width/2) / grid_spacing, (canvas_height/2 - y) / grid_spacing))

# Create the main window
root = Tk()
root.title("Skeleton creator (Prepared by-Santosh Katuwal)")

# Create a canvas widget
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Create grid lines
for x in range(0, canvas_width, grid_spacing):
    if x != canvas_width // 2:
        canvas.create_line(x, 0, x, canvas_height, fill="lightgray")
for y in range(0, canvas_height, grid_spacing):
    if y != canvas_height // 2:
        canvas.create_line(0, y, canvas_width, y, fill="lightgray")

# Create zero coordinate lines
canvas.create_line(0, canvas_height//2, canvas_width, canvas_height//2, fill="blue")
canvas.create_line(canvas_width//2, 0, canvas_width//2, canvas_height, fill="blue")

# Create crosshair cursor
crosshair = canvas.create_line(0, 0, 0, 0, fill="red")

# Create mouse coordinates label
mouse_coords_label = Label(root, text="Mouse Coordinates: (0.00m, 0.00m)")
mouse_coords_label.pack()

# Bind the left mouse button click event to the draw function
canvas.bind("<Button-1>", draw)

# Bind the mouse motion event to the update_crosshair function
canvas.bind("<Motion>", update_crosshair)

# Create tool buttons
line_button = Button(root, text="Line", command=lambda: change_tool("line"))
line_button.pack(side=LEFT)

# Start the main loop
root.mainloop()

# Save the recorded nodes and elements as separate CSV files
nodes_file = open("input\\nodes.csv", "w", newline="")
nodes_writer = csv.writer(nodes_file)
nodes_writer.writerow(["node_id", "x", "y"])
for node in nodes:
    nodes_writer.writerow([node[0], (node[1] - canvas_width/2) / grid_spacing, (canvas_height/2 - node[2]) / grid_spacing])
nodes_file.close()
#print("Nodes saved to 'nodes.csv' file.")

elements_file = open("input\elements.csv", "w", newline="")
elements_writer = csv.writer(elements_file)
elements_writer.writerow(["element_id", "x1", "y1", "x2", "y2"])
for element in elements:
    node1 = next((node for node in nodes if node[0] == element[1]), None)
    node2 = next((node for node in nodes if node[0] == element[2]), None)
    if node1 and node2:
        elements_writer.writerow([element[0], (node1[1] - canvas_width/2) / grid_spacing, (canvas_height/2 - node1[2]) / grid_spacing,
                                  (node2[1] - canvas_width/2) / grid_spacing, (canvas_height/2 - node2[2]) / grid_spacing])
elements_file.close()
#print("Elements saved to 'elements.csv' file.")
#root.quit()
