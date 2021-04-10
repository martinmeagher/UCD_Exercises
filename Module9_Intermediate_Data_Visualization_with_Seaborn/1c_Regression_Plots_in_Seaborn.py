# Create a regression plot of premiums vs. insurance_losses
sns.regplot(data=df, x="insurance_losses", y="premiums")

# Display the plot
plt.show()

# Create an lmplot of premiums vs. insurance_losses
sns.lmplot(data=df,  x="insurance_losses", y="premiums")

# Display the second plot
plt.show()

# Create a regression plot using hue
sns.lmplot(data=df,
           x="insurance_losses",
           y="premiums",
           hue="Region")

# Show the results
plt.show()

# Create a regression plot with multiple rows
sns.lmplot(data=df,
           x="insurance_losses",
           y="premiums",
           row="Region")

# Show the plot
plt.show()
