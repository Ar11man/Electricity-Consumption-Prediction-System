import tkinter as tk
from tkinter import messagebox, simpledialog
from database import add_record, get_records, delete_record
from analysis import calculate_statistics
from graph import show_graph

window = tk.Tk()
window.title("Electricity Consumption Management System")
window.geometry("700x600")

title_label = tk.Label(window, text="Electricity Consumption Management System",
                       font=("Arial", 20, "bold"))
title_label.pack(pady=20)

tk.Label(window, text="Consumer Name:").pack()
name_entry = tk.Entry(window, width=40)
name_entry.pack(pady=5)

tk.Label(window, text="Date (YYYY-MM-DD):").pack()
date_entry = tk.Entry(window, width=40)
date_entry.pack(pady=5)

tk.Label(window, text="Units Consumed (kWh):").pack()
units_entry = tk.Entry(window, width=40)
units_entry.pack(pady=5)

def add_consumption():
    name = name_entry.get()
    date = date_entry.get()
    units = units_entry.get()

    if name == "" or date == "" or units == "":
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return

    try:
        units = float(units)
        add_record(name, date, units)
        messagebox.showinfo("Success", "Electricity record added successfully.")
        name_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
        units_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Units must be a number.")
    except Exception as error:
        messagebox.showerror("Database Error", str(error))

def delete_consumption():
    record_id = simpledialog.askinteger(
        "Delete Record",
        "Enter Record ID:"
    )

    if record_id is None:
        return

    deleted = delete_record(record_id)

    if deleted:
        messagebox.showinfo(
            "Success",
            "Record deleted successfully."
        )
    else:
        messagebox.showwarning(
            "Not Found",
            "Record ID does not exist."
        )

def view_records():
    records = get_records()
    if not records:
        messagebox.showinfo("Records", "No records found.")
        return

    record_text = ""
    for record in records:
        record_text += (f"ID: {record[0]} | Consumer: {record[1]} | "
                        f"Date: {record[2]} | Units: {record[3]} kWh\n")
    messagebox.showinfo("Electricity Records", record_text)

def show_statistics():
    records = get_records()
    result = calculate_statistics(records)

    if result is None:
        messagebox.showinfo("Statistics", "No records available.")
        return

    total, average, maximum, minimum = result
    message = (f"Total Consumption: {total:.2f} kWh\n\n"
               f"Average Consumption: {average:.2f} kWh\n\n"
               f"Maximum Consumption: {maximum:.2f} kWh\n\n"
               f"Minimum Consumption: {minimum:.2f} kWh")
    messagebox.showinfo("Consumption Statistics", message)

def display_graph():
    records = get_records()
    if not records:
        messagebox.showinfo("Graph", "No records available.")
        return
    show_graph(records)

tk.Button(window, text="Add Record", width=25, command=add_consumption).pack(pady=10)
tk.Button(window, text="View Records", width=25, command=view_records).pack(pady=5)
tk.Button(window, text="Delete Record", width=25, command=delete_consumption).pack(pady=5)
tk.Button(window, text="Calculate Statistics", width=25, command=show_statistics).pack(pady=5)
tk.Button(window, text="Show Graph", width=25, command=display_graph).pack(pady=5)

window.mainloop()
