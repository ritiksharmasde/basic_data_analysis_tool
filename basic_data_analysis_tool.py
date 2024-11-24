import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import numpy as np

class DataAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Data Analysis Tool by RITIK SHARMA")
        self.root.geometry("600x400")

        self.data = None
        self.column_name = ""

        tk.Label(root, text="Data Analysis Tool", font=("Arial", 16)).pack(pady=10)

        frame = tk.Frame(root)
        frame.pack(pady=20)

        tk.Button(frame, text="Load CSV File", command=self.load_file).grid(row=0, column=0, padx=10)
        tk.Label(frame, text="Column Name:").grid(row=0, column=1, padx=5)
        self.column_entry = tk.Entry(frame)
        self.column_entry.grid(row=0, column=2, padx=10)
        tk.Button(frame, text="Analyze", command=self.analyze_column).grid(row=0, column=3, padx=10)

        self.output_text = tk.Text(root, height=15, width=70)
        self.output_text.pack(pady=10)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            return
        try:
            self.data = pd.read_csv(file_path)
            self.output_text.insert(tk.END, "File loaded successfully!\n")
            self.output_text.insert(tk.END, f"Columns: {', '.join(self.data.columns)}\n")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {e}")

    def analyze_column(self):
        if self.data is None:
            messagebox.showerror("Error", "No file loaded!")
            return

        self.column_name = self.column_entry.get()
        if not self.column_name:
            messagebox.showerror("Error", "Please enter a column name!")
            return

        if self.column_name not in self.data.columns:
            messagebox.showerror("Error", f"Column '{self.column_name}' not found in dataset!")
            return

        try:
            self.data[self.column_name] = pd.to_numeric(self.data[self.column_name], errors='coerce')
            values = self.data[self.column_name].dropna()

            mean = np.mean(values)
            median = np.median(values)
            mode = values.mode()[0] if not values.mode().empty else "No mode"
            variance = np.var(values)
            std_deviation = np.std(values)

            self.output_text.insert(tk.END, f"Analysis for column '{self.column_name}':\n")
            self.output_text.insert(tk.END, f"Mean: {mean}\n")
            self.output_text.insert(tk.END, f"Median: {median}\n")
            self.output_text.insert(tk.END, f"Mode: {mode}\n")
            self.output_text.insert(tk.END, f"Variance: {variance}\n")
            self.output_text.insert(tk.END, f"Standard Deviation: {std_deviation}\n\n")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to analyze column: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DataAnalysisApp(root)
    root.mainloop()
