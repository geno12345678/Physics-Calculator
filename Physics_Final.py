from email import message
import tkinter as tk
from tkinter import messagebox
import math

calculation_history = []
history_count = len(calculation_history)

def show_history():
    if history_count > 0:
        messagebox.showinfo("Calculation History", "\n".join(calculation_history))
    
    elif history_count == 0:
        messagebox.showerror("History = 0", "\n" "There is no history to show")
        
    else:
        messagebox.showerror("Unknown Error", "\n" "There was an unexpected error when fetching history_count, Could not execute!")
def clear_history():   
    if history_count > 0:
        calculation_history.clear()
        messagebox.showwarning("Array Clear", "\n" "CALCULATION HISTORY HAS BEEN CLEARED!")
    
    elif history_count == 0:
        messagebox.showerror("History = 0", "\n" "There is no history to clear")
       
    else:
        messagebox.showerror("Unkown Error", "\n" "There was an unexpected error when fetching history_count, Could not execute!")


def number_checker(value):
    try:
        return float(value)
    except ValueError:
        return None

def reset_entries(entries):
    for entry in entries:
        entry.delete(0, tk.END)

def hide_entries(entries):
    for entry in entries:
        entry.grid_remove()

def show_kinematics_calculation():
    hide_all_frames()
    kinematics_calculation_frame.pack(padx=20, pady=20, ipadx=10, ipady=10)

def show_shapes_calculation():
    hide_all_frames()
    shapes_calculation_frame.pack(padx=20, pady=20, ipadx=10, ipady=10)

def select_kinematic_calculation(calculation_type):
    calculation_type_label_kinematics.config(text=calculation_type)
    
    hide_entries([vi_label, vi_entry, a_label, a_entry, t_label, t_entry, vf_label, vf_entry, d_label, d_entry])
    
    if calculation_type == "Final Velocity":
        vi_label.grid()
        vi_entry.grid()
        a_label.grid()
        a_entry.grid()
        t_label.grid()
        t_entry.grid()
    elif calculation_type == "Initial Velocity":
        vf_label.grid()
        vf_entry.grid()
        a_label.grid()
        a_entry.grid()
        t_label.grid()
        t_entry.grid()
    elif calculation_type == "Time":
        vi_label.grid()
        vi_entry.grid()
        vf_label.grid()
        vf_entry.grid()
        a_label.grid()
        a_entry.grid()
    elif calculation_type == "Distance":
        vi_label.grid()
        vi_entry.grid()
        vf_label.grid()
        vf_entry.grid()
        t_label.grid()
        t_entry.grid()

def select_shape_calculation(shape_type):
    shape_type_label.config(text=shape_type)
    
    hide_entries([length_label, length_entry, width_label, width_entry, radius_label, radius_entry, base_label, base_entry, height_label, height_entry])
    
    if shape_type == "Rectangle":
        length_label.grid()
        length_entry.grid()
        width_label.grid()
        width_entry.grid()
    elif shape_type == "Circle":
        radius_label.grid()
        radius_entry.grid()
    elif shape_type == "Triangle":
        base_label.grid()
        base_entry.grid()
        height_label.grid()
        height_entry.grid()
    elif shape_type == "Square":
        length_label.grid()
        length_entry.grid()

def kinematic_equation_solver():
    calculation_type = calculation_type_label_kinematics.cget("text")
    
    if calculation_type == "Final Velocity":
        vi = number_checker(vi_entry.get())
        a = number_checker(a_entry.get())
        t = number_checker(t_entry.get())
        if vi is not None and a is not None and t is not None:
            vf = vi + a * t
            calculation_history.append(f"Initial Velocity: {vi}, Acceleration: {a}, Time: {t} - The final velocity is: {vf}")
            messagebox.showinfo("Result", f"The final velocity is: {vf}")
    elif calculation_type == "Initial Velocity":
        vf = number_checker(vf_entry.get())
        a = number_checker(a_entry.get())
        t = number_checker(t_entry.get())
        if vf is not None and a is not None and t is not None:
            vi = vf - a * t
            calculation_history.append(f"Final Velocity: {vf}, Acceleration: {a}, Time: {t} - The initial velocity is: {vi}")
            messagebox.showinfo("Result", f"The initial velocity is: {vi}")
    elif calculation_type == "Time":
        vi = number_checker(vi_entry.get())
        vf = number_checker(vf_entry.get())
        a = number_checker(a_entry.get())
        if vi is not None and vf is not None and a is not None and a != 0:
            t = (vf - vi) / a
            calculation_history.append(f"Initial Velocity: {vi}, Final Velocity: {vf}, Acceleration: {a} - The time is: {t}")
            messagebox.showinfo("Result", f"The time is: {t}")
        elif a == 0:
            messagebox.showerror("Error", "Acceleration cannot be zero.")
    elif calculation_type == "Distance":
        vi = number_checker(vi_entry.get())
        vf = number_checker(vf_entry.get())
        t = number_checker(t_entry.get())
        if vi is not None and vf is not None and t is not None:
            d = (vi + vf) * t / 2
            calculation_history.append(f"Initial Velocity: {vi}, Final Velocity: {vf}, Time: {t} - The distance is: {d}")
            messagebox.showinfo("Result", f"The distance is: {d}")

    reset_entries([vi_entry, vf_entry, a_entry, t_entry, d_entry])

