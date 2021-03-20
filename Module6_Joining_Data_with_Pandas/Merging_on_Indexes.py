# Import pandas using the alias pd
import pandas as pd

# import relevant pickle files
movies = pd.read_pickle("movies.p")
ratings = pd.read_pickle("ratings.p")
sequels = pd.read_pickle("sequels.p")
financials = pd.read_pickle("financials.p")

# Merge to the movies table the ratings table on the index
movies_ratings = movies.merge(ratings, on="id", how="left")

# Print the first few rows of movies_ratings
print(movies_ratings.head())

# Merge sequels and financials on index id
sequels_fin = sequels.merge(financials, on='id', how='left')

# Self merge with suffixes as inner join with left on sequel and right on id
orig_seq = sequels_fin.merge(sequels_fin, how='inner', left_on='sequel',
                             right_on='id', right_index=True,
                             suffixes=('_org','_seq'))

# Add calculation to subtract revenue_org from revenue_seq
orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']

# Select the title_org, title_seq, and diff
titles_diff = orig_seq[['title_org', 'title_seq', 'diff']]

# Print the first rows of the sorted titles_diff
print(titles_diff.sort_values("diff", ascending=False).head())
