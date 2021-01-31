import requests
from tmdb import URLMaker
from pprint import pprint


def popular_count():
    # 인증키 및 class 호출
    key_value = 'f4e4ad237c7fb44ea8e4abb88193fa30'
    maker = URLMaker(key_value)
    # class 내부의 get_url 함수로 url 가져오기
    url = maker.get_url()
    
    # get_url 내부에 기본인자가 설정되어 있기 때문에 해도 되고 안해도 됨
    # url = maker.get_url('movie', 'popular')
    res = requests.get(url)
    movie_dict = res.json()
    movie_list = movie_dict.get('results')
   
    result = []
    for movie in movie_list:
        result.append(movie.get('title'))
    return len(result)

if __name__ == '__main__':
    pprint(popular_count())
