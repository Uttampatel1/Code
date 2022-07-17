

#https://medium.com/analytics-vidhya/netflix-movies-and-tvshows-exploratory-data-analysis-eda-and-visualization-using-python-80753fcfcf7


import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

netflix_df = pd.read_csv("netflix_titles.csv")

#print(netflix_df.head())

#print('\nColumns with missing value:') 
#print(netflix_df.isnull().any())

netflix_df.isnull().sum().sum()

netflix_df.director.fillna("No Director", inplace=True)
netflix_df.cast.fillna("No Cast", inplace=True)
netflix_df.country.fillna("Country Unavailable", inplace=True)
netflix_df.dropna(subset=["date_added", "rating"], inplace=True)

netflix_df.isnull().any()

# Netflix Content By Type
'''
plt.figure(figsize=(12,6))

plt.title("Percentation of Netflix Titles that are either Movies or TV Shows")

g = plt.pie(netflix_df.type.value_counts(),explode=(0.025,0.025), labels=netflix_df.type.value_counts().index, colors=['red','black'],autopct='%1.1f%%', startangle=180)

plt.show()

'''

#Amount of Content as a Function of Time
'''
fig, ax = plt.subplots(figsize=(13, 7))
sns.lineplot(data=netflix_year_df,x='year', y='date_added')

sns.lineplot(data=movies_year_df, x='year', y='date_added')

sns.lineplot(data=shows_year_df, x='year', y='date_added')

ax.set_xticks(np.arange(2008, 2020, 1))

plt.title('Total content added across all years (up to 2019)')

plt.legend(['Total','Movie','TV Show'])
plt.ylabel("Releases")
plt.xlabel("Year")
plt.show()

'''


#Countries by the Amount of the Produces Content
'''
filtered_countries = netflix_df.set_index('title').country.str.split(', ', expand=True).stack().reset_index(level=1, drop=True);

filtered_countries = filtered_countries[filtered_countries != 'Country Unavailable']

plt.figure(figsize=(13,7))

g = sns.countplot(y = filtered_countries, order=filtered_countries.value_counts().index[:15])

plt.title('Top 15 Countries Contributor on Netflix')

plt.xlabel('Titles')
plt.ylabel('Country')
plt.show()
'''




#Top Directors on Netflix
'''
filtered_directors = netflix_df[netflix_df.director != 'No Director'].set_index('title').director.str.split(', ', expand=True).stack().reset_index(level=1, drop=True)
plt.figure(figsize=(13,7))
plt.title('Top 10 Director Based on The Number of Titles')
sns.countplot(y = filtered_directors, order=filtered_directors.value_counts().index[:10], palette='Blues')
plt.show()
'''




#Top Genres on Netflix
'''
filtered_genres = netflix_df.set_index('title').listed_in.str.split(', ', expand=True).stack().reset_index(level=1, drop=True);
plt.figure(figsize=(10,10))
g = sns.countplot(y = filtered_genres, order=filtered_genres.value_counts().index[:20])
plt.title('Top 20 Genres on Netflix')
plt.xlabel('Titles')
plt.ylabel('Genres')
plt.show()
'''


order = netflix_df.rating.unique()
count_movies = netflix_movies_df.groupby('rating')['title'].count().reset_index()
count_shows = netflix_shows_df.groupby('rating')['title'].count().reset_index()
count_shows = count_shows.append([{"rating" : "NC-17", "title" : 0},{"rating" : "PG-13", "title" : 0},{"rating" : "UR", "title" : 0}], ignore_index=True)
count_shows.sort_values(by="rating", ascending=True)
plt.figure(figsize=(13,7))
plt.title('Amount of Content by Rating (Movies vs TV Shows)')
plt.bar(count_movies.rating, count_movies.title)
plt.bar(count_movies.rating, count_shows.title, bottom=count_movies.title)
plt.legend(['TV Shows', 'Movies'])
plt.show()

