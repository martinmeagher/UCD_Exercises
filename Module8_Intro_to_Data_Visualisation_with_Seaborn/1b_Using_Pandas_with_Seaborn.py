# Import Pandas
import pandas as pd

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Print the head of df
print(df.head())

# Import Matplotlib, Pandas, and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Create a count plot with "Spiders" on the x-axis
sns.countplot(x="Spiders", data=df)

# Display the plot
plt.show()
