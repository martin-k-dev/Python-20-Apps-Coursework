# Note to myself - py -m jupyterlab
from surprise import Dataset, Reader, SVD, model_selection
import pandas

def collaborative_filtering(userId, movieId):
    """
    Predicts how a certain user might rate a certain movie.
    Return an estimated value

    Had some problems with installing scikit.surprise on newer python version,
    but the code should run fine.
    """
    ratings = pandas.read_csv("ratings.csv")[["userId", "movieId", "rating"]]

    reader = Reader(rating_scale=(1,5))

    dataset = Dataset.load_from_df(ratings, reader)

    trainset = dataset.build_full_trainset()

    svd = SVD()

    svd.fit(trainset)

    # Predict how a certain user rates a movie
    # and return an estimation value
    return svd.predict(userId,movieId).est

    # Extra command for validation
    # model_selection.cross_validate(svd, dataset, measures=["RMSE", "MAE"])