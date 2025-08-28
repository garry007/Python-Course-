import matplotlib.pyplot as plt
import numpy as np

# Sample data: Monthly sales and expenses for two years
months = np.arange(1, 13)
sales_2023 = [200, 220, 250, 270, 300, 320, 340, 360, 380, 400, 420, 450]
sales_2024 = [230, 260, 280, 310, 340, 360, 390, 410, 430, 460, 480, 500]
expenses_2023 = [180, 190, 200, 210, 230, 250, 270, 290, 310, 330, 350, 370]
expenses_2024 = [200, 210, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400]
sales_std = [10, 12, 15, 14, 13, 16, 15, 17, 16, 18, 17, 19]  # Standard deviation for error bands

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
totals = {
    'Sales 2023': sum(sales_2023),
    'Sales 2024': sum(sales_2024),
    'Expenses 2023': sum(expenses_2023),
    'Expenses 2024': sum(expenses_2024)
}
axs[1, 0].bar(totals.keys(), totals.values(), color=['blue', 'cyan', 'red', 'orange'])
axs[1, 0].set_title('Total Annual Sales and Expenses', fontsize=12)
axs[1, 0].set_ylabel('Total Amount ($)')
axs[1, 0].tick_params(axis='x', rotation=45)
for i, v in enumerate(totals.values()):
    axs[1, 0].text(i, v + 50, f'${v}', ha='center', fontsize=10)

# 4. Line Plot with Error Bands: Sales with Variability
axs[1, 1].plot(months, sales_2024, color='cyan', label='Sales 2024')
axs[1, 1].fill_between(months, np.array(sales_2024) - sales_std, np.array(sales_2024) + sales_std,
                       color='cyan', alpha=0.2, label='Error Band')
axs[1, 1].set_title('Sales 2024 with Variability', fontsize=12)
axs[1, 1].set_xlabel('Month')
axs[1, 1].set_ylabel('Sales ($)')
axs[1, 1].grid(True, linestyle='--', alpha=0.7)

# Shared legend outside the plots
handles, labels = axs[0, 0].get_legend_handles_labels()
fig.legend(handles, labels, loc='center right', bbox_to_anchor=(1.15, 0.5), fontsize=10)

# Display the plot
plt.show()