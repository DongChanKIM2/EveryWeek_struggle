import json


def max_revenue(movies):
    revenue = 0
    name = ''
    for movie in movies:
        id = movie['id']
        data_movies_json = open(f'data/movies/{id}.json', encoding='UTF8')
        data_movies_list = json.load(data_movies_json)
        if data_movies_list['revenue'] > revenue:
            revenue = data_movies_list['revenue']
            name = data_movies_list['title']
    return name

#    data_movies_json = 
 
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))