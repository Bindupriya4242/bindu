import pandas as pd

# Example DataFrame
data = {'A': [1, 2, 3, 4], 'B': [4, 3, 2, 1], 'C': [5, 6, 7, 8]}
index = ['D1', 'D2', 'A1', 'B1']
df = pd.DataFrame(data, index=index)

# Select rows where index starts with 'D' and rank columns A, B, C
ranked_df = df.loc[df.index.str.startswith('D'), ['A', 'B', 'C']].rank()

print(ranked_df)
