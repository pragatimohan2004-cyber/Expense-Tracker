import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

from core.models import Expense
from ui.charts import open_dashboard
from core.storage import (
    init_storage,
    save_expense,
    load_expenses,
    delete_expense,
    update_expense
)


def run_app():
    init_storage()

    root = tk.Tk()
    root.title("Expense Tracker Pro")
    root.geometry("1000x700")

    selected_id = None

    # ======================
    # INPUT AREA
    # ======================
    top = tk.Frame(root)
    top.pack(pady=15)

    tk.Label(top, text="Amount").grid(row=0, column=0, padx=5)
    amount = tk.Entry(top, width=15)
    amount.grid(row=0, column=1)

    tk.Label(top, text="Category").grid(row=0, column=2, padx=5)

    category = ttk.Combobox(
        top,
        width=15,
        state="readonly",
        values=[
            "Food", "Transport", "Housing",
            "Health", "Entertainment",
            "Shopping", "Utilities", "Other"
        ]
    )
    category.grid(row=0, column=3)
    category.current(0)

    tk.Label(top, text="Description").grid(row=0, column=4, padx=5)
    desc = tk.Entry(top, width=25)
    desc.grid(row=0, column=5)

    # ======================
    # SEARCH
    # ======================
    search_frame = tk.Frame(root)
    search_frame.pack()

    tk.Label(search_frame, text="Search").grid(row=0, column=0, padx=5)

    search_box = tk.Entry(search_frame, width=30)
    search_box.grid(row=0, column=1)

    # ======================
    # TOTAL
    # ======================
    total_label = tk.Label(
        root,
        text="Total: $0.00",
        font=("Arial", 14, "bold"),
        fg="green"
    )
    total_label.pack(pady=8)

    # ======================
    # TABLE
    # ======================
    cols = ("Date", "Amount", "Category", "Description")

    table = ttk.Treeview(
        root,
        columns=cols,
        show="headings",
        height=20
    )

    for c in cols:
        table.heading(c, text=c)

    table.column("Date", width=140)
    table.column("Amount", width=120)
    table.column("Category", width=170)
    table.column("Description", width=400)

    table.pack(pady=10)

    # ======================
    # FUNCTIONS
    # ======================
    def clear_fields():
        amount.delete(0, tk.END)
        desc.delete(0, tk.END)
        category.current(0)

    def refresh():
        for row in table.get_children():
            table.delete(row)

        rows = load_expenses()
        keyword = search_box.get().lower()

        total = 0

        for row in rows:
            line = f"{row['date']} {row['amount']} {row['category']} {row['description']}".lower()

            if keyword and keyword not in line:
                continue

            total += float(row["amount"])

            table.insert(
                "",
                tk.END,
                iid=row["id"],
                values=(
                    row["date"],
                    f"${float(row['amount']):,.2f}",
                    row["category"],
                    row["description"]
                )
            )

        total_label.config(text=f"Total: ${total:,.2f}")

    def add_expense_ui():
        try:
            item = Expense(
                amount=float(amount.get()),
                category=category.get(),
                description=desc.get(),
                date=str(date.today())
            )

            save_expense(item)
            clear_fields()
            refresh()

        except ValueError:
            messagebox.showerror("Error", "Invalid amount")

    def delete_selected():
        selected = table.selection()

        if not selected:
            messagebox.showwarning("Warning", "Select a row first.")
            return

        expense_id = int(selected[0])

        delete_expense(expense_id)
        clear_fields()
        refresh()

    def load_selected(event):
        nonlocal selected_id

        selected = table.selection()

        if not selected:
            return

        selected_id = int(selected[0])

        values = table.item(selected[0])["values"]

        amount.delete(0, tk.END)
        amount.insert(0, str(values[1]).replace("$", "").replace(",", ""))

        desc.delete(0, tk.END)
        desc.insert(0, values[3])

        category.set(values[2])

    def update_selected_ui():
        nonlocal selected_id

        if selected_id is None:
            messagebox.showwarning("Warning", "Select a row first.")
            return

        try:
            update_expense(
                selected_id,
                float(amount.get()),
                category.get(),
                desc.get()
            )

            selected_id = None
            clear_fields()
            refresh()

        except ValueError:
            messagebox.showerror("Error", "Invalid amount")

    # ======================
    # EVENTS
    # ======================
    table.bind("<<TreeviewSelect>>", load_selected)
    search_box.bind("<KeyRelease>", lambda e: refresh())

    # ======================
    # BUTTONS
    # ======================
    btn = tk.Frame(root)
    btn.pack(pady=10)

    tk.Button(btn, text="Add", width=15, command=add_expense_ui).grid(row=0, column=0, padx=5)
    tk.Button(btn, text="Update", width=15, command=update_selected_ui).grid(row=0, column=1, padx=5)
    tk.Button(btn, text="Delete", width=15, command=delete_selected).grid(row=0, column=2, padx=5)
    tk.Button(btn, text="Refresh", width=15, command=refresh).grid(row=0, column=3, padx=5)
    tk.Button(btn, text="Dashboard", width=15, command=open_dashboard).grid(row=0, column=4, padx=5)

    refresh()
    root.mainloop()