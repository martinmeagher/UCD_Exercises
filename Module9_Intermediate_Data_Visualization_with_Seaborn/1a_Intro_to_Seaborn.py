# import all modules
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read in the DataFrame
grant_file = 'schoolimprovement2010grants.csv'
df = pd.read_csv(grant_file)

# Display pandas histogram
df['Award_Amount'].plot.hist()
plt.show()

# Display a Seaborn distplot
sns.distplot(df['Award_Amount'])
plt.show()

# Clear the distplot
plt.clf()

# Clear out the pandas histogram
plt.clf()
