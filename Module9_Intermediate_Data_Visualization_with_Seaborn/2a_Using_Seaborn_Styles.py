# import all modules
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Plot the pandas histogram
df['fmr_2'].plot.hist()
plt.show()
plt.clf()

# Set the default seaborn style
sns.set()

# Plot the pandas histogram again
df['fmr_2'].plot.hist()
plt.show()
plt.clf()

# Plot with a dark style
sns.set_style('dark')
sns.distplot(df['fmr_2'])
plt.show()

# Clear the figure
plt.clf()

# Plot with a whitegrid style
sns.set_style('whitegrid')
sns.distplot(df['fmr_2'])
plt.show()

# Clear the figure
plt.clf()

# Set the style to white
sns.set_style('white')

# Create a regression plot
sns.lmplot(data=df,
           x='pop2010',
           y='fmr_2')

# Remove the spines
sns.despine()

# Show the plot and clear the figure
plt.show()
plt.clf()
