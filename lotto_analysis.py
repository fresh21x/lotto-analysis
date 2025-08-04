import pandas as pd
from collections import defaultdict

# Data from user: draw results
draw_data = [
    (2025, 8, 3, [3, 11, 12, 18, 46], 12),
    (2025, 8, 2, [3, 11, 12, 18, 46], 12),
    (2025, 7, 30, [12, 14, 32, 35, 47], 7),
    (2025, 7, 26, [2, 10, 29, 32, 37], 26),
    (2025, 7, 23, [9, 10, 34, 42, 45], 14),
    (2025, 7, 19, [4, 18, 19, 33, 43], 20),
    (2025, 7, 16, [4, 6, 8, 31, 46], 22),
    (2025, 7, 12, [4, 7, 10, 36, 46], 26),
    (2025, 7, 9, [14, 18, 29, 37, 44], 21),
    (2025, 7, 5, [7, 13, 20, 35, 44], 8),
    (2025, 7, 2, [6, 9, 11, 20, 30], 14),
    (2025, 6, 28, [3, 16, 27, 30, 33], 13),
    (2025, 6, 25, [12, 13, 23, 39, 42], 24),
    (2025, 6, 21, [14, 19, 31, 45, 47], 11),
    (2025, 6, 18, [20, 29, 33, 40, 41], 6),
    (2025, 6, 14, [7, 8, 30, 35, 39], 4),
    (2025, 6, 11, [4, 12, 27, 28, 42], 17),
    (2025, 6, 7, [16, 24, 38, 40, 45], 7),
    (2025, 6, 4, [4, 12, 16, 18, 34], 24),
    (2025, 5, 31, [3, 14, 29, 33, 47], 17),
    (2025, 5, 21, [20, 22, 28, 29, 45], 18),
    (2025, 5, 17, [11, 17, 18, 40, 44], 24),
    (2025, 5, 14, [6, 19, 39, 42, 46], 8),
    (2025, 5, 10, [7, 10, 11, 21, 32], 5),
    (2025, 5, 7, [8, 23, 38, 40, 41], 1),
    (2025, 5, 3, [3, 19, 30, 39, 46], 22),
]

# Convert data to pandas DataFrame
df = pd.DataFrame(draw_data, columns=['Year', 'Month', 'Day', 'Numbers', 'Mega'])

# Step 1: Calculate gaps
def calculate_gaps(df):
    gaps = defaultdict(list)
    
    for i, row in df.iterrows():
        for number in row['Numbers']:
            gaps[number].append(i)
    
    gap_counts = {number: len(indices) for number, indices in gaps.items()}
    return gap_counts

# Step 2: Select 10 combos based on gaps and frequency
gap_counts = calculate_gaps(df)
frequent_numbers = sorted(gap_counts.items(), key=lambda x: x[1], reverse=True)[:10]

# Display results
print("Top 10 numbers likely to appear:")
for number, count in frequent_numbers:
    print(f"Number: {number}, Occurrences: {count}")

