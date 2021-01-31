import requests
from tmdb import URLMaker
from pprint import pprint


def vote_average_movies():
    key_value = 'f4e4ad237c7fb44ea8e4abb88193fa30'
    maker = URLMaker(key_value)
    url = maker.get_url('movie', 'popular')
    res = requests.get(url)
    movie_dict = res.json()
    movie_list = movie_dict.get('results')
    
    result = []
    # 평점 8점 이상의 조건 추가
    for movie in movie_list:
        if movie['vote_average'] >= 8:
            result.append(movie.get('title'))
    return result

if __name__ == '__main__':
    pprint(vote_average_movies())    
