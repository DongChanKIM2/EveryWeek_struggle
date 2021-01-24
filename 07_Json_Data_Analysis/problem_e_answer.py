import json
from datetime import date

def dec_movies(movies):
    titles = []
    
    for movie in movies:
        id = movie['id']
        data_movies_json = open(f'data/movies/{id}.json', encoding='UTF8')
        data_movies_list = json.load(data_movies_json)
        if data_movies_list['release_date'][5:7] == '12':
            titles.append(data_movies_list['title'])
        #     revenue = data_movies_list['revenue']
        #     name = data_movies_list['title']
    return titles


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))