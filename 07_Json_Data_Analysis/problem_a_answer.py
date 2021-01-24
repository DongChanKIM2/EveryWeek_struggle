import json
from pprint import pprint


def movie_info(movie):
    # dict에서 정보 추출(key or get or request)
    genre_ids = movie['genre_ids']
    id = movie['id']
    overview = movie['overview']
    poster_path = movie['poster_path']
    title = movie['title']
    vote_average = movie.get('vote_average')

    # 추출한 정보 새로운 dict에 첨부
    movie_dict = {}
    movie_dict['genre_ids'] = genre_ids
    movie_dict['id'] = id
    movie_dict['overview'] = overview
    movie_dict['poster_path'] = poster_path
    movie_dict['title'] = title
    movie_dict['vote_average'] = vote_average

    return movie_dict
    # 여기에 코드를 작성합니다.    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))