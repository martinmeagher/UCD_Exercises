# Import pandas using the alias pd
import pandas as pd

# import relevant pickle files
movies = pd.read_pickle("movies.p")
financials = pd.read_pickle("financials.p")
taglines = pd.read_pickle("taglines.p")

# Merge movies and financials with a left join
movies_financials = movies.merge(financials, on="id", how="left")

# Count the number of rows in the budget column that are missing
number_of_missing_fin = movies_financials['budget'].isna().sum()

# Print the number of movies missing financials
print(number_of_missing_fin)

# Merge the toy_story and taglines tables with a left join
toystory_tag = toy_story.merge(taglines, on="id", how="left")

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)

# Merge the toy_story and taglines tables with a inner join
toystory_tag = toy_story.merge(taglines, on="id")

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)