def shape_calculator():
    shape_type = shape_type_label.cget("text")
    
    if shape_type == "Rectangle":
        length = number_checker(length_entry.get())
        width = number_checker(width_entry.get())
        if length is not None and width is not None:
            area = length * width
            perimeter = 2 * (length + width)
            calculation_history.append(f"Rectangle - Length: {length}, Width: {width} - The area is: {area}, The perimeter is: {perimeter}")
            messagebox.showinfo("Result", f"The area is: {area}, The perimeter is: {perimeter}")
    elif shape_type == "Circle":
        radius = number_checker(radius_entry.get())
        if radius is not None:
            area = math.pi * radius ** 2
            circumference = 2 * math.pi * radius
            calculation_history.append(f"Circle - Radius: {radius} - The area is: {area}, The circumference is: {circumference}")
            messagebox.showinfo("Result", f"The area is: {area}, The circumference is: {circumference}")
    elif shape_type == "Triangle":
        base = number_checker(base_entry.get())
        height = number_checker(height_entry.get())
        if base is not None and height is not None:
            area = 0.5 * base * height
            calculation_history.append(f"Triangle - Base: {base}, Height: {height} - The area is: {area}")
            messagebox.showinfo("Result", f"The area is: {area}")
    elif shape_type == "Square":
        length = number_checker(length_entry.get())
        if length is not None:
            area = length ** 2
            perimeter = 4 * length
            calculation_history.append(f"Square - Length: {length} - The area is: {area}, The perimeter is: {perimeter}")
            messagebox.showinfo("Result", f"The area is: {area}, The perimeter is: {perimeter}")

    reset_entries([length_entry, width_entry, radius_entry, base_entry, height_entry])

def hide_all_frames():
    kinematics_calculation_frame.pack_forget()
    shapes_calculation_frame.pack_forget()

root = tk.Tk()
root.title("Physics Calculator")

# Top Section
main_frame = tk.LabelFrame(root, text="Select Calculation Type")
main_frame.pack(padx=20, pady=20, ipadx=10, ipady=10)

kinematics_button = tk.Button(main_frame, text="Kinematics", command=show_kinematics_calculation)
kinematics_button.grid(row=0, column=0, padx=10, pady=5)

shapes_button = tk.Button(main_frame, text="Area/Perimeter", command=show_shapes_calculation)
shapes_button.grid(row=0, column=1, padx=10, pady=5)

# Mid Section

main_frame = tk.LabelFrame(root, text="History")
main_frame.pack(padx=20, pady=20, ipadx=10, ipady=10)

kinematics_button = tk.Button(main_frame, text="Show History", command=show_history)
kinematics_button.grid(row=0, column=0, padx=10, pady=5)

kinematics_button = tk.Button(main_frame, text="Clear History", command=clear_history)
kinematics_button.grid(row=0, column=1, padx=1, pady=5)

# Kinematics Calculation UI
kinematics_calculation_frame = tk.LabelFrame(root, text="Kinematics Calculation")
calculation_type_label_kinematics = tk.Label(kinematics_calculation_frame, text="Select Kinematic Type")
calculation_type_label_kinematics.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

final_velocity_button = tk.Button(kinematics_calculation_frame, text="Final Velocity", command=lambda: select_kinematic_calculation("Final Velocity"))
final_velocity_button.grid(row=1, column=0, padx=10, pady=5)

initial_velocity_button = tk.Button(kinematics_calculation_frame, text="Initial Velocity", command=lambda: select_kinematic_calculation("Initial Velocity"))
initial_velocity_button.grid(row=1, column=1, padx=10, pady=5)

