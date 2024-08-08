import tkinter as tk
from tkinter import ttk, messagebox

class RestaurantManagementSystem(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Restaurant Management System")
        self.geometry("800x600")
        self.configure(bg="#333333")

        self.menu = {
            "Fresh Items": {
                "Fresh Lime Water": 60,
                "Fresh Lime Soda": 80,
                "Fresh Fruit Salad": 80
            },
            "Tandoori": {
                "Soya Masala Tikka": 120,
                "Soya Malai Tikka": 130,
                "Paneer Tikka Masala": 140,
                "Paneer Malai Tikka": 150
            },
            "Pizzas": {
                "Margherita Pizza": 200,
                "Pepperoni Pizza": 250,
                "BBQ Chicken Pizza": 300
            },
            "Roti": {
                "Tandoori Roti": 20,
                "Butter Naan": 30,
                "Garlic Naan": 40
            },
            "Paneer Sabzee": {
                "Paneer Butter Masala": 180,
                "Shahi Paneer": 200,
                "Kadai Paneer": 220
            }
        }

        self.orders = {}  # Dictionary to store orders by table number
        self.prompt_open = False  # Flag to track if a prompt is open
        self.create_widgets()

    def create_widgets(self):
        # Header Label
        self.header_label = ttk.Label(self, text="Mayuri", font=("Helvetica", 24, "bold"), background="#333333", foreground="#ffffff")
        self.header_label.pack(pady=20)

        self.label = ttk.Label(self, text="Choose an action:", font=("Helvetica", 18), background="#333333", foreground="#ffffff")
        self.label.pack(pady=20)

        self.take_order_button = ttk.Button(self, text="Take Order", command=self.take_order)
        self.take_order_button.pack(pady=10)

        self.manage_order_button = ttk.Button(self, text="Manage Order", command=self.manage_order)
        self.manage_order_button.pack(pady=10)

        self.manage_tables_button = ttk.Button(self, text="Manage Tables", command=self.manage_tables)
        self.manage_tables_button.pack(pady=10)

        self.quit_button = ttk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack(pady=10)

        # Footer Label
        self.footer_label = ttk.Label(self, text="Arnav Tripathi", font=("Helvetica", 12), background="#333333", foreground="#ffffff")
        self.footer_label.pack(side=tk.BOTTOM, anchor='e', padx=20, pady=10)

    def take_order(self):
        if self.prompt_open:
            return
        self.prompt_open = True
        self.open_fullscreen_window(self.create_order_window)

    def create_order_window(self):
        self.order_window = tk.Toplevel(self)
        self.order_window.title("Take Order")
        self.order_window.geometry("800x600")
        self.order_window.configure(bg="#1e1e1e")

        self.table_label = ttk.Label(self.order_window, text="Table Number:", background="#1e1e1e", foreground="#ffffff")
        self.table_label.pack(pady=5)
        self.table_entry = ttk.Entry(self.order_window)
        self.table_entry.pack(pady=5)

        self.menu_label = ttk.Label(self.order_window, text="Menu:", font=("Helvetica", 14, "bold"), background="#1e1e1e", foreground="#ffffff")
        self.menu_label.pack(pady=10)

        self.menu_frame = tk.Frame(self.order_window, bg="#1e1e1e")
        self.menu_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        for category, items in self.menu.items():
            category_label = ttk.Label(self.menu_frame, text=category, font=("Helvetica", 12, "bold"), background="#1e1e1e", foreground="#ffffff")
            category_label.pack(anchor='w', pady=5)

            for item, price in items.items():
                frame = tk.Frame(self.menu_frame, bg="#1e1e1e")
                frame.pack(fill='x')
                label = ttk.Label(frame, text=f"{item} - {price} INR", font=("Helvetica", 12), background="#1e1e1e", foreground="#ffffff")
                label.pack(side='left', padx=10)
                button = ttk.Button(frame, text="Add", command=lambda item=item, category=category: self.prompt_quantity(category, item, "add"))
                button.pack(side='right')

        self.order_summary_label = ttk.Label(self.order_window, text="Order Summary:", font=("Helvetica", 14, "bold"), background="#1e1e1e", foreground="#ffffff")
        self.order_summary_label.pack(pady=10)
        self.order_summary = tk.Text(self.order_window, height=15, width=80, bg="#333333", fg="#ffffff")
        self.order_summary.pack(pady=5)

        self.confirm_order_button = ttk.Button(self.order_window, text="Confirm Order", command=self.confirm_order)
        self.confirm_order_button.pack(pady=10)

    def prompt_quantity(self, category, item, action):
        if self.prompt_open:
            return
        self.prompt_open = True
        self.open_fullscreen_window(lambda: self.create_quantity_window(category, item, action))

    def create_quantity_window(self, category, item, action):
        self.quantity_window = tk.Toplevel(self)
        self.quantity_window.title(f"Quantity for {item}")
        self.quantity_window.geometry("400x200")
        self.quantity_window.configure(bg="#1e1e1e")

        label = ttk.Label(self.quantity_window, text=f"Enter quantity to {action}:", background="#1e1e1e", foreground="#ffffff")
        label.pack(pady=10)
        self.quantity_entry = ttk.Entry(self.quantity_window)
        self.quantity_entry.pack(pady=10)

        if action == "add":
            confirm_button = ttk.Button(self.quantity_window, text="Add", command=lambda: self.add_item_to_order(category, item))
        elif action == "add_existing":
            confirm_button = ttk.Button(self.quantity_window, text="Add", command=lambda: self.add_item_to_existing_order(category, item))
        elif action == "remove_existing":
            confirm_button = ttk.Button(self.quantity_window, text="Remove", command=lambda: self.remove_item_from_existing_order(category, item))

        confirm_button.pack(pady=10)

    def open_fullscreen_window(self, create_window_function):
        create_window_function()
        self.prompt_open = False  # Reset flag when prompt is closed

    def add_item_to_order(self, category, item):
        try:
            table_number = int(self.table_entry.get())
            quantity = int(self.quantity_entry.get())

            if table_number not in self.orders:
                self.orders[table_number] = {"items": {}, "served": False}

            if item in self.orders[table_number]["items"]:
                self.orders[table_number]["items"][item]["quantity"] += quantity
            else:
                self.orders[table_number]["items"][item] = {"price": self.menu[category][item], "quantity": quantity}

            self.update_order_summary(table_number)
            self.quantity_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid table number and quantity.")

    def update_order_summary(self, table_number):
        self.order_summary.delete("1.0", tk.END)
        for item, details in self.orders[table_number]["items"].items():
            self.order_summary.insert(tk.END, f"{item}: {details['quantity']} @ {details['price']} INR each\n")

    def confirm_order(self):
        try:
            table_number = int(self.table_entry.get())
            if table_number in self.orders:
                messagebox.showinfo("Order Confirmed", f"Order confirmed for table {table_number}.")
                self.order_window.destroy()
            else:
                messagebox.showerror("Error", "No items added to the order.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid table number.")

    def manage_order(self):
        if self.prompt_open:
            return
        self.prompt_open = True
        self.open_fullscreen_window(self.create_manage_order_window)

    def create_manage_order_window(self):
        self.manage_order_window = tk.Toplevel(self)
        self.manage_order_window.title("Manage Order")
        self.manage_order_window.geometry("800x600")
        self.manage_order_window.configure(bg="#1e1e1e")

        self.table_label = ttk.Label(self.manage_order_window, text="Table Number:", background="#1e1e1e", foreground="#ffffff")
        self.table_label.pack(pady=5)
        self.table_entry = ttk.Entry(self.manage_order_window)
        self.table_entry.pack(pady=5)

        self.manage_button = ttk.Button(self.manage_order_window, text="Manage", command=self.manage_existing_order)
        self.manage_button.pack(pady=5)

    def manage_existing_order(self):
        try:
            table_number = int(self.table_entry.get())
            if table_number in self.orders:
                self.manage_existing_order_window = tk.Toplevel(self.manage_order_window)
                self.manage_existing_order_window.title(f"Manage Order for Table {table_number}")
                self.manage_existing_order_window.geometry("800x600")
                self.manage_existing_order_window.configure(bg="#1e1e1e")

                self.current_order_label = ttk.Label(self.manage_existing_order_window, text="Current Order:", font=("Helvetica", 14, "bold"), background="#1e1e1e", foreground="#ffffff")
                self.current_order_label.pack(pady=10)

                self.current_order_listbox = tk.Listbox(self.manage_existing_order_window, bg="#333333", fg="#ffffff")
                self.current_order_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

                self.update_current_order_listbox(table_number)

                self.add_remove_frame = tk.Frame(self.manage_existing_order_window, bg="#1e1e1e")
                self.add_remove_frame.pack(pady=10)

                self.add_item_button = ttk.Button(self.add_remove_frame, text="Add Item", command=lambda: self.prompt_quantity(self.get_selected_menu_item(), "add_existing"))
                self.add_item_button.pack(side=tk.LEFT, padx=5)

                self.remove_item_button = ttk.Button(self.add_remove_frame, text="Remove Item", command=lambda: self.prompt_quantity(self.get_selected_order_item(table_number), "remove_existing"))
                self.remove_item_button.pack(side=tk.LEFT, padx=5)

                self.menu_label = ttk.Label(self.manage_existing_order_window, text="Menu:", font=("Helvetica", 14, "bold"), background="#1e1e1e", foreground="#ffffff")
                self.menu_label.pack(pady=10)

                self.menu_listbox = tk.Listbox(self.manage_existing_order_window, selectmode=tk.SINGLE, bg="#333333", fg="#ffffff")
                self.menu_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

                for category, items in self.menu.items():
                    for item, price in items.items():
                        self.menu_listbox.insert(tk.END, f"{item} - {price} INR")

                self.update_current_order_listbox(table_number)
            else:
                messagebox.showerror("Error", "Table number not found.")
                self.manage_order_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid table number.")

    def get_selected_menu_item(self):
        selected_index = self.menu_listbox.curselection()
        if selected_index:
            item = self.menu_listbox.get(selected_index).split(" - ")[0]
            for category, items in self.menu.items():
                if item in items:
                    return category, item
        return None, None

    def get_selected_order_item(self, table_number):
        selected_index = self.current_order_listbox.curselection()
        if selected_index:
            item = self.current_order_listbox.get(selected_index).split(":")[0]
            return item
        return None

    def add_item_to_existing_order(self, category, item):
        try:
            table_number = int(self.table_entry.get())
            quantity = int(self.quantity_entry.get())

            if item in self.orders[table_number]["items"]:
                self.orders[table_number]["items"][item]["quantity"] += quantity
            else:
                self.orders[table_number]["items"][item] = {"price": self.menu[category][item], "quantity": quantity}

            self.update_current_order_listbox(table_number)
            self.quantity_window.destroy()
        except (ValueError, AttributeError):
            messagebox.showerror("Error", "Please enter a valid quantity and select an item.")

    def remove_item_from_existing_order(self, category, item):
        try:
            table_number = int(self.table_entry.get())
            quantity = int(self.quantity_entry.get())

            if item in self.orders[table_number]["items"]:
                if self.orders[table_number]["items"][item]["quantity"] <= quantity:
                    del self.orders[table_number]["items"][item]
                else:
                    self.orders[table_number]["items"][item]["quantity"] -= quantity
                self.update_current_order_listbox(table_number)
                self.quantity_window.destroy()
        except (ValueError, AttributeError):
            messagebox.showerror("Error", "Please enter a valid quantity and select an item.")

    def update_current_order_listbox(self, table_number):
        self.current_order_listbox.delete(0, tk.END)
        for item, details in self.orders[table_number]["items"].items():
            self.current_order_listbox.insert(tk.END, f"{item}: {details['quantity']} @ {details['price']} INR each")

    def manage_tables(self):
        if self.prompt_open:
            return
        self.prompt_open = True
        self.open_fullscreen_window(self.create_manage_tables_window)

    def create_manage_tables_window(self):
        self.manage_tables_window = tk.Toplevel(self)
        self.manage_tables_window.title("Manage Tables")
        self.manage_tables_window.geometry("800x600")
        self.manage_tables_window.configure(bg="#1e1e1e")

        self.table_listbox = tk.Listbox(self.manage_tables_window, bg="#333333", fg="#ffffff")
        self.table_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        for table_number in self.orders.keys():
            order_status = "Served" if self.orders[table_number]["served"] else "Not Served"
            self.table_listbox.insert(tk.END, f"Table {table_number} - {order_status}")

        self.serve_button = ttk.Button(self.manage_tables_window, text="Mark as Served", command=self.mark_as_served)
        self.serve_button.pack(pady=5)

        self.unserve_button = ttk.Button(self.manage_tables_window, text="Mark as Unserved", command=self.mark_as_unserved)
        self.unserve_button.pack(pady=5)

        self.complete_button = ttk.Button(self.manage_tables_window, text="Complete Order", command=self.complete_order)
        self.complete_button.pack(pady=5)

    def mark_as_served(self):
        selected_index = self.table_listbox.curselection()
        if selected_index:
            table_number = int(self.table_listbox.get(selected_index).split(" ")[1])
            self.orders[table_number]["served"] = True
            self.update_table_listbox()
        else:
            messagebox.showerror("Error", "Please select a table.")

    def mark_as_unserved(self):
        selected_index = self.table_listbox.curselection()
        if selected_index:
            table_number = int(self.table_listbox.get(selected_index).split(" ")[1])
            self.orders[table_number]["served"] = False
            self.update_table_listbox()
        else:
            messagebox.showerror("Error", "Please select a table.")

    def update_table_listbox(self):
        self.table_listbox.delete(0, tk.END)
        for table_number in self.orders.keys():
            order_status = "Served" if self.orders[table_number]["served"] else "Not Served"
            self.table_listbox.insert(tk.END, f"Table {table_number} - {order_status}")

    def complete_order(self):
        selected_index = self.table_listbox.curselection()
        if selected_index:
            table_number = int(self.table_listbox.get(selected_index).split(" ")[1])
            if self.orders[table_number]["served"]:
                total = sum(item["price"] * item["quantity"] for item in self.orders[table_number]["items"].values())
                gst = total * 0.05
                subtotal = total + gst

                messagebox.showinfo("Payment", f"Subtotal: {total} INR\nGST (5%): {gst} INR\nTotal: {subtotal} INR\nPayment secured.")

                del self.orders[table_number]
                self.update_table_listbox()
            else:
                messagebox.showerror("Error", "Order has not been served yet.")
        else:
            messagebox.showerror("Error", "Please select a table.")

if __name__ == "__main__":
    app = RestaurantManagementSystem()
    app.mainloop()
