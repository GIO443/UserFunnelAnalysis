import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("funnel_data.csv")  # rename if your file has a different name

# Filter for conversions only
converted = data[data['conversion'] == True]

# Count unique users at each funnel stage
stage_counts = converted.groupby('stage')['user_id'].nunique().sort_values(ascending=False)

# Calculate conversion rates relative to homepage
conversion_rates = stage_counts / stage_counts.iloc[0]

# Print results to console
print("Stage Counts:\n", stage_counts)
print("\nConversion Rates:\n", conversion_rates)

# Plot funnel chart
plt.figure(figsize=(10, 6))
plt.barh(stage_counts.index[::-1], stage_counts.values[::-1])
plt.xlabel("Number of Users")
plt.title("User Funnel Drop-Off Analysis")
plt.tight_layout()
plt.savefig("funnel_chart.png")
plt.show()
