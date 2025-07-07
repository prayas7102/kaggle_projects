import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv('df.csv')

# Draw histogram of 'Age' column
plt.hist(df['Episode_Length_squared'], bins=5, edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
