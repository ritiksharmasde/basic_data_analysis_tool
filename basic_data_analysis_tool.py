# -----------------------------------------------------------
import pandas as pd
import numpy as np
file_path = "output.csv"  
try:
    data = pd.read_csv(file_path)
    print("Data Loaded Successfully")
    print(data.head())  
except Exception as e:
    print(f"Error loading file: {e}")
    exit()


column_name = "Med. Age"
if column_name in data.columns:
    try:
        
        data[column_name] = pd.to_numeric(data[column_name], errors='coerce')  
        print(f"Column '{column_name}' successfully converted to numeric!")
    except ValueError as e:
        print(f"Error converting column '{column_name}': {e}")
else:
    print(f"Column '{column_name}' not found in the dataset!")

# -----------------------------------------------------------


column_name = "Med. Age"  
if column_name not in data.columns:
    print(f"Column '{column_name}' not found in dataset!")
    exit()


data[column_name] = pd.to_numeric(data[column_name], errors='coerce')  
values = data[column_name].dropna() 

mean = np.mean(values)
median = np.median(values)

mode = values.mode()[0] if not values.mode().empty else None  
variance = np.var(values)
std_deviation = np.std(values)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"variance: {variance}")
print(f"standard deviation: {std_deviation}")