time_button = tk.Button(kinematics_calculation_frame, text="Time", command=lambda: select_kinematic_calculation("Time"))
time_button.grid(row=2, column=0, padx=10, pady=5)

distance_button = tk.Button(kinematics_calculation_frame, text="Distance", command=lambda: select_kinematic_calculation("Distance"))
distance_button.grid(row=2, column=1, padx=10, pady=5)

vi_label = tk.Label(kinematics_calculation_frame, text="Initial Velocity:")
vi_label.grid(row=3, column=0, padx=10, pady=5)
vi_entry = tk.Entry(kinematics_calculation_frame)
vi_entry.grid(row=3, column=1, padx=10, pady=5)

vf_label = tk.Label(kinematics_calculation_frame, text="Final Velocity:")
vf_label.grid(row=4, column=0, padx=10, pady=5)
vf_entry = tk.Entry(kinematics_calculation_frame)
vf_entry.grid(row=4, column=1, padx=10, pady=5)

a_label = tk.Label(kinematics_calculation_frame, text="Acceleration:")
a_label.grid(row=5, column=0, padx=10, pady=5)
a_entry = tk.Entry(kinematics_calculation_frame)
a_entry.grid(row=5, column=1, padx=10, pady=5)

t_label = tk.Label(kinematics_calculation_frame, text="Time:")
t_label.grid(row=6, column=0, padx=10, pady=5)
t_entry = tk.Entry(kinematics_calculation_frame)
t_entry.grid(row=6, column=1, padx=10, pady=5)

d_label = tk.Label(kinematics_calculation_frame, text="Distance:")
d_label.grid(row=7, column=0, padx=10, pady=5)
d_entry = tk.Entry(kinematics_calculation_frame)
d_entry.grid(row=7, column=1, padx=10, pady=5)

kinematics_calculation_button = tk.Button(kinematics_calculation_frame, text="Calculate", command=kinematic_equation_solver)
kinematics_calculation_button.grid(row=8, column=0, columnspan=2, pady=10)

# Shapes Calculation UI
shapes_calculation_frame = tk.LabelFrame(root, text="Shape Calculation")
shape_type_label = tk.Label(shapes_calculation_frame, text="Select Shape Type")
shape_type_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

rectangle_button = tk.Button(shapes_calculation_frame, text="Rectangle", command=lambda: select_shape_calculation("Rectangle"))
rectangle_button.grid(row=1, column=0, padx=10, pady=5)

circle_button = tk.Button(shapes_calculation_frame, text="Circle", command=lambda: select_shape_calculation("Circle"))
circle_button.grid(row=1, column=1, padx=10, pady=5)

triangle_button = tk.Button(shapes_calculation_frame, text="Triangle", command=lambda: select_shape_calculation("Triangle"))
triangle_button.grid(row=2, column=0, padx=10, pady=5)

square_button = tk.Button(shapes_calculation_frame, text="Square", command=lambda: select_shape_calculation("Square"))
square_button.grid(row=2, column=1, padx=10, pady=5)

length_label = tk.Label(shapes_calculation_frame, text="Length:")
length_label.grid(row=3, column=0, padx=10, pady=5)
length_entry = tk.Entry(shapes_calculation_frame)
length_entry.grid(row=3, column=1, padx=10, pady=5)

width_label = tk.Label(shapes_calculation_frame, text="Width:")
width_label.grid(row=4, column=0, padx=10, pady=5)
width_entry = tk.Entry(shapes_calculation_frame)
width_entry.grid(row=4, column=1, padx=10, pady=5)

radius_label = tk.Label(shapes_calculation_frame, text="Radius:")
radius_label.grid(row=5, column=0, padx=10, pady=5)
radius_entry = tk.Entry(shapes_calculation_frame)
radius_entry.grid(row=5, column=1, padx=10, pady=5)

base_label = tk.Label(shapes_calculation_frame, text="Base:")
base_label.grid(row=6, column=0, padx=10, pady=5)
base_entry = tk.Entry(shapes_calculation_frame)
base_entry.grid(row=6, column=1, padx=10, pady=5)

height_label = tk.Label(shapes_calculation_frame, text="Height:")
height_label.grid(row=7, column=0, padx=10, pady=5)
height_entry = tk.Entry(shapes_calculation_frame)
height_entry.grid(row=7, column=1, padx=10, pady=5)

shapes_calculation_button = tk.Button(shapes_calculation_frame, text="Calculate", command=shape_calculator)
shapes_calculation_button.grid(row=8, column=0, columnspan=2, pady=10)

root.mainloop()
