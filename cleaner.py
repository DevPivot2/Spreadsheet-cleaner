import pandas as pd
df = pd.read_csv("messy_data.csv")

# Remove duplicates and fully empty rows
df = df.drop_duplicates().dropna(how="all")

# Standardize text
df["name"] = df["name"].str.strip().str.title()

# Fix dates and numbers
df["date"] = pd.to_datetime(df["date"], errors="coerce", format="mixed")
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

#Flags rows with missing or invalid amounts BEFORE Filling them
bad= df[df["amount"].isna()]
if len(bad) > 0:
    print(f"Warning: {len(bad)} rows had missing or invalid amounts:")
    print(bad)

# Fill missing amounts with 0
df["amount"] = df["amount"].fillna(0)

df.to_csv("clean_data.csv", index=False)
print(f"Cleaned {len(df)} rows")
print(df["amount"].describe())


    