import json
from pprint import pprint


def movie_info(movies, genres):
    movie_list = []
    # list이므로 for문으로 개별 데이터 추출    
    for movie in movies:
        # dict에서 정보 추출(key or get or request)
        genre_ids = movie['genre_ids']
        id = movie['id']
        overview = movie['overview']
        poster_path = movie['poster_path']
        title = movie['title']
        vote_average = movie.get('vote_average')

        # movie에서 추출한 정보 genres 데이터를 활용해 개별 변환
        new_genre_ids = []
        for genre in genres:
            for i in range(len(genre_ids)):
                if genre['id'] == genre_ids[i]:
                    new_genre_ids.append(genre['name'])

        # 추출한 정보 새로운 dict에 첨부
        movie_dict = {}
        movie_dict['genre_names'] = new_genre_ids
        movie_dict['id'] = id
        movie_dict['overview'] = overview
        movie_dict['poster_path'] = poster_path
        movie_dict['title'] = title
        movie_dict['vote_average'] = vote_average
        movie_list.append(movie_dict)

    return movie_list  
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))