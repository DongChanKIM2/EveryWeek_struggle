import requests
from tmdb import URLMaker
from pprint import pprint


def ranking():
    key_value = 'f4e4ad237c7fb44ea8e4abb88193fa30'
    maker = URLMaker(key_value)
    url = maker.get_url('movie', 'popular')
    res = requests.get(url)
    movie_dict = res.json()
    movie_list = movie_dict.get('results')

    # 평점 기준으로 정렬해야 하므로 평점 담을 temp 공간 생성
    vote_average_result = []
    for i in range(len(movie_list)):
        vote_average_result.append(movie_list[i]['vote_average'])
    
    # Bubble sort
    n = len(vote_average_result)
    for i in range(n):
        for j in range(n-1, i, -1):
            if vote_average_result[j] > vote_average_result[j-1]:
                vote_average_result[j], vote_average_result[j-1] = vote_average_result[j-1], vote_average_result[j]
                movie_list[j], movie_list[j-1] = movie_list[j-1], movie_list[j]
    
    return movie_list[0:5]

if __name__ == '__main__':
    # popular 영화 평점순 5개 출력
    pprint(ranking())
