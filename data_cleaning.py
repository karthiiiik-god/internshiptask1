import pandas as pd

# Load dataset
df = pd.read_csv("dataset_raw.csv")

# Check missing values
print("Missing values:\n", df.isnull().sum())

# Drop rows with missing Name
df = df.dropna(subset=["Name"])

# Fill missing Salary with median
df["Salary"] = df["Salary"].fillna(df["Salary"].median())

# Remove duplicates
df = df.drop_duplicates()

# Standardize text
df["Name"] = df["Name"].str.strip().str.title()
df["Gender"] = df["Gender"].str.strip().str.lower()

# Convert date column
df["Join Date"] = pd.to_datetime(df["Join Date"], errors="coerce")

# Remove unrealistic ages
df = df[df["Age"] <= 100]

# Rename columns
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)

print("Data cleaning completed.")
