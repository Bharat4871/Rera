import tkinter as tk
from tkinter import messagebox

def calculate_cagr(investment, returns, total_years):
    try:
        if investment <= 0 or returns <= 0 or total_years <= 0:
            return 0.0
        return ((returns / investment) ** (1 / total_years) - 1) * 100
    except:
        return 0.0

def on_calculate():
    try:
        monthly_premium = float(entry_premium.get())
        premium_years = int(entry_premium_years.get())
        start_year = int(entry_start_year.get())
        repay_years = int(entry_repay_years.get())
        monthly_return = float(entry_return.get())

        total_investment = monthly_premium * premium_years * 12
        total_return = monthly_return * repay_years * 12
        total_years = start_year + repay_years

        cagr = calculate_cagr(total_investment, total_return, total_years)

        result_text.set(
            f"Total Investment: ₹{total_investment:,.2f}\n"
            f"Total Return: ₹{total_return:,.2f}\n"
            f"Total Duration: {total_years} years\n"
            f"CAGR: {cagr:.2f}%"
        )
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers in all fields.")

# --- GUI Setup ---
app = tk.Tk()
app.title("CAGR Calculator App")
app.geometry("400x400")
app.configure(bg="#f0f0f0")

# --- Labels & Entries ---
tk.Label(app, text="Monthly Premium (₹):", bg="#f0f0f0").pack(pady=5)
entry_premium = tk.Entry(app)
entry_premium.pack()

tk.Label(app, text="Premium Payment Years:", bg="#f0f0f0").pack(pady=5)
entry_premium_years = tk.Entry(app)
entry_premium_years.pack()

tk.Label(app, text="Repayment Starts After (years):", bg="#f0f0f0").pack(pady=5)
entry_start_year = tk.Entry(app)
entry_start_year.pack()

tk.Label(app, text="Repayment Duration (years):", bg="#f0f0f0").pack(pady=5)
entry_repay_years = tk.Entry(app)
entry_repay_years.pack()

tk.Label(app, text="Expected Monthly Return (₹):", bg="#f0f0f0").pack(pady=5)
entry_return = tk.Entry(app)
entry_return.pack()

tk.Button(app, text="Calculate CAGR", command=on_calculate, bg="blue", fg="white").pack(pady=15)

result_text = tk.StringVar()
tk.Label(app, textvariable=result_text, bg="#f0f0f0", fg="green", font=("Arial", 10), justify="center", wraplength=300).pack(pady=10)

# Run the app
app.mainloop()
