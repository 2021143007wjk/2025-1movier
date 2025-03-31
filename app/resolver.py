import pandas as pd

def random_items():
    movies_df = pd.read_csv("data/movies_final.csv")
    movies_df = movies_df.fillna('')
    result_items = movies_df.sample(n=10).to_dict("records")
    return result_items

def random_genres_items(genre):
    movies_df = pd.read_csv("data/movies_final.csv")
    movies_df = movies_df.fillna('')
    genre_df = movies_df[movies_df['genres'].str.contains(genre)]
    # 선택한 장르의 갯수가 5보다 작은 경우 처리
    if len(genre_df) > 5:
        result_genres_items = genre_df.sample(n=5).to_dict("records")
    else :
        result_genres_items = genre_df.sample(n=len(genre_df)).to_dict("records")
    return result_genres_items

# 지정된 장르의 영화 중 평점이 높은 영화 추천
def random_genres_items_best(genre):
    movies_df = pd.read_csv("data/movies_final.csv")
    movies_df = movies_df.fillna('')
    genre_df = movies_df[(movies_df['genres'].str.contains(genre)) & (movies_df['rcount'] >= 5)].sort_values(by ='rmean' ,ascending= False)
    # 선택한 장르의 갯수가 5보다 작은 경우 처리
    result_genres_items = genre_df[:5].to_dict("records")
    return result_genres_items
