import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt

class ExpenseManager:
    def __init__(self):
        self.expenses = []  # [date, category, amount, description]
        self.categories = [
            "Food", "Transport", "Housing", "Books & Stationery",
            "Internet & Phone", "Clothing", "Entertainment",
            "College Fees", "Miscellaneous"
        ]

    def add_expense(self, date, category, amount, description):
        if category not in self.categories:
            return False, "Invalid category"
        self.expenses.append([date, category, amount, description])
        return True, "Expense added successfully"

    def get_expenses_by_category(self):
        totals = {cat: 0 for cat in self.categories}
        for _, cat, amt, _ in self.expenses:
            totals[cat] += amt
        return totals


class ExpenseTrackerApp:
    def __init__(self, root):
        self.manager = ExpenseManager()
        root.title("Expense Tracker")
        root.geometry("800x600")

        # Input Section
        input_frame = ttk.Frame(root)
        input_frame.pack(fill=tk.X)

        labels = ["Date", "Category", "Amount", "Description"]
        self.inputs = {}

        for i, label in enumerate(labels):
            ttk.Label(input_frame, text=f"{label}:").grid(row=0, column=i * 2)
            if label == "Category":
                self.inputs[label] = ttk.Combobox(input_frame, values=self.manager.categories)
            else:
                self.inputs[label] = ttk.Entry(input_frame)
            self.inputs[label].grid(row=0, column=i * 2 + 1)

        ttk.Button(input_frame, text="Add Expense", command=self.add_expense).grid(row=0, column=8)

        # Expense Table
        self.tree = ttk.Treeview(root, columns=labels, show="headings")
        for label in labels:
            self.tree.heading(label, text=label)
        self.tree.pack(expand=True, fill=tk.BOTH)

        # Action Buttons
        action_frame = ttk.Frame(root)
        action_frame.pack(fill=tk.X)
        ttk.Button(action_frame, text="Pie Chart", command=self.show_pie_chart).pack(side=tk.LEFT)

    def add_expense(self):
        try:
            date = self.inputs["Date"].get()
            category = self.inputs["Category"].get()
            amount = float(self.inputs["Amount"].get())
            description = self.inputs["Description"].get()
            success, msg = self.manager.add_expense(date, category, amount, description)

            if success:
                self.tree.insert("", tk.END, values=(date, category, f"₹{amount:.2f}", description))
                for field in self.inputs.values():
                    field.delete(0, tk.END) if isinstance(field, tk.Entry) else field.set("")
                messagebox.showinfo("Success", msg)
            else:
                messagebox.showerror("Error", msg)
        except ValueError:
            messagebox.showerror("Error", "Enter a valid amount.")

    def show_pie_chart(self):
        totals = self.manager.get_expenses_by_category()
        data = [(cat, amt) for cat, amt in totals.items() if amt > 0]

        if not data:
            messagebox.showinfo("Pie Chart", "No expenses recorded.")
            return

        labels, values = zip(*data)
        plt.pie(values, labels=labels, autopct="%1.1f%%")
        plt.title("Expenses by Category")
        plt.axis("equal")
        plt.show()


def main():
    root = tk.Tk()
    ExpenseTrackerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
