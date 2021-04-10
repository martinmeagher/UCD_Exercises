# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot of absences vs. final grade
sns.scatterplot(x="absences", y="G3", data=student_data, hue="location")

# Show plot
plt.show()

# Change the legend order in the scatter plot
sns.scatterplot(x="absences", y="G3",
                data=student_data,
                hue="location", hue_order=["Rural", "Urban"])

# Show plot
plt.show()

# Create a dictionary mapping subgroup values to colors
palette_colors = {"Rural": "green", "Urban": "blue"}

# Create a count plot of school with location subgroups
# Change the legend order in the scatter plot
sns.countplot(x="school",
                data=student_data,
                hue="location", palette=palette_colors)

# Display plot
plt.show()
