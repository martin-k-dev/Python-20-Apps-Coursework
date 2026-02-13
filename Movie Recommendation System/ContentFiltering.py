import pandas
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class ContentFiltering:
    def __init__(self, file_to_read='movies_small.csv', separator=';'):
        self.movies = pandas.read_csv(file_to_read, sep=separator)
        self.similarity_matrix = self.get_similarity_matrix()

    def get_similarity_matrix(self):
        tfidf = TfidfVectorizer(stop_words="english")

        self.movies["overview"] = self.movies["overview"].fillna("")

        tfidf_matrix = tfidf.fit_transform(self.movies["overview"])

        pandas.DataFrame(tfidf_matrix.toarray(), columns=tfidf.get_feature_names_out())

        similarity_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)

        return similarity_matrix

    def similar_movies(self, movie_title, nr_movies):
        """
        :param movie_title: the function finds similar movies to this one
        :param nr_movies: how many movies to return
        :return:
        """
        # Index of a movie title
        try:
            idx = self.movies.loc[self.movies["title"] == movie_title].index[0]
        except IndexError:
            return "Could not find a movie with that name"

        scores = list(enumerate(self.similarity_matrix[idx]))

        scores_sorted = sorted(scores, key=lambda x: x[1], reverse=True)

        movies_indices = [tpl[0] for tpl in scores_sorted[1:nr_movies + 1]]

        similar_titles = list(self.movies["title"].iloc[movies_indices])
        return similar_titles

if __name__ == "__main__":
    print(ContentFiltering().similar_movies('Kung Fu Panda 3', 3))
    # ['John Carter', 'Furious 7', 'Cars 2']