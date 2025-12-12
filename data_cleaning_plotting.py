import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("gene_expression_sample.csv")

# Display first rows
print("Initial Dataset:")
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values with column mean
df_filled = df.fillna(df.mean(numeric_only=True))

print("\nAfter Filling Missing Values:")
print(df_filled)

# Summary statistics
print("\nSummary Statistics:")
print(df_filled.describe())

# Plot 1: Bar plot of average expression per gene
avg_expression = df_filled.mean(axis=1)
plt.figure(figsize=(8,5))
plt.bar(df['Gene'], avg_expression)
plt.title("Average Gene Expression Levels")
plt.xlabel("Gene")
plt.ylabel("Expression Value")
plt.tight_layout()
plt.savefig("avg_expression_plot.png")
plt.show()

# Plot 2: Line plot of sample-wise variance
sample_variance = df_filled.var(axis=0)
plt.figure(figsize=(8,5))
plt.plot(sample_variance)
plt.title("Variance Across Samples")
plt.xlabel("Sample")
plt.ylabel("Variance")
plt.tight_layout()
plt.savefig("sample_variance_plot.png")
plt.show()
