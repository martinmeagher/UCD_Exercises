# import all modules
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set style, enable color code, and create a magenta distplot
sns.set(color_codes=True)
sns.distplot(df['fmr_3'], color='m')

# Show the plot
plt.show()

# Loop through differences between bright and colorblind palettes
for p in ['bright', 'colorblind']:
    sns.set_palette(p)
    sns.distplot(df['fmr_3'])
    plt.show()

    # Clear the plots
    plt.clf()

# Create the Purples palette
sns.palplot(sns.color_palette("Purples", 8))
plt.show()

# Create the husl palette
sns.palplot(sns.color_palette("husl", 10))
plt.show()

# Create the coolwarm palette
sns.palplot(sns.color_palette("coolwarm", 6))
plt.show()
