# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Change to use relplot() instead of scatterplot()
sns.relplot(x="absences", y="G3",
                data=student_data, kind="scatter")

# Show plot
plt.show()

# Change to make subplots based on study time
sns.relplot(x="absences", y="G3",
            data=student_data,
            kind="scatter", col="study_time")

# Show plot
plt.show()

# Change this scatter plot to arrange the plots in rows instead of columns
sns.relplot(x="absences", y="G3",
            data=student_data,
            kind="scatter",
            row="study_time")

# Show plot
plt.show()

# Create a scatter plot of G1 vs. G3
sns.relplot(x="G1", y="G3",
                data=student_data, kind="scatter")

# Show plot
plt.show()

# Adjust further to add subplots based on family support
sns.relplot(x="G1", y="G3",
            data=student_data,
            kind="scatter",
            col="schoolsup",
            col_order=["yes", "no"])

# Show plot
plt.show()

# Adjust further to add subplots based on family support
sns.relplot(x="G1", y="G3",
            data=student_data,
            kind="scatter",
            col="schoolsup",
            col_order=["yes", "no"],
            row="famsup",
            row_order=["yes", "no"])

# Show plot
plt.show()
