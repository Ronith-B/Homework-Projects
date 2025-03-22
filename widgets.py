import tkinter as tk

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result_label.config(text=f"Product: {num1 * num2}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter numbers.")

root = tk.Tk()
root.title("Getting Started with Widgets")
root.geometry("400x300")

tk.Label(root, text="Enter two numbers to calculate their product:").pack(pady=10)

tk.Label(root, text="First Number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Second Number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Button(root, text="Calculate", command=calculate_product).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()