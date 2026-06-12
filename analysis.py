import pandas as pd

df = pd.read_csv("student_marks.csv")

print("Missing Values:")
print(df.isnull().sum())

print("\nDuplicates:")
print(df.duplicated().sum())

df["Average"] = df[["Maths","Science","English"]].mean(axis=1)

print(df)

topper = df.loc[df["Average"].idxmax()]
print("\nTop Scorer:")
print(topper)
