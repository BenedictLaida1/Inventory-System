import json
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from tkinter import PhotoImage

def add_item(inventory, inventory_list):
    item_name = simpledialog.askstring("Add Item", "Enter item name:")
    if item_name:
        if item_name in inventory:
            messagebox.showinfo("Info", "Item already exists in the inventory.")
        else:
            try:
                quantity = int(simpledialog.askstring("Add Item", "Enter quantity:"))
                if quantity < 0:
                    messagebox.showerror("Error", "Quantity cannot be negative.")
                else:
                    inventory[item_name] = quantity
                    inventory_list.insert(tk.END, f"{item_name}: {quantity}")
                    messagebox.showinfo("Success", f"Item '{item_name}' added with quantity {quantity}.")
            except (ValueError, TypeError):
                messagebox.showerror("Error", "Invalid quantity. Please enter a number.")

def remove_item(inventory, inventory_list):
    selected = inventory_list.curselection()
    if selected:
        item = inventory_list.get(selected[0])
        item_name = item.split(":")[0].strip()
        del inventory[item_name]
        inventory_list.delete(selected[0])
        messagebox.showinfo("Success", f"Item '{item_name}' removed from inventory.")
    else:
        messagebox.showerror("Error", "No item selected.")

def update_item_quantity(inventory, inventory_list):
    selected = inventory_list.curselection()
    if selected:
        item = inventory_list.get(selected[0])
        item_name = item.split(":")[0].strip()
        try:
            quantity = int(simpledialog.askstring("Update Quantity", f"Enter new quantity for '{item_name}':"))
            if quantity < 0:
                messagebox.showerror("Error", "Quantity cannot be negative.")
            else:
                inventory[item_name] = quantity
                inventory_list.delete(selected[0])
                inventory_list.insert(selected[0], f"{item_name}: {quantity}")
                messagebox.showinfo("Success", f"Quantity for '{item_name}' updated to {quantity}.")
        except (ValueError, TypeError):
            messagebox.showerror("Error", "Invalid quantity. Please enter a number.")
    else:
        messagebox.showerror("Error", "No item selected.")

def save_inventory_to_file(inventory):
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if file_path:
        try:
            with open(file_path, 'w') as file:
                json.dump(inventory, file)
            messagebox.showinfo("Success", f"Inventory saved to '{file_path}'.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the file: {e}")

def load_inventory_from_file(inventory, inventory_list):
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        try:
            with open(file_path, 'r') as file:
                loaded_inventory = json.load(file)
            inventory.clear()
            inventory.update(loaded_inventory)
            inventory_list.delete(0, tk.END)
            for item, quantity in inventory.items():
                inventory_list.insert(tk.END, f"{item}: {quantity}")
            messagebox.showinfo("Success", f"Inventory loaded from '{file_path}'.")
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found.")
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Invalid file format.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while loading the file: {e}")

def main():
    inventory = {}

    root = tk.Tk()
    root.title("Inventory System")
    root.configure(bg="#1c1c1c")

    # Add Chrome Hearts Logo
    logo_frame = tk.Frame(root, bg="#1c1c1c")
    logo_frame.pack(pady=10)
    try:
        logo = PhotoImage(file="c:/Users/Administrator/Documents/Bene/InventorySystemProject/chromehearts_logo.png") 
        logo_label = tk.Label(logo_frame, image=logo, bg="#1c1c1c")
        logo_label.image = logo
        logo_label.pack()
    except Exception as e:
        print("Logo image not found. Proceeding without it.")

    title_label = tk.Label(root, text="Inventory System", font=("Old English Text MT", 24), bg="#1c1c1c", fg="#ffffff")
    title_label.pack(pady=5)

    # Chrome Hearts Cross Decorations
    cross_frame = tk.Frame(root, bg="#1c1c1c")
    cross_frame.pack()
    try:
        cross_image = PhotoImage(file="c:/Users/Administrator/Documents/Bene/InventorySystemProject/chromehearts_crossz.png")
        for _ in range(8):
            cross_label = tk.Label(cross_frame, image=cross_image, bg="#1c1c1c")
            cross_label.image = cross_image
            cross_label.pack(side=tk.LEFT, padx=5)
    except Exception as e:
        print("Cross image not found. Proceeding without it.")

    frame = tk.Frame(root, bg="#1c1c1c", bd=2, relief=tk.GROOVE)
    frame.pack(pady=10, padx=10)

    inventory_list = tk.Listbox(frame, width=50, height=15, bg="#2b2b2b", fg="white", font=("Helvetica", 12), selectbackground="#4f4f4f")
    inventory_list.pack(side=tk.LEFT, padx=5, pady=5)

    scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=inventory_list.yview, bg="#1c1c1c")
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    inventory_list.config(yscrollcommand=scrollbar.set)

    button_frame = tk.Frame(root, bg="#1c1c1c", bd=2, relief=tk.RAISED)
    button_frame.pack(pady=10)

    add_button = tk.Button(button_frame, text="Add Item", bg="#4f4f4f", fg="white", font=("Helvetica", 10, "bold"), command=lambda: add_item(inventory, inventory_list))
    add_button.grid(row=0, column=0, padx=5, pady=5)

    remove_button = tk.Button(button_frame, text="Remove Item", bg="#4f4f4f", fg="white", font=("Helvetica", 10, "bold"), command=lambda: remove_item(inventory, inventory_list))
    remove_button.grid(row=0, column=1, padx=5, pady=5)

    update_button = tk.Button(button_frame, text="Update Quantity", bg="#4f4f4f", fg="white", font=("Helvetica", 10, "bold"), command=lambda: update_item_quantity(inventory, inventory_list))
    update_button.grid(row=0, column=2, padx=5, pady=5)

    save_button = tk.Button(button_frame, text="Save Inventory", bg="#4f4f4f", fg="white", font=("Helvetica", 10, "bold"), command=lambda: save_inventory_to_file(inventory))
    save_button.grid(row=1, column=0, padx=5, pady=5)

    load_button = tk.Button(button_frame, text="Load Inventory", bg="#4f4f4f", fg="white", font=("Helvetica", 10, "bold"), command=lambda: load_inventory_from_file(inventory, inventory_list))
    load_button.grid(row=1, column=1, padx=5, pady=5)

    exit_button = tk.Button(button_frame, text="Exit", bg="#4f4f4f", fg="white", font=("Helvetica", 10, "bold"), command=root.destroy)
    exit_button.grid(row=1, column=2, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
