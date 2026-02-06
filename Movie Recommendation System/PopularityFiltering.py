import pandas

movies = pandas.read_csv('movies.csv')
# credits = pandas.read_csv('credits.csv')
# ratings = pandas.read_csv('ratings.csv')

class PopularityFiltering:
    def __init__(self):
        self.avg_rating_multiple_movies = movies["vote_average"].mean()
        self.minimum_votes = movies["vote_count"].quantile(0.9)

    def weighted_rating(self, df, m=""):
        if m is "":
            m = self.minimum_votes
        avg_rating_movie = df["vote_average"]
        votes_for_movie = df["vote_count"]

        wr = (((votes_for_movie / votes_for_movie + m) * avg_rating_movie) +
              (m / (votes_for_movie + m) * self.avg_rating_multiple_movies))
        return wr

    def top_x_movies(self, x):
        """
        :param x: Number of movies to return
        :return: Returns an x long dictionary with this format
        {
        'title': {'movieId': 'MovieName'},
        'weighted_rating': {'movieId': 'the_rating'}
        }
        """
        movies_filtered = movies.copy().loc[movies["vote_count"] >= self.minimum_votes]

        movies_filtered["weighted_rating"] = movies_filtered.apply(self.weighted_rating, axis=1)

        return (movies_filtered.sort_values("weighted_rating", ascending=False)[["title", "weighted_rating"]]
                .head(x).to_dict())

if __name__ == "__main__":
    pop_filter = PopularityFiltering()
    print(pop_filter.top_x_movies(x=25))
