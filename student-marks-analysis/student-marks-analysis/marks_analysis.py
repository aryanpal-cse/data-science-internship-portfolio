import pandas as pd

data = {
    "Student": ["Amit", "Riya", "Aryan", "Neha", "Rahul"],
    "Math": [78, 85, 90, 67, 74],
    "Science": [82, 79, 88, 72, 69],
    "English": [75, 81, 84, 70, 77]
}

df = pd.DataFrame(data)

print("Student Marks Data")
print(df)

print("\nAverage Marks:")
print(df[["Math", "Science", "English"]].mean())

print("\nHighest Marks:")
print(df[["Math", "Science", "English"]].max())

print("\nLowest Marks:")
print(df[["Math", "Science", "English"]].min())
