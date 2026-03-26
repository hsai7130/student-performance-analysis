import pandas as pd

data = {
    "Student": ["A", "B", "C", "D"],
    "Marks": [75, 85, 60, 90]
}

df = pd.DataFrame(data)

print("Average Marks:", df["Marks"].mean())

top = df.loc[df["Marks"].idxmax()]
print("Top Student:", top["Student"])
