# import all modules
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a distplot
sns.distplot(df['Award_Amount'],
             kde=False,
             bins=20)

# Display the plot
plt.show()

# Create a distplot of the Award Amount
sns.distplot(df['Award_Amount'],
             hist=False,
             rug=True,
             kde_kws={'shade': True})

# Plot the results
plt.show()
