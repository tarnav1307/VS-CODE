import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS income (
                    id INTEGER PRIMARY KEY,
                    source TEXT,
                    amount REAL,
                    date TEXT
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY,
                    category TEXT,
                    amount REAL,
                    date TEXT
                )
            ''')

    def add_income(self, source, amount, date):
        with self.conn:
            self.conn.execute("INSERT INTO income (source, amount, date) VALUES (?, ?, ?)",
                              (source, amount, date))

    def add_expense(self, category, amount, date):
        with self.conn:
            self.conn.execute("INSERT INTO expenses (category, amount, date) VALUES (?, ?, ?)",
                              (category, amount, date))

    def get_income(self, start_date, end_date):
        with self.conn:
            return self.conn.execute("SELECT * FROM income WHERE date BETWEEN ? AND ?",
                                     (start_date, end_date)).fetchall()

    def get_expenses(self, start_date, end_date):
        with self.conn:
            return self.conn.execute("SELECT * FROM expenses WHERE date BETWEEN ? AND ?",
                                     (start_date, end_date)).fetchall()

class FinanceManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Personal Finance Manager")
        self.geometry("600x400")

        self.db = Database('finances.db')

        self.create_widgets()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True)

        self.create_income_tab()
        self.create_expense_tab()
        self.create_report_tab()
        self.create_visualization_tab()

    def create_income_tab(self):
        income_frame = ttk.Frame(self.notebook)
        self.notebook.add(income_frame, text="Income")

        ttk.Label(income_frame, text="Source:").grid(row=0, column=0, padx=10, pady=10)
        self.income_source_entry = ttk.Entry(income_frame)
        self.income_source_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(income_frame, text="Amount:").grid(row=1, column=0, padx=10, pady=10)
        self.income_amount_entry = ttk.Entry(income_frame)
        self.income_amount_entry.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(income_frame, text="Date (YYYY-MM-DD):").grid(row=2, column=0, padx=10, pady=10)
        self.income_date_entry = ttk.Entry(income_frame)
        self.income_date_entry.grid(row=2, column=1, padx=10, pady=10)

        ttk.Button(income_frame, text="Add Income", command=self.add_income).grid(row=3, column=0, columnspan=2, pady=10)

    def add_income(self):
        source = self.income_source_entry.get()
        amount = self.income_amount_entry.get()
        date = self.income_date_entry.get()

        if not source or not amount or not date:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number!")
            return

        self.db.add_income(source, amount, date)
        messagebox.showinfo("Success", "Income added successfully!")
        self.income_source_entry.delete(0, tk.END)
        self.income_amount_entry.delete(0, tk.END)
        self.income_date_entry.delete(0, tk.END)

    def create_expense_tab(self):
        expense_frame = ttk.Frame(self.notebook)
        self.notebook.add(expense_frame, text="Expenses")

        ttk.Label(expense_frame, text="Category:").grid(row=0, column=0, padx=10, pady=10)
        self.expense_category_entry = ttk.Entry(expense_frame)
        self.expense_category_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(expense_frame, text="Amount:").grid(row=1, column=0, padx=10, pady=10)
        self.expense_amount_entry = ttk.Entry(expense_frame)
        self.expense_amount_entry.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(expense_frame, text="Date (YYYY-MM-DD):").grid(row=2, column=0, padx=10, pady=10)
        self.expense_date_entry = ttk.Entry(expense_frame)
        self.expense_date_entry.grid(row=2, column=1, padx=10, pady=10)

        ttk.Button(expense_frame, text="Add Expense", command=self.add_expense).grid(row=3, column=0, columnspan=2, pady=10)

    def add_expense(self):
        category = self.expense_category_entry.get()
        amount = self.expense_amount_entry.get()
        date = self.expense_date_entry.get()

        if not category or not amount or not date:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number!")
            return

        self.db.add_expense(category, amount, date)
        messagebox.showinfo("Success", "Expense added successfully!")
        self.expense_category_entry.delete(0, tk.END)
        self.expense_amount_entry.delete(0, tk.END)
        self.expense_date_entry.delete(0, tk.END)

    def create_report_tab(self):
        report_frame = ttk.Frame(self.notebook)
        self.notebook.add(report_frame, text="Reports")

        ttk.Label(report_frame, text="Start Date (YYYY-MM-DD):").grid(row=0, column=0, padx=10, pady=10)
        self.start_date_entry = ttk.Entry(report_frame)
        self.start_date_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(report_frame, text="End Date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=10)
        self.end_date_entry = ttk.Entry(report_frame)
        self.end_date_entry.grid(row=1, column=1, padx=10, pady=10)

        ttk.Button(report_frame, text="Generate Report", command=self.generate_report).grid(row=2, column=0, columnspan=2, pady=10)

    def generate_report(self):
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()

        if not start_date or not end_date:
            messagebox.showerror("Error", "Both start and end dates are required!")
            return

        report = self.create_report(start_date, end_date)
        if report:
            messagebox.showinfo("Report", report)
        else:
            messagebox.showinfo("Report", "No data available for the given date range.")

    def create_report(self, start_date, end_date):
        income = self.db.get_income(start_date, end_date)
        expenses = self.db.get_expenses(start_date, end_date)

        if not income and not expenses:
            return None

        income_df = pd.DataFrame(income, columns=["ID", "Source", "Amount", "Date"])
        expenses_df = pd.DataFrame(expenses, columns=["ID", "Category", "Amount", "Date"])

        total_income = income_df['Amount'].sum()
        total_expenses = expenses_df['Amount'].sum()
        savings = total_income - total_expenses

        report = f"Report from {start_date} to {end_date}\n"
        report += f"Total Income: ${total_income:.2f}\n"
        report += f"Total Expenses: ${total_expenses:.2f}\n"
        report += f"Savings: ${savings:.2f}\n"

        return report

    def create_visualization_tab(self):
        visualization_frame = ttk.Frame(self.notebook)
        self.notebook.add(visualization_frame, text="Visualization")

        ttk.Label(visualization_frame, text="Start Date (YYYY-MM-DD):").grid(row=0, column=0, padx=10, pady=10)
        self.visualization_start_date_entry = ttk.Entry(visualization_frame)
        self.visualization_start_date_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(visualization_frame, text="End Date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=10)
        self.visualization_end_date_entry = ttk.Entry(visualization_frame)
        self.visualization_end_date_entry.grid(row=1, column=1, padx=10, pady=10)

        ttk.Button(visualization_frame, text="Plot Expenses vs Income", command=self.plot_expenses_vs_income).grid(row=2, column=0, columnspan=2, pady=10)

    def plot_expenses_vs_income(self):
        start_date = self.visualization_start_date_entry.get()
        end_date = self.visualization_end_date_entry.get()

        if not start_date or not end_date:
            messagebox.showerror("Error", "Both start and end dates are required!")
            return

        self.plot_graph(start_date, end_date)

    def plot_graph(self, start_date, end_date):
        income = self.db.get_income(start_date, end_date)
        expenses = self.db.get_expenses(start_date, end_date)

        if not income and not expenses:
            plt.figure()
            plt.title("No data available for the given date range.")
            plt.show()
            return

        income_df = pd.DataFrame(income, columns=["ID", "Source", "Amount", "Date"])
        expenses_df = pd.DataFrame(expenses, columns=["ID", "Category", "Amount", "Date"])

        income_df['Date'] = pd.to_datetime(income_df['Date'])
        expenses_df['Date'] = pd.to_datetime(expenses_df['Date'])

        income_df = income_df.groupby('Date')['Amount'].sum()
        expenses_df = expenses_df.groupby('Date')['Amount'].sum()

        plt.figure(figsize=(10, 6))
        plt.plot(income_df, label="Income", color="green")
        plt.plot(expenses_df, label="Expenses", color="red")
        plt.title("Income vs Expenses")
        plt.xlabel("Date")
        plt.ylabel("Amount")
        plt.legend()
        plt.show()

if __name__ == "__main__":
    app = FinanceManagerApp()
    app.mainloop()
