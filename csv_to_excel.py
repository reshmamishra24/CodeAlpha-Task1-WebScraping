import pandas as pd

df = pd.read_csv("books_data.csv")
df.to_excel("books_data.xlsx", index=False)
print("Excel File create: books_data.xlsx")