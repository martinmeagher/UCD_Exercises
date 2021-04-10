# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower",
            y="mpg",
            kind="scatter",
            data=mpg,
            size="cylinders")

# Show plot
plt.show()

# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower", y="mpg",
            data=mpg, kind="scatter",
            size="cylinders", hue="cylinders")

# Show plot
plt.show()

# Create a scatter plot of acceleration vs. mpg
sns.relplot(x="acceleration",
            y="mpg",
            kind="scatter",
            data=mpg,
            hue="origin",
            style="origin")

# Show plot
plt.show()
