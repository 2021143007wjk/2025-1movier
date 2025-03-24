import joblib

import pandas as pd
from scipy.sparse import coo_matrix
import numpy as np
from implicit.als import AlternatingLeastSquares

from app.movie_preprocess import rating_df

data_fname = "data/ratings.csv"
item_fname = "data/movies_final.csv"
saved_model_fname = "data/model_final.sav"
weight = 10

def model_train():
    rating_df = pd.read_csv(data_fname)
    rating_df['userId'] = rating_df['userId'].astype("category")
    rating_df['movieId'] = rating_df['movieId'].astype("category")
    rating_matrix = coo_matrix( #희소행렬
        (
            rating_df['rating'].astype(np.float32),
            (
                rating_df['movieId'].cat.codes.copy(),
                rating_df['userId'].cat.codes.copy(),
            ),
        )
    )
    als_model = AlternatingLeastSquares(factors=50, regularization=0.01, iterations=50, dtype=np.float64)
    als_model.fit(rating_matrix * weight)
    joblib.dump(als_model, saved_model_fname)
    return

model = model_train()