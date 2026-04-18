import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from core.reports import get_monthly_totals, get_category_totals


def open_dashboard():
    win = tk.Toplevel()
    win.title("Dashboard")
    win.geometry("950x700")

    fig = plt.Figure(figsize=(9, 6), dpi=100)

    # Bar chart
    ax1 = fig.add_subplot(211)
    monthly = get_monthly_totals()

    ax1.bar(list(monthly.keys()), list(monthly.values()))
    ax1.set_title("Monthly Spending")
    ax1.tick_params(axis="x", rotation=45)

    # Pie chart
    ax2 = fig.add_subplot(212)
    cats = get_category_totals()

    if cats:
        ax2.pie(
            list(cats.values()),
            labels=list(cats.keys()),
            autopct="%1.1f%%"
        )
        ax2.set_title("Spending by Category")

    fig.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)