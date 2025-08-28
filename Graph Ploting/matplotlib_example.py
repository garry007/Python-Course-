
import matplotlib.pyplot as plt
import numpy as np
import json

# Read plot data from JSON file
with open('Graph Ploting/plot_data.json', 'r') as f:
    data = json.load(f)

months = np.array(data["months"])
sales_2023 = data["sales_2023"]
sales_2024 = data["sales_2024"]
expenses_2023 = data["expenses_2023"]
expenses_2024 = data["expenses_2024"]
sales_std = data["sales_std"]

# Create a 2x2 subplot grid
fig, axs = plt.subplots(2, 2, figsize=(12, 10), constrained_layout=True)

# 1. Line Plot: Sales and Expenses Trends
axs[0, 0].plot(months, sales_2023, marker='o', linestyle='-', color='blue', label='Sales 2023')
axs[0, 0].plot(months, sales_2024, marker='s', linestyle='--', color='cyan', label='Sales 2024')
axs[0, 0].plot(months, expenses_2023, marker='^', linestyle='-', color='red', label='Expenses 2023')
axs[0, 0].plot(months, expenses_2024, marker='d', linestyle='--', color='orange', label='Expenses 2024')
axs[0, 0].set_title('Monthly Sales and Expenses (2023 vs 2024)', fontsize=12)
axs[0, 0].set_xlabel('Month')
axs[0, 0].set_ylabel('Amount ($)')
axs[0, 0].grid(True, linestyle='--', alpha=0.7)
axs[0, 0].annotate('Peak Sales', xy=(12, 500), xytext=(10, 510),
                   arrowprops=dict(facecolor='black', shrink=0.05))

# 2. Scatter Plot: Sales vs Expenses with Trend Line
axs[0, 1].scatter(sales_2023, expenses_2023, color='blue', label='2023', s=100, alpha=0.6)
axs[0, 1].scatter(sales_2024, expenses_2024, color='cyan', label='2024', s=100, alpha=0.6)
# Fit a linear trend line for 2024 data
z = np.polyfit(sales_2024, expenses_2024, 1)
p = np.poly1d(z)
axs[0, 1].plot(sales_2024, p(sales_2024), "k--", label='Trend 2024')
axs[0, 1].set_title('Sales vs Expenses', fontsize=12)
axs[0, 1].set_xlabel('Sales ($)')
axs[0, 1].set_ylabel('Expenses ($)')
axs[0, 1].set_yscale('log')  # Logarithmic scale for y-axis
axs[0, 1].grid(True, which="both", linestyle='--', alpha=0.7)


# 3. Bar Plot: Total Annual Sales and Expenses
bar_width = 0.35
index = np.arange(2)
total_sales = [sum(sales_2023), sum(sales_2024)]
total_expenses = [sum(expenses_2023), sum(expenses_2024)]

axs[1, 0].bar(index, total_sales, bar_width, label='Total Sales', color='green')
axs[1, 0].bar(index + bar_width, total_expenses, bar_width, label='Total Expenses', color='red')
axs[1, 0].set_xlabel('Year')
axs[1, 0].set_ylabel('Total Amount ($)')
axs[1, 0].set_title('Total Annual Sales vs Expenses')
axs[1, 0].set_xticks(index + bar_width / 2)
axs[1, 0].set_xticklabels(['2023', '2024'])
axs[1, 0].legend()
axs[1, 0].grid(True, axis='y', linestyle='--', alpha=0.7)

# 4. Error Bar Plot: Sales 2023 with Standard Deviation
axs[1, 1].errorbar(months, sales_2023, yerr=sales_std, fmt='-o', color='purple', ecolor='gray', capsize=5, label='Sales 2023')
axs[1, 1].set_title('Sales 2023 with Error Bars')
axs[1, 1].set_xlabel('Month')
axs[1, 1].set_ylabel('Sales ($)')
axs[1, 1].grid(True, linestyle='--', alpha=0.7)
axs[1, 1].legend()

plt.show()
