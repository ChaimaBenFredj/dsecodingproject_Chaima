# Project code will be shown here



# Loading the datasets
import pandas as pd

# Loading the relevant columns from each dataset
movies_df = pd.read_csv('Dataset/movie.tsv', sep='\t', usecols=['tconst', 'primaryTitle', 'genres'])
ratings_df = pd.read_csv('Dataset/ratings.tsv', sep='\t', usecols=['tconst', 'averageRating', 'numVotes'])
crew_df = pd.read_csv('Dataset/crew.tsv', sep='\t', usecols=['tconst', 'nconst', 'category'])
person_df = pd.read_csv('Dataset/person.tsv', sep='\t', usecols=['nconst', 'primaryName', 'birthYear','deathYear','primaryProfession'])

# You can now work with the datasets and perform analysis or merge them as needed.
print(ratings_df.head(5))